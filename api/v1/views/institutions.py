#!/usr/bin/python3
"""Define the Institutions API"""
from flask import abort, jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.institution import Institution
from models.city import City


@app_views.route("/institutions", methods=["GET", "POST"],
                 strict_slashes=False)
@app_views.route("/institutions/<id>", methods=["GET", 'PUT', 'DELETE'],
                 strict_slashes=False)
def institutions(id=None):
    """
    GET: Return the list of avaiable institutions.
         Or the a specific institution if ID has been provided.
    POST: Create new institutions
        MUST: provide a city_id
            or city's name + state_id.
    """

    if request.method == 'GET':
        if not id:
            institutions = storage.all(Institution)

            institutions_dict = [institution.to_dict() for institution in
                                 institutions.values()]

            return jsonify(institutions_dict), 200

        institution = storage.get(Institution, id)
        if not institution:
            abort(404)

        return jsonify(institution.to_dict()), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 400

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        # Check if city already exist, 1st by its id if it's provided
        # +or by its name.
        # If the city object is not found, we create new one bound to
        # +state_id provided
        if 'city_id' in data.keys():
            city = storage.get(City, data.get('city_id'))
            if not city:
                return jsonify({'error': "UNKNOWN CITY"}), 400
        # last resort, cities lists will be populated automatically using
        # +dataset from the internet,
        # +So city_id should be always provided.
        elif 'city' in data.keys():
            city_name = data.get('city')
            city = storage.query(City).filter(City.name == city_name).first()

            if not city:
                if 'state_id' not in data.keys():
                    return jsonify({
                        'error': "Missing state_id: provide city_id or city's\
                        name plus state_id"}), 400
                city = City(name=city_name, state_id=data.get('state_id'))
        else:
            return jsonify({'error': "provide city's info, name or id"}), 400

        institution = Institution(name=data.get('name'),
                                  city_id=city.id, city=city.name)
        # city.institutions.append(institution)
        # No need: Many to many relationship#s association
        try:
            storage.new(institution)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400

        return jsonify(institution.to_dict()), 201

    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 400

        institution = storage.get(Institution, id)
        if not institution:
            return jsonify({'error': "UNKNOWN INSTITUTION"}), 400

        ignore = ['id', 'created_at', 'updated_at']

        for k, v in data.items():
            if k not in ignore:
                setattr(institution, k, v)
        institution.save()
        return jsonify(institution.to_dict()), 200

    if request.method == 'DELETE':
        institution = storage.get(Institution, id)
        if not institution:
            return jsonify({'error': "UNKNOWN INSTITUTION"}), 400

        institution.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/institutions/<id>/lessons", methods=['GET'],
                 strict_slashes=False)
def institutions_lessons(id):

    """
    GET: return all lessons published by teachers works or has works
    in the institution by the specific ID
    """

    institution = storage.get(Institution, id)
    if not institution:
        abort(404, description="UNKNOWN INSTITUTION")

    lessons = institution.lessons

    lessons_dict = [lesson.to_dict() for lesson in lessons]
    return jsonify(lessons_dict), 200


@app_views.route("/institutions/<id>/teachers", methods=['GET'],
                 strict_slashes=False)
def institutions_teachers(id):
    """
    GET: return all teachers works or has works
    in the institution by the specific ID
    """

    institution = storage.get(Institution, id)
    if not institution:
        abort(404, description="UNKNOWN INSTITUTION")

    teachers = institution.teachers

    teachers_dict = [teacher.to_dict() for teacher in teachers]
    return jsonify(teachers_dict), 200


@app_views.route("/institutions/<id>/subjects", methods=['GET'],
                 strict_slashes=False)
def institutions_subjects(id):
    """
    GET: return all subjects works or has works
    in the institution by the specific ID
    """

    institution = storage.get(Institution, id)
    if not institution:
        abort(404, description="UNKNOWN INSTITUTION")

    subjects = institution.subjects

    subjects_dict = [subject.to_dict() for subject in subjects]
    return jsonify(subjects_dict), 200


@app_views.route("/institutions/<id>/classes", methods=['GET'],
                 strict_slashes=False)
def institutions_classes(id):
    """
    GET: return all classes taught in the institution by the specific ID
    """

    institution = storage.get(Institution, id)
    if not institution:
        abort(404, description="UNKNOWN INSTITUTION")

    classes = institution.classes

    classes_dict = [classe.to_dict() for classe in classes]
    return jsonify(classes_dict), 200


@app_views.route("/institutions/<id>/students", methods=['GET'],
                 strict_slashes=False)
def institutions_students(id):
    """
    GET: return all students that learn in the institution by the specific ID
    """

    institution = storage.get(Institution, id)
    if not institution:
        abort(404)

    students = institution.students

    students_dict = [student.to_dict() for student in students]
    return jsonify(students_dict), 200
