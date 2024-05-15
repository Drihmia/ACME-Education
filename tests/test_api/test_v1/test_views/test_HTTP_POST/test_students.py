#!/usr/bin/python3
import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "students"
tempData = {"first_name": "Catz",
            "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"
            }
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


def test_other_data_passed():
    """Checks when other info is sent"""
    data = {"__class__": "cat"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing email"}
        print(marko.status_code)
        print(marko.json())


def test_no_email():
    """Checks when emial is missing"""
    data = {"first_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing email"}


def test_new_student_repeated_email():
    """Checks when emial is used by another student"""
    data = {"first_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage", 
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
            "email": "hicham@gmail.com"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 700
        assert marko.json() == {"error": "student exists"}


def test_teacher_email():
    """Checks when emial of student is the same as of a teacher"""
    data = {"first_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5",
            "email": "red1@gmail.com"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 409
        assert marko.json() == {"error": "red1@gmail.com is already "
                                         "registered as a teacher"}


def test_missting_one_name():
    """Checks when on of the names is missing"""
    data = {"fir_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "email": "temp",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing first_name"}


def test_missting_one_name2():
    """Checks when on of the names is missing"""
    data = {"first_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "las_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "email": "temp",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing last_name"}


def test_no_password():
    """Checks when no password is passed"""
    data = {"first_name": "Catz",
            "institution_id": "00005709-9ad5-48e7-bcb0-c1b10ea02654",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing password"}


def test_password_missMatch():
    """Checks when retyping the password goes wrong"""
    data = {"first_name": "Catz",
            "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "password": "Mirage",
            "confirm_password": "Mrage",
            "teacher_email": "red1@gmail.com",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "password do not match"}


def test_no_class_ID():
    """Checks when no class ID is passed"""
    data = {"first_name": "Catz",
            "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "Missing class_id"}


def test_no_institute_info():
    """Checks when all data about institute is missing"""
    data = {"first_name": "Catz",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "gender": "M",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"}
    with req.post(link, data=json.dumps(data),
                  headers=head) as marko:
        print(marko.status_code)
        print(marko.json())
        assert marko.status_code == 400
        assert marko.json() == {"error": "provide institution's info"
                                         ", name or id"}


def test_correct_data():
    """Checks when everything is in order"""
    tempData = {"first_name": "Catz",
                "institution_id": "1df2f1a4-19df-4015-8d42-7cbc686d1d19",
                "email": "temp1@tempEmail.com",
                "last_name": "Dean",
                "teacher_email": "red1@gmail.com",
                "password": "Mirage",
                "confirm_password": "Mirage",
                "class_id": "7f1ff24a-e07d-4e96-81b1-9dcf9613000f"
                }
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 201
        assert marko.json()["first_name"] == tempData["first_name"]
        tempID = marko.json()["id"]
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["first_name"] == tempData["first_name"]
    with req.get(link) as marko:
        new = len(marko.json())
        assert new == count + 1


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
