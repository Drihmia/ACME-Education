#!/usr/bin/python3
"""
Test casses for the states API. It cover for approx. all sensitive cases.

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
toTest = "states"
link = base + toTest
# Data to change the object with
tempData = {"name": "Cat State"}
# Headers needed so the application accepts changes
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 404


def test_no_data():
    """Checks with when no data is sent"""
    # ID chosen from database resulting from the POST test
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}


def test_correct_ID_no_name():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    # ID chosen from database resulting from the POST test
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    # Data needed for the test case
    data = {"name": ""}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_correct_data():
    """Checks when everything is in order"""
    # ID chosen from database resulting from the POST test
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=json.dumps(tempData),
                 headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["name"] == "Cat State"


def test_no_json():
    """Checks when the request body is not a JSON"""
    # ID chosen from database resulting from the POST test
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}


def test_ineditable_data():
    """checks when trying to edit ineditable data"""
    # ID chosen from database resulting from the POST test
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    # Data needed for the test case
    data = {"updated_at": "2024-05-30T23:23:35.000000"}
    with req.put(testLink, data=json.dumps(data)) as marko:
        polo = marko.json()
        assert marko.status_code == 400
        assert polo == {"error": "Not a JSON"}
