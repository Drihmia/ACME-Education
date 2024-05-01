import json
import requests as req
# Aliasing requests to req
# No data to delete whatsoever

base = "http://54.157.156.176/"
toTest = "teachers"
link = base + toTest


def test_fake_ID():
    """Checks when passing a wrong ID"""
    with req.delete(link + "/temp") as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "UNKNOWN TEACHER"}


def test_correct_input():
    """Checks when everything is in order"""
    testID = "/01a066ed-b31d-45d8-9468-e19c3418ee45"
    with req.get(link) as marko:
        count = len(marko.json())
    with req.delete(link + testID) as marko:
        assert marko.status_code == 200
        assert marko.json() == {}
    with req.get(link) as marko:
        test = len(marko.json())
        assert count == test - 1
