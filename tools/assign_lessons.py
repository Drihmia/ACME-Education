#!/usr/bin/python3
"""
This model contains functions to assign lessons to teachers.
"""

def assign_private_lessons_to_students(student, lesson):
    """
    Assigns lessons to a student.
    Important Notes:
        - Assigned lessons is a list of lessons from the teacher's lessons.
        - Assigned lessons must have same institution as student.
        - Assigned lessons must have same class as the student.
        - Assigned lessons must have same subject as the student.
    """

    if not student.institutions:
        return student

    # 1- Get list of lesson's institution's IDs.
    lesson_institutions_ids = {ins.id for ins in lesson.institutions}
    if student.institutions.id not in lesson_institutions_ids:
        return student

    # 2- Get list of lesson's class IDs.
    lesson_classes_ids = {clas.id for clas in lesson.classes}
    if student.classes.id not in lesson_classes_ids:
        return student

    # 3- Get list of lesson's subject IDs.
    lesson_subjects_ids = {subj.id for subj in lesson.subjects}
    if student.subjects.id not in lesson_subjects_ids:
        return student

    student.lessons.append(lesson)
    return student
