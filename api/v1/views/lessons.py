#!/usr/bin/python3
"""Define the Lessons API"""
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request
import uuid
from werkzeug.exceptions import BadRequest
from api.v1.views import app_views
from models import storage
from models.clas import Clas
from models.institution import Institution
from models.lesson import Lesson
from models.teacher import Teacher
from models.subject import Subject


@app_views.route("/lessons", methods=["GET", "POST"],
                 strict_slashes=False)
@app_views.route("/lessons/<id>", methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def lessons(id=None):
    """
    GET: Return the list of avaiable lessons if there is not ID.
         Or the list with the specified ID.
    POST: Create new lesson.
         * A teacher can chose an insitution and/or a class,
         therefor the lesson will be assigned to that institution and that
         class, also to all his students in that institution from that class.

         * Otherwise the lesson will be affected to all his students regardless
         of thier original institution/class.

         Note: Student won't be assigned to a lesson from outside of its
         class or list of its subjects.

        - example 1:
        data = {'name', 'download_link', 'description', 'public',
        'subject_id', 'teacher_id', 'class_id**', 'institution_id**'}

        - example 2:
        data = {'name', 'download_link', 'description', 'public',
        'subject_id', 'teacher_id'}

        ** optional parametres.

    PUT: Update only normal attributes
        data = {'name', 'download_link', 'description', 'public'}

    """

    # GET's method *******************************************************
    if request.method == 'GET':
        less = storage.all(Lesson)
        if id is None:
            data = []
            for elem in less.values():
                temp = elem.to_dict()
                data.append(temp)
            return jsonify(data), 200
        else:
            seek = "Lesson." + id
            try:
                data = less[seek].to_dict()
                return jsonify(data), 200
            except KeyError:
                return jsonify({"error": "UNKNOWN LESSON"}), 404

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

        #                ///////\\\\\\\\\\
        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        #                ///////\\\\\\\\\\
        if 'download_link' not in data.keys():
            return jsonify({'error': 'Missing download_link'}), 400

        #                ///////\\\\\\\\\\
        if 'subject_id' not in data.keys():
            return jsonify({'error': 'Missing subject_id'}), 400

        #                ///////\\\\\\\\\\
        if 'teacher_id' not in data.keys():
            return jsonify({'error': 'Missing teacher_id'}), 400

        # ---------  Check if the user is a teacher.  -------------
        # ---------------------------------------------------------
        teacher_id = data.get('teacher_id').strip()
        # I'm calling teacher's object for accessing
        # +the list of its students.
        teacher = storage.get(Teacher, teacher_id)
        if not teacher:
            return jsonify({'error': "UNKNOWN TEACHER"}), 403
        teacher_fullname = teacher.first_name + ' ' + teacher.last_name.upper()

        subject_id = data.get('subject_id').strip()
        teacher_subject_ids = [sub.id for sub in teacher.subjects if sub]
        if subject_id not in teacher_subject_ids:
            return jsonify({
                'error': 'The subject is outside your area of expertise.'
            }), 400

        # ****************** This is ignored for the moment *************
        # ***************************************************************
        if 'institutions_id' in data.keys():
            return jsonify({
                'error': "institutions_id is being ignored for MVP"}), 400
        """
        # Make sure institutions_id is a list.
            institutions_id = data.get('institutions_id')
            if not isinstance(institutions_id, list):
                return jsonify({'error': "institutions_id must be a list"}),
                400

            # Making sure there's no duplicates, remove empty or spaced
            entries.
            institutions_id = list(set(s.strip()
                                       for s in institutions_id if
                                       is_valid_uuid(s.strip())))

            if not len(institutions_id):
                return jsonify(
                    {'error': "No institutions's id has been provided"}), 400
            must = ['name', 'download_link', 'subject_id', 'teacher_id']
            for k, v in data.items():
                if k in must and not isinstance(v, str):
                    return jsonify({'error': f'{k} is not a string'}), 400
        """
        # ***************************************************************
        # ***************************************************************

        # Getting attribute's value.
        name = data.get('name').strip()
        download_link = data.get('download_link').strip()
        subject_id = data.get('subject_id').strip()

        subject_obj = storage.get(Subject, subject_id)
        if not subject_obj:
            return jsonify({'error': 'UNKNOWN SUBJECT'}), 400

        # Check if description's attribute is provided.
        if 'description' in data.keys():
            description = data.get('description').strip()
        else:
            description = 'Null'

        # Check if public's attribute is provided.
        if 'public' in data.keys():
            public = data.get('public')
        else:
            public = True

        try:
            lesson = Lesson(name=name, download_link=download_link,  # A must
                            subject_id=subject_id, teacher_id=teacher_id,
                            description=description, public=public,  # Option.
                            subject=subject_obj.name,
                            teacher=teacher_fullname)
        except IntegrityError:
            storage.rollback()
            return jsonify({'error': 'lesson exists'}), 400

        try:
            storage.new(lesson)
            storage.save()
        except IntegrityError as f:
            storage.rollback()
            f = str(f)

            if 'Duplicate' in f:
                return jsonify({'error': 'lesson exists'}), 400
            must_ids = ['teacher_id', 'subject_id']
            for s_id in must_ids:
                if s_id in f[:f.find('REFERENCES')]:
                    return jsonify({'error': f'unknown: {s_id}'}), 400

            return jsonify({'error': 'lesson exists'}), 400

        # ****************** This is ignored for the moment ************
        # **************************************************************
        # Looping trough list of institution's id to make many to many
        # +relationship between lesson and given institutions.
        """
        for inst_id in institutions_id:
            institution = storage.query(Institution).filter(
                Institution.id == inst_id).first()
            if institution:
                try:
                    # Making sure that lesson does not already exist in this
                    # +particular institution's relationship.
                    if institution.lessons:
                        # Avoid duplicates.
                        inst_less_list = set(institution.lessons + [lesson])
                    else:
                        inst_less_list = [lesson]

                    institution.lessons = (inst_less_list)
                    institution.save()
                    # The lessen get related to at least one institution.
                    witness = 1
                except IntegrityError as e:
                    storage.rollback()
        if not witness:
            lesson.delete()
            storage.save()
            return jsonify({'error': 'No institution has been regonized'}), 400
        """
        # *************************************************************
        # *************************************************************

        # ---------------------------------------------------------
        if 'institution_id' in data.keys() and \
                is_valid_uuid(data.get('institution_id')):
            institution_id = data.get('institution_id').strip()
            institution = storage.get(Institution, institution_id)
            if not institution:
                return jsonify({'error': "UNKNOWN INSTITUTION"}), 400
            institutions = [institution]
        else:
            institutions = teacher.institutions

        # Associate lesson to its institution.
        for institution in institutions:
            institution.lessons.append(lesson)

            try:
                institution.save()
            except IntegrityError:
                storage.rollback()

        # ---------------------------------------------------------
        if 'class_id' in data.keys() and \
                is_valid_uuid(data.get('class_id')):
            class_id = data.get('class_id').strip()
            clas = storage.get(Clas, class_id)
            if not clas:
                return jsonify({'error': "UNKNOWN CLASS"}), 400
            setattr(lesson, 'class_alias', clas.alias)
            classes = [clas]
        else:
            classes = teacher.classes

        # Associate lesson to its clas.
        for clas in classes:
            clas.lessons.append(lesson)

            try:
                clas.save()
            except IntegrityError:
                storage.rollback()

        # Assign lesson to all teacher's student that belong to the classes
        # +subjects and institutions chosen by the teacher.
        for student in teacher.students:

            if not student.institutions:
                continue

            teacher_institutions_ids = [i.id for i in institutions if i]

            # Student has only 1 institution, please mind the 's'.
            if student.institutions.id not in teacher_institutions_ids:
                continue

#             teacher_classes_ids = [c.id for c in classes if c]
            # if student_id not in teacher_classes_ids:
                # continue
            student.lessons.append(lesson)
            try:
                student.save()
            except IntegrityError:
                storage.rollback()

        # save lesson
        try:
            lesson.save()
        except IntegrityError:
            storage.rollback()

        lesson = lesson.to_dict()

        # Remove all list of objects assigned to this lesson
        # +by many to many or one to many or many to one relationship.
        if 'classes' in lesson:
            del lesson['classes']

        if 'subjects' in lesson:
            del lesson['subjects']

        if 'students' in lesson:
            del lesson['students']

        if 'teachers' in lesson:
            del lesson['teachers']

        if 'institutions' in lesson:
            del lesson['institutions']

        return jsonify(lesson), 201

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

        lesson = storage.get(Lesson, id)
        if not lesson:
            return jsonify({'error': "UNKNOWN LESSON"}), 400

        lesson_dict = lesson.to_dict()
        normal_attr = ['name', 'download_link', 'description', 'public']

        for k, v in data.items():
            if k in normal_attr:
                # Accept only normal attributes and ignore 0 length values
                if isinstance(v, bool):
                    setattr(lesson, k.strip(), v)
                    continue
                if v == lesson_dict.get(k) or not len(v):
                    continue
                setattr(lesson, k.strip(), v.strip())

        lesson.save()

        lesson = lesson.to_dict()
        # Remove all list of objects assigned to this lesson
        # +by many to many or one to many or many to one relationship.
        if 'classes' in lesson:
            del lesson['classes']

        if 'subjects' in lesson:
            del lesson['subjects']

        if 'students' in lesson:
            del lesson['students']

        if 'teachers' in lesson:
            del lesson['teachers']

        if 'institutions' in lesson:
            del lesson['institutions']

        return jsonify(lesson), 200

    # DELETE's method *******************************************************
    if request.method == 'DELETE':
        lesson = storage.get(Lesson, id)
        if not lesson:
            return jsonify({'error': "UNKNOWN LESSON"}), 400

        lesson.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route("/public_lessons", methods=["GET"],
                 strict_slashes=False)
def public_lessons():
    """return all public lessons"""
    lessons = storage.all(Lesson).values()

    public_lessons = [p_lesson.to_dict() for p_lesson in lessons
                      if p_lesson.public is True]

    return jsonify(public_lessons), 200


def is_valid_uuid(s):
    try:
        uuid_obj = uuid.UUID(s)
        # Check if the string representation matches the original string
        if str(uuid_obj) != s:
            print(f"{s} not a valid uuid")
            return False
        return True
    except ValueError:
        print(f"{s} not uuid string")
        return False
