#!/usr/bin/python3
""" This module contains helper functions for creating lessons routes """

from models.lesson import Lesson
from models.subject import Subject
from sqlalchemy.exc import IntegrityError


def missing_arg_create_lessons(data: dict) -> str | None:
    """
    This function takes a dictionary as an argument and checks if the dictionary has the following keys:
    - name
    - download_link
    - subject_id
    - teacher_id
    If any of the keys is missing, it returns an error message.
    """

    if 'name' not in data.keys():
        return 'Missing name'
    if 'download_link' not in data.keys():
        return 'Missing download_link'
    if 'subject_id' not in data.keys():
        return 'Missing subject_id'
    if 'teacher_id' not in data.keys():
        return 'Missing teacher_id'
    return None


def create_lesson(data: dict, teacher_id, teacher_fullname, storage) -> Lesson | str:
    """
    This function takes a dictionary as an argument and creates a new lesson object.
    Args:
    - data: A dictionary containing the following keys:
        - name: The lesson's name as string.
        - download_link: The lesson's download link as string.
        - subject_id: The lesson's subject id as string uuid.
        - description: The lesson's description as string.
        - public: The lesson's public status, True if public, False if private.
    - teacher_id: The teacher's id as string uuid.
    - teacher_fullname: The teacher's fullname as string.
    - storage: An instance of the storage class.

    """

    # Getting attribute's values.
    name = data.get('name', '').strip()
    download_link = data.get('download_link', '').strip()
    subject_id = data.get('subject_id', '').strip()

    # Check if description's attribute is provided.
    description = data.get('description', 'Null').strip()

    # Check if public's attribute is provided.
    public = data.get('public', True)

    subject_obj = storage.get(Subject, subject_id)
    if not subject_obj:
        return 'UNKNOWN SUBJECT'

    lesson = Lesson(name=name, download_link=download_link,  # A must
                    subject_id=subject_id, teacher_id=teacher_id,
                    description=description, public=public,  # Option.
                    subject=subject_obj.name,
                    teacher=teacher_fullname)

    return lesson


def handle_integrity_error_saving_lesson(error: IntegrityError) -> str:
    """
    This function takes an IntegrityError object as an argument and handles the error.
    Args:
    - f: An IntegrityError object.
    """

    error_str = str(error)

    if 'Duplicate' in error_str:
        return 'lesson exists'

    must_ids = ['teacher_id', 'subject_id']
    for s_id in must_ids:
        if s_id in error_str[:error_str.find('REFERENCES')]:
            return f'unknown: {s_id}'

    return 'lesson exists'
