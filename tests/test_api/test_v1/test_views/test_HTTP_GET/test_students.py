from datetime import datetime
import requests as req
# aliasing requests to req
import uuid


base = "http://54.157.156.176/"
toTest = "students"
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
           cls = elem["__class__"]
           assert cls == "Student"


def test_values_availability():
    """Checks if all values are present in classes"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert elem["__class__"] is not None
            assert elem["created_at"] is not None
            assert elem["id"] is not None
            assert elem["updated_at"] is not None
            assert elem["class_id"] is not None
            assert elem["email"] is not None
            assert elem["first_name"] is not None
            assert elem["institution_id"] is not None
            assert elem["last_name"] is not None
            assert elem["teacher_email"] is not None


def test_correct_value_type_in_return():
    """
    Checks if all the values in class is valid and from the correct data type
    """
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            assert uuid.UUID(str(elem["id"]))
            assert uuid.UUID(str(elem["class_id"]))
            assert isinstance(elem["email"], str)
            assert uuid.UUID(str(elem["institution_id"]))
            assert isinstance(elem["last_name"], str)
            assert isinstance(elem["teacher_email"], str)
            assert datetime.strptime(elem["updated_at"], timeFormat)
            assert datetime.strptime(elem["created_at"], timeFormat)
            assert isinstance(elem["__class__"], str)


def test_getting_one_student():
    """Checks when we pick a student"""
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
        assert cls == "Student"

def test_getting_not_atudent():
    """Checks what happens if the ID is wrong"""
    with req.get(link + "/temp") as marko:
        assert marko.status_code == 404


def test_institutions_of_student():
    """Checks filter for institutes of a student"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            chkID = elem["id"]
            testLink = link + "/" + chkID + "/institutions"
            with req.get(testLink) as marko2:
             polo2 = marko.json()
             for elem2 in polo2:
                assert elem2["__class__"] == "Institution"


def test_year_of_student():
    """Checks filter for year of a student"""
    with req.get(link) as marko:
        polo = marko.json()
        for elem in polo:
            chkID = elem["id"]
            testLink = link + "/" + chkID + "/classes"
            with req.get(testLink) as marko2:
                polo2 = marko2.json()
                assert polo2["__class__"] == "Clas"
