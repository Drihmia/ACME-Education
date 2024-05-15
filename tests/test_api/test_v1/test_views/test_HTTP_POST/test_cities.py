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
import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "cities"
# The information for the new city that will be created
tempData = {"name": "Cat  Vills",
            "state_id": "aa44e339-77ca-4532-b169-2fab14b9a133"}
# Headers needed by the application
head = {"Content-Type": "application/json"}
link = base + toTest


# Getting the count of cities before creating a new one
with req.get(link) as marko:
    count = len(marko.json())


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


def test_no_name():
    """Checks when the name is missing"""
    # Data needed for testing the case
    data = {"state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_no_state():
    """Checks when the state ID is missing"""
    # Data needed for testing the case
    data = {"name": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}


def test_other_data_passed():
    """Checks when other info is sent"""
    # Data needed for testing the case
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.json() == {"error": "Missing name"}


def test_correct_data():
    """Checks when everything is in order"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 201
        assert marko.json()["name"] == tempData["name"]
        assert marko.json()["state_id"] == tempData["state_id"]
    with req.get(link) as marko:
        new = len(marko.json())
        assert count == new + 1


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
