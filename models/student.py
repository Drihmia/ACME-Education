#!/usr/bin/python
""" holds class Student"""
import bcrypt
from sqlalchemy import Column, event, String
from sqlalchemy import ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
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

    # -------------------------------------------------------------
    # Normal attributes
    first_name = Column(String(128, collation='utf8mb4_unicode_ci'),
                        nullable=False)  # A must.
    last_name = Column(String(128, collation='utf8mb4_unicode_ci'),
                       nullable=False)  # A must.
    email = Column(String(128, collation='utf8mb4_unicode_ci'),
                   nullable=False, unique=True)  # A must.
    password = Column(String(128, collation='utf8mb4_unicode_ci'),
                      nullable=False)  # A must.

    # -------------------------------------------------------------
    # Optional attributes.
    gender = Column(String(1), nullable=True)
    teacher_email = Column(String(64, collation='utf8mb4_unicode_ci'),
                           nullable=True)
    institution = Column(String(128, collation='utf8mb4_unicode_ci'),
                         nullable=True)
    city = Column(String(64, collation='utf8mb4_unicode_ci'),
                  nullable=True)
    phone_number = Column(String(14), nullable=True)

    # -------------------------------------------------------------
    # Many to one relationship's attributes.
    institution_id = Column(String(60),
                            ForeignKey('institutions.id'),  # A must.
                            nullable=False)

    class_id = Column(String(60),
                      ForeignKey('classes.id'),  # A must.
                      nullable=False)

    # -------------------------------------------------------------
    # many to many relationship's attributes.
    subjects = relationship("Subject", secondary=subject_student,
                            viewonly=True)
    lessons = relationship("Lesson", secondary=student_lesson,
                           viewonly=False)
    teachers = relationship("Teacher", secondary=teacher_student,
                            viewonly=True)


def hash_password_before_insert_or_update(_, __, student):
    """Hashing the password before store it into database"""
    if student.password is not None and isinstance(student.password, str):
        # Generate a salt and hash the password using bcrypt
        salt = bcrypt.gensalt()
        student.password = bcrypt.hashpw(
            student.password.encode('utf-8'), salt)


event.listen(Student, 'before_insert', hash_password_before_insert_or_update)
event.listen(Student, 'before_update', hash_password_before_insert_or_update)
