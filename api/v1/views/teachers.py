#!/usr/bin/python3
"""This module contains teacher'S IP"""
from flask import abort, jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from models.teacher import Teacher
from models.institution import Institution
from models.city import City
from models import storage


@app_views.route('/teachers', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/teachers/<id>', methods=["GET", 'PUT', 'DELETE'],
                 strict_slashes=False)
def teachers_list(id=None):
    """
    Get: return teacher object by id if provided otherwise a
    full list of all teachers objects.
    POST: Create a new teacher
        MUST: give the institution_id
            or institution_name + city_name/city_id.
        data = {first_name, last_name, email, password,
        institution_id}

        data = {first_name, last_name, email, password,
        institution_id, institutions: list}
        data = {first_name, last_name, email, password, city_id, institution}

        the 1st syntax is faster
    """

    if request.method == 'GET':
        if id:
            teacher = storage.get(Teacher, id)
            if not teacher:
                abort(404)
            return jsonify(teacher.to_dict()), 200
        teachers_list = [teacher.to_dict() for teacher in
                         storage.all(Teacher).values()]
        return jsonify(teachers_list), 200

    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 400

        if 'first_name' not in data.keys():
            return jsonify({'error': 'Missing first_name'}), 400

        if 'last_name' not in data.keys():
            return jsonify({'error': 'Missing last_name'}), 400

        if 'email' not in data.keys():
            return jsonify({'error': 'Missing email'}), 400

        if 'password' not in data.keys():
            return jsonify({'error': 'Missing password'}), 400

        # Check if institution already exist, 1st by its id if it's provided
        # +or by its name.
        # If the institution object is not found, we create new one bound to
        # +state_id provided
        if 'institution_id' in data.keys():
            institution = storage.get(Institution, data.get('institution_id'))
            if not institution:
                return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
        elif 'institution' in data.keys():
            institution_name = data.get('institution')
            if 'city' in data.keys():
                city_name = data.get('city')
                institution = storage.query(Institution).filter(
                    Institution.name == institution_name,
                    Institution.city == city_name).first()
                # if not institution:
                # return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
            elif 'city_id' in data.keys():
                city_id = data.get('city_id')
                institution = storage.query(Institution).filter(
                    Institution.name == institution_name,
                    Institution.city_id == city_id).first()
                # if not institution:
                # return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
            else:
                return jsonify({'error': "Missin city_id: provide city_id or\
                                city's name + institution_id"}), 400

            # If no institution exist with that name, create new one.
            if not institution:
                if 'city_id' not in data.keys():
                    return jsonify({
                        'error': "Missin city_id: provide city_id or\
                        city's name + institution_id"}), 400
                city = storage.get(City, data.get('city_id'))
                city_name = city.name
                if not city:
                    return jsonify({'error': "UNKNOWN CITY"}), 400

                # Creation new institution
                institution = Institution(name=institution_name,
                                          city_id=city.id,
                                          city=city.name)
        else:
            return jsonify({'error': "provide city's info, name or id"}), 400

        teacher = Teacher(first_name=data.get('first_name'),
                          last_name=data.get('last_name'),
                          email=data.get('email'),
                          password=data.get('password'),
                          institution=institution.name,
                          city=institution.cities.name)
        institution.teachers.append(teacher)

        # asseign all optionnal institutions to teacher's object.
        # If institution does not exist, it will be ignored
        if 'institutions' in data.keys():
            institutions = data.get('institutions')
            for institution_key in institutions:
                institution_optional = storage.get(Institution,
                                                   institution_key)
                if institution_optional:
                    institution_optional.teachers.append(teacher)
                    try:
                        institution_optional.save()
                    except IntegrityError:
                        pass
        try:
            storage.new(teacher)
            institution.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400
        return jsonify(teacher.to_dict()), 201

    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 400

        teacher = storage.get(Teacher, id)
        if not teacher:
            return jsonify({'error': "UNKNOWN TEACHER"}), 400

        ignore = ['id', 'created_at', 'updated_at', 'email']

        for k, v in data.items():
            if k not in ignore:
                setattr(teacher, k, v)
        teacher.save()
        return jsonify(teacher.to_dict()), 200

    if request.method == 'DELETE':
        teacher = storage.get(Teacher, id)
        if not teacher:
            return jsonify({'error': "UNKNOWN TEACHER"}), 400

        teacher.delete()
        storage.save()
        return jsonify({}), 200


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
        abort(404)

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

    return jsonify([institution.to_dict() for institution in
                    institutions]), 200


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
