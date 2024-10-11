#!/usr/bin/python3
"""
Setting general many to many relationship's information for institutions
with classes and subjects.
"""

from models import storage
from models.clas import Clas
from models.institution import Institution
from models.subject import Subject
from sqlalchemy import or_

print(
    "Setting relationship between institution and thier classes and subjects")
institutions_db = storage.all(Institution).values()
subjects_db = storage.all(Subject).values()
classes_college_db = storage.query(Clas).filter(
    Clas.name.like("%college%")).all()
classes_lycee_db = storage.query(Clas).filter(or_(
    Clas.name.like("Tronc%"),
    Clas.name.like("%Bac%")
)).all()

print(f"number of classes_college_db: {len(classes_college_db)}")
print(f"number of classes_lycee_db: {len(classes_lycee_db)}")
[print("classes_lycee_db:", cla_lyc.name) for cla_lyc in classes_lycee_db]


number_institution = len(institutions_db)

classes_db = []
current = 1
for institution in institutions_db:
    print(f"{(current/number_institution)*100:0.2f} of 100")

    if institution.name.lower().startswith("lycee"):
        if "college" in institution.name.lower():
            classes_db = classes_college_db

        classes_db = classes_lycee_db
    elif "college" in institution.name.lower():
        classes_db = classes_college_db

    institution.subjects.extend(subjects_db)
    institution.classes.extend(classes_db)
    institution.save()
    current += 1
