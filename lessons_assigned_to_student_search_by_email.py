#!/usr/bin/python3
"""
Display all lessons assigned to a student.
Student is identified by email.
Usage: python3 lessons_assigned_to_student_search_by_email.py <email>
"""

from sys import argv
from models import storage
from models.student import Student

if len(argv) < 2:
    print(__doc__)
    exit(1)

email = argv[1]
students = storage.query(Student).filter(Student.email.like(email)).first()

if not students:
    print(f"No student found with email '{email}'")
    exit(1)

# Display student's Information
print("*" * 40)
print("*" * 40)
print(f"Student has been found:")
print(f"Full Name: {students.last_name} {students.first_name}")
print(f"Class: {students.classes.alias}")
print(f"Institution: {students.institution} ({students.city})")
print(f"Teacher's Email: {students.teacher_email}")
print("Subjects:", ", ".join([s.name for s in students.subjects]))
print("+" * 40)
print("+" * 40)

# Display Lesson's names by Class's Alias.
stats = {
    'Chimestry': 0,
    'Physics': 0,
    'DS': 0,
    'Divers': 0,
}

for lesson in students.lessons:
    lesson_name = lesson.name
    print(f" - {lesson_name} ({lesson.class_alias})")
    if 'CH' in lesson_name:
        stats['Chimestry'] += 1
    elif 'PH' in lesson_name:
        stats['Physics'] += 1
    elif 'devoir' in lesson_name.lower():
        stats['DS'] += 1
    else:
        stats['Divers'] += 1

# Display various statics about lessons an d Homeworks...
print("-" * 40)
print("-" * 40)
print(f"The total number of lessons is: {len(students.lessons)}")
print(f" - Physics Lessons: {stats.get('Physics', 0)}")
print(f" - Chimestry Lessons: {stats.get('Chimestry', 0)}")
print(f" - Homeworks: {stats.get('DS', 0)}")
print(f" - Divers Lessons: {stats.get('Divers', 0)}")
