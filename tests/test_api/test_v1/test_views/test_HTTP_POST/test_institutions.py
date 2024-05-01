import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "cities"
tempData = {"name": "Cat  Vills",
            "city": "Al Haouz",
            "city_id": "a51ec686-4ee4-4c1a-82cd-09543a123467"}
head = {"Content-Type": "application/json"}
link = base + toTest


with req.get(link) as marko:
    count = len(marko.json())


def test_data_not_JSON():
    """checks when data is not a proper JSON"""
    with req.post(link, data=tempData,
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}


def test_no_data():
    """Checks when no data is sent"""
    with req.post(link, data=json.dumps({}),
                  headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}


def test_no_name():
    """Checks when the name is missing"""
    data = {"city": "Al Haouz",
            "city_id": "a51ec686-4ee4-4c1a-82cd-09543a123467"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_no_city_name():
    """Checks when the city name is missing"""
    # Unexpectanly passing
    data = {"name": "Cat  Vills",
            "city_id": "a51ec686-4ee4-4c1a-82cd-09543a123467"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}
        print(marko.status_code)
        print(marko.json())


def test_missing_city_ID():
    """Checks when the city ID is missing"""
    # Unexpectanly passing
    data = {"name": "Cat  Vills",
            "city": "Al Haouz"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}
        print(marko.status_code)
        print(marko.json())


def test_only_name_passed():
    """Checks when only passing the name of institute"""
    # Not the expected
    data = {"name": "Cat  Vills"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "provide city's info, name or id"}
        print(marko.status_code)
        print(marko.json())


def test_other_data_passed():
    """Checks when other info is sent"""
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}
        print(marko.status_code)
        print(marko.json())


def test_correct_data():
    """Checks when everything is in order"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        print(marko.json())
        assert marko.status_code == 201
        assert marko.json()["name"] == tempData["name"]
        assert marko.json()["city_id"] == tempData["city_id"]
        tempID = marko.json()["id"]
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["name"] == tempData["name"]
        assert marko.json()["city_id"] == tempData["city_id"]
    with req.get(link) as marko:
        new = len(marko.json())
        assert count == new + 1


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
