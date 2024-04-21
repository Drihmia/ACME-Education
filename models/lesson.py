#!/usr/bin/python
""" holds class Lesson"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


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
