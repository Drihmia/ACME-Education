import json
import requests as req
# Aliasing requests to req
# Need to add data for that

base = "http://54.157.156.176/"
toTest = "teachers"
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
        print(marko.json())


def test_correct_data():
    """Checks when everything is in order"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 201
        assert marko.json()["name"] == tempData["name"]
        tempID = marko.json()["id"]
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["name"] == tempData["name"]
    with req.get(link) as marko:
        new = len(marko.json())
        assert count == new + 1


def test_missing_email():
    """Checks when email is missing"""
    data = {"first_name": "Mani",
            "last_name": "Cat",
            "city": "Al Haouz",
            "institution": "CATZ",
            "subject": "Feline Behaviour"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing email"}
        print(marko.json())


def test_email_exists():
    """Checks when email is repeated"""
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
        print(marko.json())


def test_missing_name():
    """Checks when one of the names is missing"""
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
        print(marko.json())


def test_missing_name2():
    """Checks when one of the names is missing"""
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
        print(marko.json())


def test_missing_password():
    """Checks when password is missing"""
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
        print(marko.json())


def test_create_found_institute():
    """Checks when creating in an existing institute"""
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
        print(marko.json())
