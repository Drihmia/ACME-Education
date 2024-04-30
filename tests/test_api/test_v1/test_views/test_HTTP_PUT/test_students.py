import requests as req
import json
# Aliasing requests to req

# No data, maybe after HTTP POST
base = "http://54.157.156.176/"
toTest = "institutions"
link = base + toTest
tempData = {"name": "Black Cat",
            "city_id": "a51ec686-4ee4-4c1a-82cd-09543a123467",
            "city": "Al Haouz"}
head = {"Content-Type": "application/json"}


def test_wrong_id():
    """Checks what happens when wrong id is passed"""
    with req.put(link + "/temp", data=json.dumps(tempData),
                 headers=head) as marko:
            assert marko.status_code == 400
            assert marko.json() == {"error": "UNKNOWN INSTITUTION"}
            #print(marko.status_code)
            #print(marko.json())


def test_no_data():
    """Checks with when no data is sent"""
    testLink = link + "/0001aef5-af10-4d78-8755-ffc6cf3369f2"
    with req.put(testLink, data=json.dumps({}),
                 headers=head) as marko:
        assert marko.status_code == 422
        assert marko.json() == {"error": "No data"}
        #print(marko.status_code)
        #print(marko.json())


def test_correct_ID_no_name():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/0001aef5-af10-4d78-8755-ffc6cf3369f2"
    data = {"state_id": "5e21a8d6-a018-4e09-8243-f0228ecb86b9"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing name"}


def test_correct_ID_no_id():
    """Checks when no name is sent with a correct ID"""
    # We need some change on that
    testLink = link + "/0001aef5-af10-4d78-8755-ffc6cf3369f2"
    data = {"name": "Cat"}
    with req.put(testLink, data=json.dumps(data),
             headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing state_id"}


def test_correct_data():
    """Checks when everything is in order"""
    testLink = link + "/0001aef5-af10-4d78-8755-ffc6cf3369f2"
    with req.put(testLink, data=json.dumps(tempData),
                 headers=head) as marko:
        assert marko.status_code == 200
        assert marko.json()["name"] == "Black Cat"
        print(marko.json())


def test_no_json():
    """Checks when the request body is not a JSON"""
    testLink = link + "/0001aef5-af10-4d78-8755-ffc6cf3369f2"
    with req.put(testLink, data=tempData,
                 headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Not a JSON"}
        print(marko.json())
