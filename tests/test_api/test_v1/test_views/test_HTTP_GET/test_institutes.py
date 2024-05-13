#!/usr/bin/python3
from datetime import datetime
import requests as req
# aliasing requests to req
import uuid


base = "http://54.157.156.176/"
toTest = "institutions"
link = base + toTest
timeFormat = "%Y-%m-%dT%H:%M:%S.%f"
limit = 32
testID = ""


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
           cls = elem["__class__"]
           assert cls == "Institution"


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
            assert elem["city"] is not None
            assert elem["city_id"] is not None


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
            assert isinstance(elem["city"], str)
            assert uuid.UUID(str(elem["city_id"]))


def test_getting_one_institute():
    """Checks when we pick a institute"""
    with req.get(link) as marko:
        polo = marko.json()
        got = polo[-1]
        slct = polo[-1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        chkSlct = polo["id"]
        assert chkSlct == slct
        assert polo == got


def test_getting_the_correct_class():
    """Checks if the class of the reuturn"""
    with req.get(link) as marko:
        polo = marko.json()
        slct = polo[1]["id"]
    with req.get(link + "/" + slct) as marko:
        polo = marko.json()
        cls = polo["__class__"]
        assert cls == "Institution"

def test_getting_not_institute():
    """Checks what happens if the ID is wrong"""
    with req.get(link + "/temp") as marko:
        assert marko.status_code == 400


def test_relationships():
    """
    Checks if institute is from a state and city in the database
    """
    with req.get(base + "cities") as marko:
        polo = marko.json()
        city = []
        cityID = []
    for elem in polo:
        city.append(elem["name"])
        cityID.append(elem["id"]) 
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["city_id"] in cityID
            assert elem["city"] in city


def test_correct_relationship():
    """Check if the information is correct"""
    i = 0
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            if i != limit:
                cityID = elem["city_id"]
                with req.get(base + "/cities/" + cityID) as marko2:
                    polo2 = marko2.json()
                    assert polo2["id"] == cityID
                    i = i + 1
            else:
                break


def test_lesson_from_institute():
    """Checks the filter of lessons from the same institute"""
    testID = "d48256df-47f8-4c51-9e77-a380bbe208b8"
    testLink = link + "/" + testID + "/lessons"
    with req.get(testLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Lesson"
            assert elem["institution_id"] == testID


def test_teacher_by_institute():
    """Checks the teachers in same institute filter"""
    testID = "d48256df-47f8-4c51-9e77-a380bbe208b8"
    testLink = link + "/" + testID + "/teachers"
    with req.get(testLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Teacher"


def test_subjct_by_institute():
    """Checks the filter of subjects from the same institute"""
    testID = "d48256df-47f8-4c51-9e77-a380bbe208b8"
    testLink = link + "/" + testID + "/subjects"
    with req.get(testLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Subject"


def test_year_by_institute():
    """Checks the filter of years from the same institute"""
    testID = "d48256df-47f8-4c51-9e77-a380bbe208b8"
    testLink = link + "/" + testID + "/classes"
    with req.get(testLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Clas"


def test_student_by_institute():
    """Checks the filter of students from the same institute"""
    testID = "31975d9f-08a3-445b-88aa-fc01cd05d18c"
    testLink = link + "/" + testID + "/students"
    with req.get(testLink) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] == "Student"
            assert elem["institution_id"] == testID
