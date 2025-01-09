#!/usr/bin/python3
"""
This script remove college classes from High schools.
"""
from json import load
from sqlalchemy.exc import IntegrityError
from models import storage
from models.institution import Institution

list_college_classes_id = [
    '856b49c0-3e9a-42df-b814-ff9aba0d1e19',
    'c5d0a01b-4e1e-4064-a52c-a816e9277038',
    'ef6fba67-8f06-43ad-b85e-5858ff3e2595',
]

def get_lycees():
    """
    Get High schools from DataBase.
    """

    Lycees = storage.query(Institution).filter(Institution.name.like('Lycee%')).all()
    return Lycees

def remove_classes_from_school(schools: list):
    """
    remove the classes from the school.
    """

    print('Number of high schools:', len(schools))

    for school in schools:
        for cl in school.classes:
            if  cl.id in list_college_classes_id:
                print('Removing class:', cl.name, 'from school:', school.name)
                cl.institutions.remove(school)
                school.classes.remove(cl)
                cl.save()
                school.save()


def remove_college_classes_from_high_schools():
    """
    Remove cllege classes from High schools.
    """

    lycees = get_lycees()


    remove_classes_from_school(lycees)


if __name__ == '__main__':
    remove_college_classes_from_high_schools()

