#!/usr/bin/python3
"""
This script assigns private lessons to a student based on the teacher's email.
It takes two command-line arguments: the teacher's email and the student's email.
"""

from models import storage
from models.teacher import Teacher
from models.student import Student
from models.subject import Subject
from tools.assign_lessons import assign_private_lesson_to_student
from sys import argv
from sqlalchemy.exc import IntegrityError

# Check if the correct number of arguments is provided
if len(argv) != 3:
    print("Usage: assign_private_lesson_to_student_by_teacher_email.py <teacher_email> <student_email>")
    exit()

# Get teacher and student emails from command-line arguments
teacher_email = argv[1]
student_email = argv[2]

# Query the teacher and student by their emails
teacher = storage.query(Teacher).filter(Teacher.email == teacher_email).one()
student = storage.query(Student).filter(Student.email == student_email).one()

# Assign all subjects to the student if none exist
if not student.subjects:
    for subject in storage.all(Subject).values():
        try:
            subject.students.append(student)  # Add student to the subject
            subject.save()  # Save changes to the subject
        except IntegrityError:
            pass  # Ignore if the student is already associated

# Associate the student with the teacher if not already done
if student.email not in {s.email for s in teacher.students}:
    teacher.students.append(student)
    teacher.save()  # Save changes to the teacher

student_lessons_names = {l.name for l in student.lessons}
# Assign private lessons from the teacher to the student
for lesson in teacher.lessons:
    lesson_class_aliases = {c.alias for c in lesson.classes}
    if lesson.name not in student_lessons_names:
        assign_private_lesson_to_student(lesson, student).save()

student_lessons_names_after = {l.name for l in student.lessons}
# Output the student's lessons and counts
print("Student's lessons: ", student.lessons)
print("Number of lessons before new assignement: ", len(student_lessons_names))
print("Number of lessons after new assignement: ", len(student_lessons_names_after))

