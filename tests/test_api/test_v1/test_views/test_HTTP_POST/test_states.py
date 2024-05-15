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
import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "states"
# The information for the new institute that will be created
tempData = {"name": "Cats Den"}
# Headers needed by the application
head = {"Content-Type": "application/json"}
link = base + toTest


# Getting the count of institutes before creating a new one
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


def test_other_data_passed():
    """Checks when other info is sent"""
    # Data needed for testing the case
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.json() == {"error": "Missing name"}
        assert marko.status_code == 400


def test_correct_data():
    """Checks when everything is in order"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 201
        assert marko.json()["name"] == tempData["name"]
        # Saving the ID of the newly created object
        tempID = marko.json()["id"]
    # Formulating a link using it
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["name"] == tempData["name"]


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
