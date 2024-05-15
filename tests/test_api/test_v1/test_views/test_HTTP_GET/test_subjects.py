#!/usr/bin/python3`
"""
Test casses for the subjects API. It cover for approx. all sensitive cases.

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
toTest = "subjects"
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
           assert elem["__class__"] == "Subject"


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


def test_getting_one_subject():
    """Checks when we pick a subject"""
    with req.get(link) as marko:
        polo = marko.json()
        # Saving the last subject
        got = polo[-1]
        # Saving its ID
        slct = polo[-1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        # Saving the branch crawl ID
        chkSlct = polo["id"]
        assert chkSlct == slct
        assert polo == got


def test_getting_the_correct_class():
    """Checks if the class of the reuturn"""
    with req.get(link) as marko:
        polo = marko.json()
        # Saving the first subject's ID
        slct = polo[1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        assert polo["__class__"] == "Subject"

def test_getting_not_subject():
    """Checks what happens if the ID is wrong"""
    with req.get(link + "/temp") as marko:
        assert marko.status_code == 400


def test_subject_of_institute():
    """Checks filter of institute by subject"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            # Saving the ID
            chkID = elem["id"]
            # Formulating a link based on it
            testLink = link + "/" + chkID + "/institutions"
            with req.get(testLink) as marko2:
                polo2 = marko2.json()
                for elem2 in polo2:
                    assert elem2["__class__"] == "Institution"


def test_subject_of_lessons():
    """Checks filter of institute by lessons"""
    # ID chosen form the database
    chkID = "7424627e-8f0d-4273-ad4e-b2e69215b526"
    # Formulating a link based on it
    testLink = link + "/" + chkID + "/lessons"
    with req.get(testLink) as marko2:
        polo2 = marko2.json()
        for elem2 in polo2:
            assert elem2["__class__"] == "Lesson"


def test_teacher_of_subject():
    """Checks filter of subject by teacher"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            # Saving the ID
            chkID = elem["id"]
            # Formulating a link based on it
            testLink = link + "/" + chkID + "/teachers"
            with req.get(testLink) as marko2:
                polo2 = marko2.json()
                for elem2 in polo2:
                    assert elem2["__class__"] == "Teacher"
