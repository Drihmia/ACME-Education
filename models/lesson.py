#!/usr/bin/python
""" holds class Lesson"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.clas import clas_lesson


class Lesson(BaseModel, Base):
    """Representation of Lesson """
    __tablename__ = 'lessons'

    # Normal attributes
    name = Column(String(128), nullable=False)
    download_link = Column(String(1024), nullable=False)
    description = Column(String(1024), nullable=True)

    # Many to one relationship's attributes.
    institution_id = Column(String(60), ForeignKey('institutions.id'),
                            nullable=False)
    subject_id = Column(String(60), ForeignKey('subjects.id'), nullable=False)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)

    # many to many relationship's attributes.
    classes = relationship('Clas', secondary=clas_lesson, viewonly=True)
