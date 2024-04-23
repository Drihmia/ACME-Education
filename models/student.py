#!/usr/bin/python
""" holds class Student"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, int
from sqlalchemy.orm import relationship
from models.subject import subject_student


class Student(BaseModel, Base):
    """Representation of Student """
    __tablename__ = 'students'

    # Normal attributes
    name = Column(String(128), nullable=False)
    age = Column(int, nullable=True)
    user_name = Column(String(32), nullable=True)
    passward = Column(String(32), nullable=True)

    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="students",
                           cascade="all, delete, delete-orphan")

    # Many to one relationship's attributes.
    institution_id = Column(String(60), ForeignKey('institutions.id'),
                            nullable=False)

    class_id = Column(String(60), ForeignKey('classes.id'),
                            nullable=False)

    # many to many relationship's attributes.
    subjects = relationship("Subject", secondary=subject_student,
                            viewonly=True)
