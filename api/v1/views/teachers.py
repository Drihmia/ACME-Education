#!/usr/bin/python3
"""This module contains teacher'S IP"""
from flask import jsonify, request
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from models.teacher import Teacher
from models.institution import Institution
from models.city import City
from models.clas import Clas
from models.subject import Subject
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

        - example 1:
        data = {first_name, last_name, email, password, confirm_password
        institution_id}

        - example 2:
        data = {first_name, last_name, email, password, confirm_password
        city_id, institution}

        the 1st syntax is faster

    PUT: Update first_name, last_name, password, institutions, city, subjects,
            classes.

        - example:
        data = {first_name, last_name, password, city,
        institutions_id: list of ids,
        subjects_id: list of ids,
        classes_id: list of ids}

        all those attributes are optional.
    """
    # GET's method *******************************************************
    if request.method == 'GET':
        if id:
            teacher = storage.get(Teacher, id)
            if not teacher:
                return jsonify({'error': "UNKNOWN TEACHER"}), 403
            return jsonify(teacher.to_dict()), 200
        teachers_list = [teacher.to_dict() for teacher in
                         storage.all(Teacher).values()]
        return jsonify(teachers_list), 200

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

        # Check if the teacher's email not in our database.
        if storage.query(Teacher).filter(Teacher.email == data.
                                         get('email').strip()).first():
            return jsonify({'error': "teacher exists"}), 400

        # -------------------------------------------------------

        if 'first_name' not in data.keys():
            return jsonify({'error': 'Missing first_name'}), 400

        if 'last_name' not in data.keys():
            return jsonify({'error': 'Missing last_name'}), 400

        if 'password' not in data.keys():
            return jsonify({'error': 'Missing password'}), 400

        if 'confirm_password' in data.keys():
            if data.get('confirm_password'.strip()) != data.get(
                    'password'.strip()):
                return jsonify({'error': 'password do not match'}), 400
            else:
                del data['confirm_password']

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
                # if not institution:
                # return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
            elif 'city_id' in data.keys():
                city_id = data.get('city_id').strip()
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
                city = storage.get(City, data.get('city_id').strip())
                if not city:
                    return jsonify({'error': "UNKNOWN CITY"}), 400
                city_name = city.name

                # Creation new institution
                institution = Institution(name=institution_name,
                                          city_id=city.id,
                                          city=city.name)

        else:
            return jsonify({'error': "provide institution's info, name or id"}), 400

        teacher = Teacher(first_name=data.get('first_name').strip(),
                          last_name=data.get('last_name').strip(),
                          email=data.get('email').strip(),
                          password=data.get('password').strip(),
                          institution=institution.name,
                          city=institution.city)
        institution.teachers.append(teacher)

        try:
            institution.save()
        except IntegrityError:
            return jsonify({'error': 'institution exists'}), 400

        try:
            storage.new(teacher)
            storage.save()
        except IntegrityError:
            return jsonify({'error': 'teacher exists'}), 400

        return jsonify(teacher.to_dict()), 201

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

        teacher = storage.get(Teacher, id)
        if not teacher:
            return jsonify({'error': "UNKNOWN TEACHER"}), 400

        tech_dict = teacher.to_dict()
        normal_attr = ['first_name', 'last_name', 'password', 'institution',
                       'city', 'subject']

        for k, v in data.items():
            if k in normal_attr:
                # Accept only attr that already part of object
                # +and ignore 0 length values.
                if v == tech_dict.get(k, "Not Found") or not len(v):
                    continue
                setattr(teacher, k.strip(), v.strip())

        # assign all optional subjects to teacher's object.
        # If subject does not exist, it will be ignored
        if 'subjects_id' in data.keys():
            subjects_id = data.get('subjects_id').strip()

            # Make sure that subjects_id is an actual list.
            if not isinstance(subjects_id, list):
                return jsonify({'error': "subjects_id must be a list"}), 400

            # Making sure there's no duplicates.
            subjects_id = list(set(subjects_id))

            # List of subjects IDs already associated with the teacher.
            teacher_subject_ids = [s.id for s in teacher.subjects]

            for subject_id in subjects_id:
                # Ignore subject that are already associated to this teacher.
                # Avoid duplications
                if subject_id in teacher_subject_ids:
                    continue

                subject_optional = storage.get(Subject,
                                               subject_id)
                if subject_optional:
                    try:
                        subject_optional.teachers.append(teacher)
                        subject_optional.save()
                    except IntegrityError:
                        # If teacher already had that subject.
                        pass

                    # Update student's subjects automatically
                    # +as he add new teacher.
                    for student in teacher.students:
                        if subject_optional not in student.subjects:
                            subject_optional.students.append(student)
                            try:
                                subject_optional.save()
                            except IntegrityError:
                                storage.rollback()

        # assign all optional institutions to teacher's object.
        # If institution does not exist, it will be ignored
        if 'institutions_id' in data.keys():
            institutions = data.get('institutions_id').strip()

            # Make sure that institutions is an actual list.
            if not isinstance(institutions, list):
                return jsonify({'error': "institutions must be a list"}), 400

            # Making sure there's no duplicates.
            institutions = list(set(institutions))

            # List of institutions ID already associated with the teacher.
            teacher_institution_ids = [i.id for i in teacher.institutions]

            for institution_id in institutions:
                # Ignore institution t'are already associated to this teacher.
                # Avoid duplications
                if institution_id in teacher_institution_ids:
                    continue

                institution_optional = storage.get(Institution,
                                                   institution_id)
                if institution_optional:
                    try:
                        institution_optional.teachers.append(teacher)
                        institution_optional.save()
                    except IntegrityError:
                        # If teacher already had that institution.
                        pass

        # assign all optional classes to teacher's object.
        # If class does not exist, it will be ignored
        if 'classes_id' in data.keys():
            classes = data.get('classes_id').strip()

            # Make sure that classes is an actual list.
            if not isinstance(classes, list):
                return jsonify({'error': "classes must be a list"}), 400

            # Making sure there's no duplicates.
            classes = list(set(classes))

            # List of classes ID already associated with the teacher.
            teacher_class_ids = [c.id for c in teacher.classes]

            for class_id in classes:
                # Ignore class that are already associated to this teacher.
                # Avoid duplications
                if class_id in teacher_class_ids:
                    continue

                class_optional = storage.get(Clas,
                                             class_id)
                if class_optional:
                    try:
                        class_optional.teachers.append(teacher)
                        class_optional.save()
                    except IntegrityError:
                        # If teacher already had that class.
                        pass
        teacher.save()
        return jsonify(teacher.to_dict()), 200

    # DELETE's method *******************************************************
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
    # lessons = storage.query(Teacher).filter(Teacher.id == id).
    # all()[-1].lessons

    # Match faster if the maching is faster and less overload on database.
    teacher = storage.get(Teacher, id)
    if not teacher:
        return jsonify({'error': "UNKNOWN TEACHER"}), 403

    lessons = teacher.lessons
    return jsonify([lesson.to_dict() for lesson in lessons]), 200


@app_views.route('/teachers/<id>/subjects',  methods=['GET'],
                 strict_slashes=False)
def teachers_list_subject(id):
    """return a list of all subjects by teacher"""

    teacher = storage.get(Teacher, id)
    if not teacher:
        return jsonify({'error': "UNKNOWN TEACHER"}), 403

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
        return jsonify({'error': "UNKNOWN TEACHER"}), 403

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
        return jsonify({'error': "UNKNOWN TEACHER"}), 403

    classes = teacher.classes

    # two differente approach using query methode from storage.
    # teacher = storage.query(Teacher).filter(Teacher.id == id).all()
    # lessons = storage.query(Subject).filter(Subject.subject_id == id).all()

    return jsonify([classe.to_dict() for classe in classes]), 200
