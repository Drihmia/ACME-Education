#!/usr/bin/python3
"""
Setting general many to many relationship's information for institutions
with classes and subjects.
"""

from models import storage
from models.clas import Clas
from models.institution import Institution
from models.subject import Subject

print(
    "Setting relationship between institution and thier classes and subjects")
institutions_db = storage.all(Institution).values()
subjects_db = storage.all(Subject).values()
classes_db = storage.all(Clas).values()

number_institution = len(institutions_db)

current = 1
for institution in institutions_db:
    print(f"{(current/number_institution)*100:0.2f} of 100")
    institution.subjects.extend(subjects_db)
    institution.classes.extend(classes_db)
    institution.save()
    current += 1
