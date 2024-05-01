import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "states"
link = base + toTest


def test_fake_ID():
    """Checks when passing a wrong ID"""
    with req.delete(link + "/temp") as marko:
        assert marko.status_code == 404
        assert marko.json() == {"error": "Not found"}


def test_correct_input():
    """Checks when everything is in order"""
    testID = "/0aafb626-9874-4299-adee-b9e303a28e38"
    with req.get(link) as marko:
        count = len(marko.json())
    with req.delete(link + testID) as marko:
        assert marko.status_code == 200
        assert marko.json() == {}
    with req.get(link) as marko:
        test = len(marko.json())
        assert count == test - 1
