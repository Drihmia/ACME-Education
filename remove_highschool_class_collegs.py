#!/usr/bin/python3
"""
This script remove college classes from colleges.
"""
from models import storage
from models.institution import Institution

list_lycee_classes_id = [
    '06b1a0ef-eac4-4c81-9e4f-cce0d4c0d61d',
    '708e7f5b-1fc7-425b-a7e3-39182b802c9c',
    '7ac039d6-de06-474a-96d6-b3ad661c1d2f',
    '7f4a08e6-b343-4ea1-9b26-15512d092527',
    '839f3cf8-cdb0-4027-b0c6-f4740c83c651',
    '9331ddff-2af3-45ff-99ab-cb976c93ef6f',
    '983bd731-54b8-49ca-be8c-65562d33422d',
    '9f12a794-8cb5-440c-af94-bbda2bf3d5c6',
    'b4197d9c-1420-4820-9779-4f224c873345',
]

def get_colleges():
    """
    Get colleges from DataBase.
    """

    Colleges = storage.query(Institution).filter(Institution.name.like('%COLLEGE%')).all()
    return Colleges

def remove_classes_from_school(schools: list):
    """
    remove the classes from the school.
    """

    print('Number of colleges:', len(schools))

    for school in schools:
        print('+' * 100)
        print('+' * 40, school.name, '+' * 40)
        print('+' * 100)
        for cl in school.classes:
            if  cl.id in list_lycee_classes_id:
                print('Removing class:', cl.name, 'from school:', school.name)
                cl.institutions.remove(school)
                school.classes.remove(cl)
                cl.save()
                school.save()


def remove_college_classes_from_high_schools():
    """
    Remove college classes from colleges.
    """

    colleges = get_colleges()


    remove_classes_from_school(colleges)


if __name__ == '__main__':
    remove_college_classes_from_high_schools()

