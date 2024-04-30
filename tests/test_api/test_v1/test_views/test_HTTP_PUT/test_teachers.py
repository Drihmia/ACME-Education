import requests as req
import json
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "teachers"
link = base + toTest
tempData = {"first_name": "Black",
            "last_name": "Cat",
            "institution": "",
            "city": "Al Haouz",
            "subject": "Feline Behaviour"}
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 400
            assert marko.json() == {"error": "UNKNOWN TEACHER"}
            print(marko.status_code)
            print(marko.json())


def test_no_data():
    """Checks with when no data is sent"""
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}
        print(marko.status_code)
        print(marko.json())


def test_one_data_at_a_time():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    data = {"first_name": tempData["first_name"]}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.json()["first_name"] == tempData["first_name"]
        print(marko.json())


def test_one_data_at_a_time2():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    data = {"last_name": tempData["last_name"]}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.json()["last_name"] == tempData["last_name"]
        print(marko.json())


def test_ineditable_data():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    data = {"email": "Black@Cat.temp"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.json()["email"] == "omer2@gmail.com"
        assert marko.status_code == 200
        print(marko.json())


def test_correct_data():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    after = {
    "__class__": "Teacher",
    "email": "omer2@gmail.com",
    "first_name": "Black",
    "id": "7b932940-d6c4-4b4a-8b14-9606c91c82f3",
    "institution": "",
    "last_name": "Cat",
    "subject": "Feline Behaviour",
    }
    with req.put(testLink, data=json.dumps(tempData),
             headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["id"] == after["id"]
        assert marko.json()["__class__"] == after["__class__"]
        assert marko.json()["email"] == after["email"]
        assert marko.json()["institution"] == after["institution"]
        assert marko.json()["last_name"] == after["last_name"]
        assert marko.json()["subject"] == after["subject"]


def test_no_json():
    """Checks when the request body is not a JSON"""
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}
        print(marko.json())


def test_ineditable_data():
    """checks when trying to edit ineditable data"""
    testLink = link + "/7b932940-d6c4-4b4a-8b14-9606c91c82f3"
    data = {"updated_at": "2024-05-30T23:23:35.000000"}
    with req.put(testLink, data=json.dumps(data)) as marko:
        polo = marko.json()
        assert marko.status_code == 400
        assert polo == {"error": "Not a JSON"}
