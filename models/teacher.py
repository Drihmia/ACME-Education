#!/usr/bin/python
""" holds class Teacher"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Teacher(BaseModel, Base):
    """Representation of Teacher """
    __tablename__ = 'teachers'

    # Normal attributes
    name = Column(String(128), nullable=False)

    # Many to one relationship's attributes.
    # institution_id = Column(String(60), ForeignKey('institutions.id'),
    # nullable=False)
    # subject_id = Column(String(60), ForeignKey('subjects.id'),
    # nullable=False)

    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="teachers",
                           cascade="all, delete, delete-orphan")

    # many to many relationship's attributes.
    # subjects = relationship("Subject", secondary=teacher_subject,
    # viewonly=False)