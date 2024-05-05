#!/usr/bin/python3
"""This module contains student'S IP"""
from flask import jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from models.city import City
from models.clas import Clas
from models.institution import Institution
from models.student import Student
from models.subject import Subject
from models.teacher import Teacher
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
        - example 1:
        data = {first_name, last_name, email, password, confirm_password
        teacher_email, class_id, institution_id}

        - example 2:
        data = {first_name, last_name, email, password, confirm_password
        teacher_email, class_id, city_id, institution}

        - example 2:
        data = {first_name, last_name, email, password, confirm_password
        teacher_email, class_id, city, institution}

        the 1st example is faster

    PUT: Update first_name, last_name, password, and list of  email teachers

        data = {'first_name', 'last_name', 'password',
                'teachers_email': list of email}

        all those attributes are optional.
    """

    # GET's method *******************************************************
    if request.method == 'GET':
        if id:
            student = storage.get(Student, id)
            if not student:
                return jsonify({'error': "UNKNOWN STUDENT"}), 403
            return jsonify(student.to_dict()), 200
        students_list = [student.to_dict() for student in
                         storage.all(Student).values()]
        return jsonify(students_list), 200

    # POST's method *******************************************************
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 422

        if 'email' not in data.keys():
            return jsonify({'error': 'Missing email'}), 400

        # -----------------------------------------------------------------
        # Check if the student's email not in our database.
        if storage.query(Student).filter(Student.email == data.
                                         get('email').strip()).first():
            return jsonify({'error': "student exists"}), 700

        # -----------------------------------------------------------------

        # Check if the student's email not in our database as a Teacher.
        email = data.get('email').strip()
        if storage.query(Teacher).filter(Teacher.email == email).first():
            return jsonify(
                {'error':
                 f"{email} is already registered as a teacher"}), 409

        # -----------------------------------------------------------------

        if 'first_name' not in data.keys():
            return jsonify({'error': 'Missing first_name'}), 400

        if 'last_name' not in data.keys():
            return jsonify({'error': 'Missing last_name'}), 400

        if 'password' not in data.keys():
            return jsonify({'error': 'Missing password'}), 400

        if 'confirm_password' in data.keys():
            if data.get('confirm_password').strip() != data.get(
                    'password').strip():
                return jsonify({'error': 'password do not match'}), 400
            else:
                del data['confirm_password']
        else:
            return jsonify({'error': 'Missing confirm_password'}), 400

        if 'class_id' not in data.keys():
            return jsonify({'error': 'Missing class_id'}), 400

        # Check if institution already exist, 1st by its id if it's provided
        # +or by its name.
        # If the institution object is not found, we create new one bound to
        # +state_id provided
        if 'institution_id' in data.keys():
            institution = storage.get(Institution, data.get(
                'institution_id').strip())
            if not institution:
                return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
        elif 'institution' in data.keys():
            institution_name = data.get('institution').strip()
            if 'city' in data.keys():
                city_name = data.get('city').strip()
                institution = storage.query(Institution).filter(
                    Institution.name == institution_name,
                    Institution.city == city_name).first()

            elif 'city_id' in data.keys():
                city_id = data.get('city_id').strip()
                institution = storage.query(Institution).filter(
                    Institution.name == institution_name,
                    Institution.city_id == city_id).first()
            else:
                return jsonify({'error': "Provide 'institution' name \
with 'city' name or 'city_id', or you can provide the 'institution_id'"}), 400

            # If no institution exist with that name, create new one.
            # I'm supposing the city already exist.
            if not institution:
                if 'city_id' not in data.keys():
                    return jsonify({
                        'error': "UNKNOWN INSTITUTION, \
create new institution: provide 'city_id' and 'institution' name"}), 400
                city = storage.get(City, data.get('city_id').strip())
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

        # This one item is not a list of items, should be institution.city.
        if institution.cities:
            city_name = institution.cities.name
        elif 'city' in data.keys():
            city_name = data.get('city').strip()
        else:
            city_name = 'Null'

        # assign teacher to student, if student provide an valid teacher_email.
        if 'teacher_email' in data.keys():
            teacher = storage.query(Teacher).filter(Teacher.email == data.
                                                    get("teacher_email")
                                                    ).first()
            if teacher:
                teacher_email = teacher.email
            else:
                teacher_email = 'Null'
        else:
            teacher = None
            teacher_email = 'Null'

        # Adding gender.
        if 'gender' in data.keys():
            gender = data.get('gender').strip()
        else:
            gender = 'N'

        if 'phone_number' in data.keys():
            phone_number = data.get('phone_number')
        else:
            phone_number = 'Null'

        try:
            student = Student(first_name=data.get('first_name'),
                              last_name=data.get('last_name'),
                              email=data.get('email'),
                              password=data.get('password'),
                              class_id=data.get('class_id'),
                              institution_id=institution.id,
                              institution=institution.name,
                              teacher_email=teacher_email,
                              city=city_name,
                              gender=gender,
                              phone_number=phone_number)

            storage.new(student)

            # institution.students.append(student)
            # update student's relations
            if teacher:
                student.lessons.extend(teacher.lessons)

                for subject in teacher.subjects:
                    subject.students.append(student)
                    try:
                        subject.save()
                    except IntegrityError:
                        storage.rollback()

                teacher.students.append(student)
                try:
                    teacher.save()
                except IntegrityError:
                    storage.rollback()

        except IntegrityError:
            # storage.rollback()
            return jsonify({'error': 'exists'}), 400

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
            if teacher:
                teacher.save()
        except IntegrityError:
            return jsonify({'error': 'exists'}), 400

        student = student.to_dict()
        if 'institutions' in student:
            del student['institutions']
        return jsonify(student), 201

    # PUT's method *******************************************************
    if request.method == 'PUT':
        if not request.is_json:
            return jsonify({'error': 'Not a JSON'}), 400

        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Not a JSON'}), 400

        if not data:
            return jsonify({'error': 'No data'}), 422

        if 'password' in data.keys() and 'confirm_password' in data.keys():
            if data.get('confirm_password').strip() != data.get(
                    'password').strip():
                return jsonify({'error': 'password do not match'}), 400
            else:
                del data['confirm_password']

        student = storage.get(Student, id)
        if not student:
            return jsonify({'error': "UNKNOWN STUDENT"}), 400

        student_dict = student.to_dict()
        normal_attr = ['first_name', 'last_name', 'password', 'institution',
                       'city', 'phone_number', 'gender', 'teacher_email']

        for k, v in data.items():
            if k in normal_attr:
                # Accept only attr that already part of object
                # +and ignore 0 length values
                if v == student_dict.get(k, "Not Found") or not len(v):
                    continue
                if k == 'gender' and len(v) != 1:
                    return jsonify({'error': 'gender must be M/F'}), 400
                setattr(student, k.strip(), v.strip())

        if 'teachers_email' in data.keys():
            teachers_email = data.get('teachers_email').strip()

            # Make sure that teachers_email is an actual list.
            if not isinstance(teachers_email, list):
                return jsonify({'error': "teachers_email must be a list \
of teacher's IDs"}), 400

            # Making sure there's no duplicates.
            teachers_email = list(set(teachers_email))

            # List of teacher IDs already associated with the student.
            student_teacher_ids = [t.id for t in student.teachers]

            for teacher_email in teachers_email:
                teacher = storage.query(Teacher).filter(
                    Teacher.email == teacher_email).first()
                # I'm not sure which policy  I should adopte,
                # +forgiven or strict.
                # I chose to be strict.
                if not teacher:
                    # If techer object with one of the teacher's emails
                    # +provided not in our database or it's misspelled
                    # all the list will be rejected.
                    return jsonify({
                        'error': f'UNKNOWN TEACHER with {teacher_email}'}), 400

                if teacher.id in student_teacher_ids:
                    continue

                # Add a teacher to the student's list of teachers.
                teacher.students.append(student)

                # Append new subjects/lessons related to new teacher to
                # +student.
                # and avoid duplications
                st_sub = set(student.subjects + teacher.subjects)
                student.subjects.extend(st_sub)

                # Making sure that student get assigned only lessons of
                # +the classes he studies in.
                teacher_lessons = [lesson for lesson in teacher.lessons
                                   if lesson.classes.id in
                                   [c.id for c in student.classes] and
                                   lesson.institutions.id ==
                                   student.institutions.id]
                st_lessons = set(student.lessons + teacher_lessons)
                student.lessons.extend(st_lessons)

        student.save()
        student = student.to_dict()

        if 'subjects' in student:
            del student['subjects']

        if 'lessons' in student:
            del student['lessons']

        if 'teachers' in student:
            del student['teachers']

        return jsonify(student.to_dict()), 200

    # DELETE's method *******************************************************
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
        return jsonify({'error': "UNKNOWN STUDENT"}), 403

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
        return jsonify({'error': "UNKNOWN STUDENT"}), 403

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
        return jsonify({'error': "UNKNOWN STUDENT"}), 403

    classes = student.classes

    # two differente approach using query methode from storage.
    # student = storage.query(Student).filter(Student.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify(classes.to_dict()), 200
