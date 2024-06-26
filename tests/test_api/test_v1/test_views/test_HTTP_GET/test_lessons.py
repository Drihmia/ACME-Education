#!/usr/bin/python3
"""
Test casses for the lessons API. It cover for approx. all sensitive cases.

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
toTest = "lessons"
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
    """Checks if the endpoint returned the correct types"""
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
           assert elem["__class__"] == "Lesson"


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
            assert elem["description"] is not None
            assert elem["download_link"] is not None
            assert elem["subject_id"] is not None
            assert elem["teacher_id"] is not None


def test_correct_value_type_in_return():
    """
    Checks if all the values in class is valid and from the correct data type
    """
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert uuid.UUID(str(elem["id"]))
            assert datetime.strptime(elem["updated_at"], timeFormat)
            assert datetime.strptime(elem["created_at"], timeFormat)
            assert isinstance(elem["__class__"], str)
            assert isinstance(elem["name"], str)
            assert uuid.UUID(str(elem["subject_id"]))
            assert uuid.UUID(str(elem["teacher_id"]))
            assert isinstance(elem["download_link"], str)
            assert isinstance(elem["description"], str)



def test_getting_one_lesson():
    """Checks when we pick a lesson"""
    with req.get(link) as marko:
        polo = marko.json()
        # Saving the last lesson
        got = polo[-1]
        # Saving its ID
        slct = polo[-1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        # Saving the resulting ID from the branch crawl
        chkSlct = polo["id"]
        assert chkSlct == slct
        assert polo == got


def test_getting_the_correct_class():
    """Checks if the class of the reuturn"""
    with req.get(link) as marko:
        polo = marko.json()
        # Saving the first lesson's ID
        slct = polo[1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        assert polo["__class__"] == "Lesson"

def test_getting_not_lesson():
    """Checks what happens if the ID is wrong"""
    with req.get(link + "/temp") as marko:
        assert marko.status_code == 400


def test_relationships():
    """
    Checks if institute is from a
    teacher, institute and subject in the database
    """
    with req.get(base + "teachers") as marko:
        polo = marko.json()
        # List to hold teachers IDs
        teach = []
        for elem in polo:
            teach.append(elem["id"])
    with req.get(base + "subjects") as marko:
        polo = marko.json()
        # List to hold subjects IDs
        subj = []
    for elem in polo:
        subj.append(elem["id"])
    with req.get(base + "institutions") as marko:
        polo = marko.json()
        # List to hold institutes IDs
        inst = []
        for elem in polo:
            inst.append(elem["id"])
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["subject_id"] in subj
