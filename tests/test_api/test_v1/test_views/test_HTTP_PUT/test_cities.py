#!/usr/bin/python3
"""
Test casses for the cities API. It cover for approx. all sensitive cases.

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
import requests as req
import json
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "cities"
link = base + toTest
# Data to edit the object with
tempData = {"name": "temp4",
            "state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
# Headers needed so the application accept changes
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 400
            assert marko.json() == {"error": "UNKNOWN CITY"}


def test_no_data():
    """Checks with when no data is sent"""
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}


def test_correct_ID_no_name():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_correct_ID_no_id():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"name": "Cat"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}


def test_correct_data():
    """Checks when everything is in order"""
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=json.dumps(tempData),
                 headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["name"] == "temp4"


def test_no_json():
    """Checks when the request body is not a JSON"""
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}


def test_ineditable_data():
    """checks when trying to edit ineditable data"""
    # ID chosen for the POST method
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"updated_at": "2024-05-30T23:23:35.000000"}
    with req.put(testLink, data=json.dumps(data)) as marko:
        polo = marko.json()
        assert marko.status_code == 400
        assert polo == {"error": "Not a JSON"}
