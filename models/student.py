#!/usr/bin/python
""" holds class Student"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INT, Table
from sqlalchemy.orm import relationship
from models.subject import subject_student

# A lesson can be shared among many students as
# +a student can have access to many students.
student_lesson = Table('student_lesson', Base.metadata,
                        Column('lesson_id', String(60),
                               ForeignKey('lessons.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        Column('student_id', String(60),
                               ForeignKey('students.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True))



class Student(BaseModel, Base):
    """Representation of Student """
    __tablename__ = 'students'

    # Normal attributes
    name = Column(String(128), nullable=False, unique=True)
    age = Column(INT, nullable=True)
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
    lessons = relationship("Lesson", secondary=student_lesson,
                            viewonly=False)
