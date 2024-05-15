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
from datetime import datetime
import requests as req
# aliasing requests to req
import uuid


base = "http://54.157.156.176/"
toTest = "cities"
link = base + toTest
timeFormat = "%Y-%m-%dT%H:%M:%S.%f"


# Tests HTTP GET all
def test_endpoint_running():
    """Checks if the api is started"""
    with req.get(link) as marko:
        polo = marko.status_code
        assert polo == 200


def test_return_type():
    """Checks the return value of the endpoint"""
    with req.get(link) as marko:
        polo = marko.headers["content-type"]
        assert polo == "application/json"


def test_json_and_list():
    """Checks if the endpoint returned the correct data types"""
    with req.get(link) as marko:
        polo = marko.json()
        assert isinstance(polo, list)
        for elem in polo:
            assert isinstance(elem, dict)


def test_class_addherence():
    """Checks if all the data is from the same class"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "City"


def test_values_availability():
    """Checks if all values are present in classes"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] is not None
            assert elem["created_at"] is not None
            assert elem["id"] is not None
            assert elem["name"] is not None
            assert elem["updated_at"] is not None
            assert elem["state_id"] is not None


def test_correct_value_type_in_return():
    """
    Checks if all the values in class is valid and from the correct data type
    """
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert uuid.UUID(str(elem["id"]))
            assert uuid.UUID(str(elem["state_id"]))
            assert datetime.strptime(elem["updated_at"], timeFormat)
            assert datetime.strptime(elem["created_at"], timeFormat)
            assert isinstance(elem["__class__"], str)
            assert isinstance(elem["name"], str)


def test_getting_one_city():
    """Checks when we pick a city"""
    with req.get(link) as marko:
        polo = marko.json()
        # Selecting the last city
        got = polo[-1]
        # Saving the ID of the selected city
        slct = polo[-1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        # Saving the resulting ID to assert it
        chkSlct = polo["id"]
        assert chkSlct == slct
        assert polo == got


def test_getting_the_correct_class():
    """Checks if the class of the reuturn"""
    with req.get(link) as marko:
        polo = marko.json()
        # Selecting the first city
        slct = polo[1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        assert polo["__class__"] == "City"

def test_getting_not_city():
    """Checks what happens if the ID is wrong"""
    with req.get(link + "/temp") as marko:
        assert marko.status_code == 400


def test_getting_not_city_response():
    """Checks the response when ID is wrong"""
    with req.get(link + "/temp") as marko:
        polo = marko.json()
        assert polo == {"error": "UNKNOWN CITY"}


def test_state_relationship():
    """Checks if a city is from on of the states"""
    with req.get(base + "states") as marko:
        polo = marko.json()
        # List of states IDs
        state = []
        for elem in polo:
            state.append(elem["id"])
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["state_id"] in state


def test_intitutes_in_city():
    """Checks the institute filter by city"""
    # ID randomly checked from the database
    testID = "024fa7fa-20f0-4c64-8394-684809648ff9"
    newLink = link + "/" + testID + "/institutions"
    with req.get(link + "/" + testID) as marko:
        polo = marko.json()
        # Saving the name to check
        chkName = polo["name"]
    with req.get(newLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Institution"
            assert elem["city"] == chkName
            assert elem["city_id"] == testID


def test_state_of_this_city():
    """
    Checks the city state relationship.
    based upon api of the same file, line 101
    """
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            # Saving the ID
            chkID = elem["id"]
            # Saving the state ID
            chkState = elem["state_id"]
            with req.get(link + "/" + chkID + "/state") as marko2:
                polo2 = marko2.json()
                assert polo2["__class__"] == "State"
                assert polo2["id"] == chkState
