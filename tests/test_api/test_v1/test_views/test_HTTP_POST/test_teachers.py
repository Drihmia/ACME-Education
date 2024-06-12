#!/usr/bin/python3
"""
Test casses for the teachers API. It cover for approx. all sensitive cases.

Variable naming conviction:
    - marko: Statnds for the responce object when using "requests" library.
    - polo: The object created when using methods of on "marko".
            Usually is the human readable version of "marko"
            or the content we intend on doing further processing on.
            The both originate from the famous childrens' hide and seek game,
            where one child screems "MARKO!" and the other one replies "POLO!"
            in response to his call.
    - elem: Short for element. This looping variable is used to hold
            the content of the current iteration object
            that we will do proccessing on.
"""
import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "teachers"
# The information for the new institute that will be created
tempData = {"first_name": "Catz",
            "last_name": "Candy",
            "email": "temp@catvill.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "institution_id": "00014fb3-eed2-43e8-a99d-2845be4c4f4f",
            "city_id": "f5f202a7-4de8-4173-a7e9-9b0d94b9f6dei",
            "gender": "M"
            }
# Headers needed by the application
head = {"Content-Type": "application/json"}
link = base + toTest


def test_data_not_JSON():
    """checks when data is not a proper JSON"""
    with req.post(link, data=tempData,
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}


def test_no_data():
    """Checks when no data is sent"""
    with req.post(link, data=json.dumps({}),
                  headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}


def test_other_data_passed():
    """Checks when other info is sent"""
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400


def test_correct_data():
    """Checks when everything is in order"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 201
        assert marko.json()["name"] == tempData["name"]
        # Saving the ID
        tempID = marko.json()["id"]
    # Formulating a link using it
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["name"] == tempData["name"]
    with req.get(link) as marko:
        # Getting count after object creation
        new = len(marko.json())
        assert count == new + 1


def test_missing_email():
    """Checks when email is missing"""
    # Data needed for the test case
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "institution": "CATZ",
            "subject": "Feline Behaviour"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing email"}


def test_email_exists():
    """Checks when email is repeated"""
    # Data needed for the test case
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "institution": "CATZ",
            "email": "omer2@gmail.com",
            "subject": "Feline Behaviour"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "teacher exists"}


def test_missing_name():
    """Checks when one of the names is missing"""
    # Data needed for the test case
    data = {"first_name": "Mani",
            "city": "Al Haouz",
            "email": "omer2@gmail.rk",
            "institution": "CATZ",
            "subject": "Feline Behaviour",
            "password": 12345}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing last_name"}


def test_missing_name2():
    """Checks when one of the names is missing"""
    # Data needed for the test case
    data = {"last_name": "Mani",
            "city": "Al Haouz",
            "email": "omer2@gmail.rk",
            "institution": "CATZ",
            "subject": "Feline Behaviour",
            "password": 12345}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing first_name"}


def test_missing_password():
    """Checks when password is missing"""
    # Data needed for the test case
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "email": "omer2@gmail.wo",
            "institution": "CATZ",
            "subject": "Feline Behaviour"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing password"}


def test_create_found_institute():
    """Checks when creating in an existing institute"""
    # Data needed for the test case
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "email": "omer2@gmail.wrk",
            "institution": "Black Cat",
            "subject": "Feline Behaviiour",
            "password": "temp"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
                      print(marko.status_code)


def test_reAdd():
    """Checks when you re-add the same state again"""
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "email": "omer2@gmail.wrk",
            "institution": "Black Cat",
            "subject": "Feline Behaviiour",
            "password": "temp"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
