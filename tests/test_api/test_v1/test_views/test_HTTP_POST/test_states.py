import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "states"
tempData = {"name": "Cats Den"}
head = {"Content-Type": "application/json"}
link = base + toTest


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
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        print(marko.status_code)
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


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
