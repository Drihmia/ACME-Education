#!/usr/bin/python3
"""
Test casses for the students API. It cover for approx. all sensitive cases.

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
import json
import requests as req
# Aliasing requests to req

base = "http://54.157.156.176/"
toTest = "students"
# The information for the new institute that will be created
tempData = {"first_name": "Catz",
            "institution_id": "27e99d13-0dae-4c2a-b180-864a5af7a4e6",
            "email": "temp@tempEmail.com",
            "last_name": "Dean",
            "teacher_email": "red1@gmail.com",
            "password": "Mirage",
            "confirm_password": "Mirage",
            "class_id": "fde4ee7c-7b59-4d0a-bd35-95e5e14a2ee5"
            }
# Headers needed by the application
head = {"Content-Type": "application/json"}
link = base + toTest


# Getting the count of institutes before creating a new one
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


def test_no_email():
    """Checks when emial is missing"""
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
    # Data needed for testing the case
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
        assert marko.status_code == 400
        assert marko.json() == {"error": "provide institution's info"
                                         ", name or id"}


def test_correct_data():
    """Checks when everything is in order"""
    # Data needed for testing the case
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
        # Saving the ID of the newly created object
        tempID = marko.json()["id"]
    # Formulating a link using it
    testLink = link + "/" + tempID
    with req.get(testLink) as marko:
        assert marko.json()["first_name"] == tempData["first_name"]
    with req.get(link) as marko:
        # Getting count after creation
        new = len(marko.json())
        assert new == count + 1


def test_reAdd():
    """Checks when you re-add the same state again"""
    with req.post(link, data=json.dumps(tempData),
                  headers=head) as marko:
        assert marko.status_code == 400
        assert marko.json() == {"error": "exists"}
