#!/usr/bin/python
""" holds class Student"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from models.subject import subject_student
from models.teacher import teacher_student

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
                              primary_key=True),
                       UniqueConstraint('student_id', 'lesson_id'))


class Student(BaseModel, Base):
    """Representation of Student """
    __tablename__ = 'students'

    # Normal attributes
    first_name = Column(String(128), nullable=False)  # A must.
    last_name = Column(String(128), nullable=False)  # A must.
    email = Column(String(128), nullable=False, unique=True)  # A must.
    teacher_email = Column(String(128), nullable=False)  # A must.

    institution = Column(String(128), nullable=True)
    subject = Column(String(128), nullable=True)
    city = Column(String(128), nullable=True)

    password = Column(String(128), nullable=False)  # A must.

    # One to many relationship's attributes.
    # lessons = relationship("Lesson",
    # backref="students",
    # cascade="all, delete, delete-orphan")

    # Many to one relationship's attributes.
    institution_id = Column(String(60),
                            ForeignKey('institutions.id'),  # A must.
                            nullable=False)

    class_id = Column(String(60), ForeignKey('classes.id'),  # A must.
                      nullable=False)

    # many to many relationship's attributes.
    subjects = relationship("Subject", secondary=subject_student,
                            viewonly=True)
    lessons = relationship("Lesson", secondary=student_lesson,
                           viewonly=False)
    teachers = relationship("Teacher", secondary=teacher_student,
                            viewonly=True)
