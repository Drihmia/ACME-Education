#!/usr/bin/python3
"""Define the Subjects API"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage


@app_views.route("/subjects", methods=["GET"], strict_slashes=False)
@app_views.route("/subjects/<id>", methods=["GET"], strict_slashes=False)
def allSubs(id=None):
    """
    GET: Return the list of avaiable subjects if there is not ID.
         Or the list with the specified ID.
    """
    from models.subject import Subject
    subjects = storage.all(Subject)
    if id is None:
        subjects_dict = []
        for subject in subjects.values():
            subject_temp = subject.to_dict()
            subjects_dict.append(subject_temp)
        return jsonify([subject_dict for subject_dict in subjects_dict]), 200

    subject = storage.get(Subject, id)
    if not subject:
        abort(404)

    return jsonify(subject.to_dict()), 200


@app_views.route("/subjects/<id>/institutions", methods=["GET"],
                 strict_slashes=False)
def subject_institutions(id):
    """
    GET: Lists all the subjects tought in a particular institute.
    """
    if request.method == 'GET':
        from models.subject import Subject

        subject = storage.get(Subject, id)
        if not subject:
            abort(404)
        institutions = [institution.to_dict() for institution in
                        subject.institutions]

        return jsonify(institutions), 200


@app_views.route("/subjects/<id>/lessons", methods=["GET"],
                 strict_slashes=False)
def subject_lessons(id):
    """
    GET: List of all lessons that belong this particular subject
    """

    if request.method == 'GET':
        from models.subject import Subject

        subject = storage.get(Subject, id)
        if not subject:
            abort(404)
        lessons = [lesson.to_dict() for lesson in subject.lessons]

        return jsonify(lessons), 200


@app_views.route("/subjects/<id>/teachers", methods=["GET"],
                 strict_slashes=False)
def subject_teachers(id):
    """
    GET: List of all teachers that teach this particular subject
    """
    if request.method == 'GET':
        from models.subject import Subject

        subject = storage.get(Subject, id)
        if not subject:
            abort(404)
        teachers = [teacher.to_dict() for teacher in subject.teachers]

        return jsonify(teachers), 200
