#!/usr/bin/python3
"""
This model contains functions to assign lessons to teachers.
"""

def assign_private_lesson_to_student(lesson, student):

    """
    Assigns lessons to a student.
    Important Notes:
        - Assigned lessons is a list of lessons from the teacher's lessons.
        - Assigned lessons must have same institution as student.
        - Assigned lessons must have same class as the student.
        - Assigned lessons must have same subject as the student.
    """

    # Skip:
     # If students is institution-less.
     # If the lesson is public.
    if not student.institutions or lesson.public:

        return student

    # 1- Get list of lesson's institution's IDs.
    lesson_institutions_ids = {ins.id for ins in lesson.institutions}

    # Make sure that the student's institution is one of the lesson's institutions.
    if student.institutions.id not in lesson_institutions_ids:
        return student

    # 2- Get list of lesson's class IDs.
    lesson_classes_ids = {clas.id for clas in lesson.classes}

    # Make sure that the lesson's class is a class of the student.
    if student.classes.id not in lesson_classes_ids:
        return student

    # 3- Get list of student's subject IDs.
    student_subjects_ids = {subj.id for subj in student.subjects}

    # Make sure that the lesson's subject is a subject of the student.
    if lesson.subjects.id not in student_subjects_ids:
        return student

    # 4- Get list of student's teachers IDs.
    student_teachers_ids = {teach.id for teach in student.teachers}

    # Make sure that the lesson's author is a teacher of the student.
    if lesson.teachers.id not in student_teachers_ids:
        return student

    student.lessons.append(lesson)
    return student


def assign_public_lessons_student_creation(student):
    """
    assign public lessons to the recenlty created student,
    that have same institution as the lesson.
    """
    for lesson in student.institutions.lessons:
        # assign only public lessons to student.
        if lesson.public:
            student.lessons.append(lesson)


def assign_public_lesson_while_its_creation(lesson):

    """
    assign recenlty public lesson to all students of the same institutions
    as the lessons.
    """
    # If lesson is not public, return.
    if not lesson.public:
        return

    for institution in lesson.institutions:
        for student in institution.students:
            student.lessons.append(lesson)
            student.save()

