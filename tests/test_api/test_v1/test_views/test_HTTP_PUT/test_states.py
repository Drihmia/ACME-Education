import requests as req
import json
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "states"
link = base + toTest
tempData = {"name": "Cat State"}
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 404
            print(marko.status_code)
            print(marko.json())


def test_no_data():
    """Checks with when no data is sent"""
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}
        print(marko.status_code)
        print(marko.json())


def test_correct_ID_no_name():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    data = {"name": ""}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}
        print(marko.json())


def test_correct_data():
    """Checks when everything is in order"""
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=json.dumps(tempData),
                 headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["name"] == "Cat State"
        print(marko.json())


def test_no_json():
    """Checks when the request body is not a JSON"""
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}
        print(marko.json())


def test_ineditable_data():
    """checks when trying to edit ineditable data"""
    testLink = link + "/3467008c-627b-4ae3-80a9-0a085c0628f6"
    data = {"updated_at": "2024-05-30T23:23:35.000000"}
    with req.put(testLink, data=json.dumps(data)) as marko:
        polo = marko.json()
        assert marko.status_code == 400
        assert polo == {"error": "Not a JSON"}
