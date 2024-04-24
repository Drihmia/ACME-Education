#!/usr/bin/python3
"""This module contains student'S IP"""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models.student import Student
from models.lesson import Lesson
from models.subject import Subject
from models import storage


@app_views.route('/students', methods=['GET'], strict_slashes=False)
@app_views.route('/students/<id>', methods=['GET'], strict_slashes=False)
def students_list(id=None):
    """Get student object by id if provided otherwise a
    full list of all students"""

    if id:
        student = storage.get(Student, id)
        if not student:
            raise abort(404)
        return jsonify(student.to_dict()), 200
    students_list = [student.to_dict() for student in
                     storage.all(Student).values()]
    return jsonify(students_list), 200


@app_views.route('/students/<id>/lessons',  methods=['GET'],
                 strict_slashes=False)
def students_list_lessons(id):
    """return a list of all  lessons by student"""

    # lessons = storage.query(Lesson).filter(Lesson.student_id == id).all()
    lessons = storage.query(Student).filter(Student.id == id).all()[-1].lessons

    return jsonify([lesson.to_dict() for lesson in lessons]), 200


@app_views.route('/students/<id>/subjects',  methods=['GET'],
                 strict_slashes=False)
def students_list_subject(id):
    """return a list of all subjects by student"""

    student = storage.get(Student, id)
    if not student:
        raise abort(404)

    subjects = student.subjects

    # two differente approach using query methode from storage.
    # student = storage.query(Student).filter(Student.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify([subject.to_dict() for subject in subjects]), 200


@app_views.route('/students/<id>/institutions',  methods=['GET'],
                 strict_slashes=False)
def students_list_institution(id):
    """return a list of all institutions by student"""

    student = storage.get(Student, id)
    if not student:
        raise abort(404)

    institutions = student.institutions

    # two differente approach using query methode from storage.
    # student = storage.query(Student).filter(Student.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify(institutions.to_dict()), 200


@app_views.route('/students/<id>/classes',  methods=['GET'],
                 strict_slashes=False)
def students_list_class(id):
    """return a list of all classes by student"""

    student = storage.get(Student, id)
    if not student:
        raise abort(404)

    classes = student.classes

    # two differente approach using query methode from storage.
    # student = storage.query(Student).filter(Student.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify(classes.to_dict()), 200
