import requests as req
import json
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "cities"
link = base + toTest
tempData = {"name": "temp4",
            "state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 400
            assert marko.json() == {"error": "UNKNOWN CITY"}


def test_no_data():
    """Checks with when no data is sent"""
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}


def test_correct_ID_no_name():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_correct_ID_no_id():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"name": "Cat"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}


def test_correct_data():
    """Checks when everything is in order"""
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=json.dumps(tempData),
                 headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["name"] == "temp4"
        print(marko.json())


def test_no_json():
    """Checks when the request body is not a JSON"""
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}


def test_ineditable_data():
    """checks when trying to edit ineditable data"""
    testLink = link + "/000b2973-1388-4642-893f-3ff9b2c08922"
    data = {"updated_at": "2024-05-30T23:23:35.000000"}
    with req.put(testLink, data=json.dumps(data)) as marko:
        polo = marko.json()
        assert marko.status_code == 400
        assert polo == {"error": "Not a JSON"}
