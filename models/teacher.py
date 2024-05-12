#!/usr/bin/python
""" holds class Teacher"""
import bcrypt
from sqlalchemy import Column, event, String
from sqlalchemy import ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.clas import clas_teacher
from models.institution import institution_teacher
from models.subject import subject_teacher


teacher_student = Table('teacher_student', Base.metadata,
                        Column('student_id', String(60),
                               ForeignKey('students.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        Column('teacher_id', String(60),
                               ForeignKey('teachers.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        UniqueConstraint('student_id', 'teacher_id'))


class Teacher(BaseModel, Base):
    """Representation of Teacher """
    __tablename__ = 'teachers'

    # -------------------------------------------------------------
    # Normal attributes.
    first_name = Column(String(64), nullable=False)  # A must
    last_name = Column(String(64), nullable=False)  # A must
    email = Column(String(64), nullable=False, unique=True)  # A must
    password = Column(String(64), nullable=False)  # A must

    # -------------------------------------------------------------
    # Optional attributes.
    gender = Column(String(1), nullable=True)
    institution = Column(String(128), nullable=True)
    main_subject = Column(String(128), nullable=True)
    city = Column(String(64), nullable=True)
    phone_number = Column(String(14), nullable=True)

    # -------------------------------------------------------------
    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="teachers",
                           cascade="all, delete, delete-orphan")

    # -------------------------------------------------------------
    # many to many relationship's attributes.
    students = relationship('Student', secondary=teacher_student,
                            viewonly=False)
    subjects = relationship("Subject", secondary=subject_teacher,
                            viewonly=True)
    institutions = relationship('Institution', secondary=institution_teacher,
                                viewonly=True)
    classes = relationship('Clas', secondary=clas_teacher, viewonly=True)


def hash_password_before_insert_or_update(_, __, teacher):
    """Hashing the password before store it into database"""
    if teacher.password is not None and isinstance(teacher.password, str):
        # Generate a salt and hash the password using bcrypt
        if len(teacher.password) != 60:
            salt = bcrypt.gensalt()
            teacher.password = bcrypt.hashpw(
                teacher.password.encode('utf-8'), salt)


event.listen(Teacher, 'before_insert', hash_password_before_insert_or_update)
event.listen(Teacher, 'before_update', hash_password_before_insert_or_update)
