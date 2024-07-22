#!/usr/bin/python3
"""Define the Classes API"""
from flask import jsonify
from api.v1.views import app_views, role_required
from models import storage
from models.clas import Clas


@app_views.route("/classes", methods=["GET"], strict_slashes=False)
@app_views.route("/classes/<id>", methods=["GET"],
                 strict_slashes=False)
def classes(id=None):
    """
    GET: Return the list of all avaiable Classes, if not id is provided,
    otherwise return the spesific class to that id.
    """
    if not id:
        classes = storage.all(Clas)

        classes_dict = [clas.to_dict() for clas in classes.values()]
        return jsonify(classes_dict), 200

    clas = storage.get(Clas, id)
    if not clas:
        return jsonify({'error': "UNKNOWN CLASS"}), 400

    return jsonify(clas.to_dict()), 200


@app_views.route("/classes/<id>/students", methods=["GET"],
                 strict_slashes=False)
# Not used for now
@role_required(["dev"])
def classes_students(id=None):
    """
    GET: Return the list of all avaiable students of that class.
    """

    clas = storage.get(Clas, id)
    if not clas:
        return jsonify({'error': "UNKNOWN CLASS"}), 400

    students = clas.students
    students_dict = [student.to_dict() for student in students]
    return jsonify(students_dict), 200


@app_views.route("/classes/<id>/lessons", methods=["GET"],
                 strict_slashes=False)
# Not used for now
@role_required(["dev"])
def classes_lessons(id=None):
    """
    GET: Return the list of all avaiable lessons of that class.
    """

    clas = storage.get(Clas, id)
    if not clas:
        return jsonify({'error': "UNKNOWN CLASS"}), 400

    lessons = clas.lessons
    lessons_dict = [lesson.to_dict() for lesson in lessons]
    return jsonify(lessons_dict), 200


@app_views.route("/classes/<id>/teachers", methods=["GET"],
                 strict_slashes=False)
# Not used for now
@role_required(["dev"])
def classes_teachers(id=None):
    """
    GET: Return the list of all avaiable teachers of that class.
    """

    clas = storage.get(Clas, id)
    if not clas:
        return jsonify({'error': "UNKNOWN CLASS"}), 400

    teachers = clas.teachers
    teachers_dict = [teacher.to_dict() for teacher in teachers]
    return jsonify(teachers_dict), 200


@app_views.route("/classes/<id>/institutions", methods=["GET"],
                 strict_slashes=False)
# Not used for now
@role_required(["dev"])
def classes_institutions(id=None):
    """
    GET: Return the list of all avaiable institutions of that class.
    """

    clas = storage.get(Clas, id)
    if not clas:
        return jsonify({'error': "UNKNOWN CLASS"}), 400

    institutions = clas.institutions
    institutions_dict = [institution.to_dict() for institution in institutions]
    return jsonify(institutions_dict), 200
