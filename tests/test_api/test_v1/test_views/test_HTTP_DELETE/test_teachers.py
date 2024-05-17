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
    # Chosen ID from databases referring the one generated from HTTP POST test
    testID = "/01a066ed-b31d-45d8-9468-e19c3418ee45"
    with req.get(link) as marko:
        count = len(marko.json())
    with req.delete(link + testID) as marko:
        assert marko.status_code == 200
        assert marko.json() == {}
    with req.get(link) as marko:
        test = len(marko.json())
        assert count == test - 1
