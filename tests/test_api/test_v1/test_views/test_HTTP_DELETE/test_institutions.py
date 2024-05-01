import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "institutions"
link = base + toTest


def test_fake_ID():
    """Checks when passing a wrong ID"""
    with req.delete(link + "/temp") as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "UNKNOWN INSTITUTION"}


def test_correct_input():
    """Checks when everything is in order"""
    testID = "/ab7bcc05-5b4d-45e7-b5a1-fb8d225deb69"
    with req.get(link) as marko:
        count = len(marko.json())
    with req.delete(link + testID) as marko:
        assert marko.status_code == 200
        assert marko.json() == {}
    with req.get(link) as marko:
        test = len(marko.json())
        assert count == test - 1
