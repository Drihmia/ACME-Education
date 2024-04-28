#!/usr/bin/python3
"""This module contains student'S IP"""
from flask import abort, jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from models.student import Student
from models.teacher import Teacher
from models.institution import Institution
from models.city import City
from models.clas import Clas
from models.subject import Subject
from models import storage


@app_views.route('/students', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/students/<id>', methods=["GET", 'PUT', 'DELETE'],
                 strict_slashes=False)
def students_list(id=None):
    """Get student object by id if provided otherwise a
    full list of all students
    POST: Create a new student
        MUST: give the institution_id
            or institution_name + city_name/city_id.
        data = {first_name, last_name, email, password,
        teacher_email, class_id, institution_id}

        data = {first_name, last_name, email, password,
        teacher_email, class_id, city_id, institution}

        the 1st syntax is faster
    """

    # GET's method.
    if request.method == 'GET':
        if id:
            student = storage.get(Student, id)
            if not student:
                abort(404)
            return jsonify(student.to_dict()), 200
        students_list = [student.to_dict() for student in
                         storage.all(Student).values()]
        return jsonify(students_list), 200

    # POST's method.
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

        if 'class_id' not in data.keys():
            return jsonify({'error': 'Missing class_id'}), 400

        if 'teacher_email' not in data.keys():
            return jsonify({'error': "Missing teacher's email"}), 400

        # checking student's teacher exist in our database.
        teacher = storage.query(Teacher).filter(Teacher.email == data.
                                                get("teacher_email")).first()
        if not teacher:
            return jsonify({'error': "UNKNOWN TEACHER"}), 400

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
            # I'm supposing the city already exist.
            if not institution:
                if 'city_id' not in data.keys():
                    return jsonify({
                        'error': "incorrect city_id / city /\
                        institution: provide city_id or\
                        city's name + institution_id"}), 400
                city = storage.get(City, data.get('city_id'))
                if not city:
                    return jsonify({'error': "UNKNOWN CITY"}), 400

                # Creation new institution
                institution = Institution(name=institution_name,
                                          city_id=city.id,
                                          city=city.name)
        else:
            return jsonify({'error': "provide institution's info, name or id"
                            }), 400

        # Check if the class object exist.
        clas = storage.get(Clas, data.get('class_id'))
        if not clas:
            return jsonify({'error': "UNKNOWN CLASS"}), 400

        if institution.cities:
            city_name = institution.cities.name
        elif 'city' in data.keys():
            city_name = data.get('city')
        elif 'city_id' in data.keys():
            city_name = data.get('city_id')

        try:
            student = Student(first_name=data.get('first_name'),
                              last_name=data.get('last_name'),
                              email=data.get('email'),
                              password=data.get('password'),
                              class_id=data.get('class_id'),
                              institution_id=institution.id,
                              teacher_email=teacher.email,
                              city=city_name)
            institution.students.append(student)
            teacher.students.append(student)
        except IntegrityError:
            # storage.rollback()
            return jsonify({'error': 'exists'}), 400
        print("****************")
        for subject in storage.all(Subject).values():
            try:
                subject.students.append(student)
                storage.save()
                subject.save()
            except IntegrityError:
                pass
        try:
            storage.new(student)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400

        try:
            institution.save()
            teacher.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400

        student = student.to_dict()
        del student['institutions']
        return jsonify(student), 201

    # PUT's method.
    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 400

        student = storage.get(Student, id)
        if not student:
            return jsonify({'error': "UNKNOWN STUDENT"}), 400

        ignore = ['id', 'created_at', 'updated_at', 'email']

        for k, v in data.items():
            if k not in ignore:
                setattr(student, k, v)
        student.save()
        return jsonify(student.to_dict()), 200

    # DELETE's method.
    if request.method == 'DELETE':
        student = storage.get(Student, id)
        if not student:
            return jsonify({'error': "UNKNOWN STUDENT"}), 400

        student.delete()
        storage.save()
        return jsonify({}), 200


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
        abort(404)

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
        abort(404)

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
        abort(404)

    classes = student.classes

    # two differente approach using query methode from storage.
    # student = storage.query(Student).filter(Student.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify(classes.to_dict()), 200
