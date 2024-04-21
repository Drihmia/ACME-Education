#!/usr/bin/python3
"""This module contains teacher'S IP"""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models.teacher import Teacher
from models.lesson import Lesson
from models.subject import Subject
from models import storage


@app_views.route('/teachers', methods=['GET'], strict_slashes=False)
@app_views.route('/teachers/<id>', methods=['GET'], strict_slashes=False)
def teachers_list(id=None):
    """Get teacher object by id if provided otherwise a
    full list of all teachers"""

    if id:
        teacher = storage.get(Teacher, id)
        if not teacher:
            raise abort(404)
        return jsonify(teacher.to_dict()), 200
    teachers_list = [teacher.to_dict() for teacher in
                     storage.all(Teacher).values()]
    return jsonify(teachers_list), 200


@app_views.route('/teachers/<id>/lessons',  methods=['GET'],
                 strict_slashes=False)
def teachers_list_lessons(id):
    """return a list of all  lessons by teacher"""

    # lessons = storage.query(Lesson).filter(Lesson.teacher_id == id).all()
    lessons = storage.query(Teacher).filter(Teacher.id == id).all()[-1].lessons

    return jsonify([lesson.to_dict() for lesson in lessons]), 200


@app_views.route('/teachers/<id>/subjects',  methods=['GET'],
                 strict_slashes=False)
def teachers_list_subject(id):
    """return a list of all subjects by teacher"""

    teacher = storage.get(Teacher, id)
    if not teacher:
        raise abort(404)

    subjects = teacher.subjects

    # two differente approach using query methode from storage.
    # teacher = storage.query(Teacher).filter(Teacher.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify([subject.to_dict() for subject in subjects]), 200


@app_views.route('/teachers/<id>/institutions',  methods=['GET'],
                 strict_slashes=False)
def teachers_list_institution(id):
    """return a list of all institutions by teacher"""

    teacher = storage.get(Teacher, id)
    if not teacher:
        raise abort(404)

    institutions = teacher.institutions

    # two differente approach using query methode from storage.
    # teacher = storage.query(Teacher).filter(Teacher.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify([institution.to_dict() for institution in institutions]), 200


@app_views.route('/teachers/<id>/classes',  methods=['GET'],
                 strict_slashes=False)
def teachers_list_class(id):
    """return a list of all classes by teacher"""

    teacher = storage.get(Teacher, id)
    if not teacher:
        raise abort(404)

    classes = teacher.classes

    # two differente approach using query methode from storage.
    # teacher = storage.query(Teacher).filter(Teacher.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify([classe.to_dict() for classe in classes]), 200
