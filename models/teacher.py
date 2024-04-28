#!/usr/bin/python
""" holds class Teacher"""
from sqlalchemy import Column, event, String
from hashlib import sha256
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table, UniqueConstraint
from models.base_model import BaseModel, Base
from models.subject import subject_teacher
from models.institution import institution_teacher
from models.clas import clas_teacher


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
    # __table_args__ = (UniqueConstraint('first_name', 'last_name'), )

    # Normal attributes
    first_name = Column(String(128), nullable=False)  # A must
    last_name = Column(String(128), nullable=False)  # A must
    email = Column(String(128), nullable=False, unique=True)  # A must

    institution = Column(String(128), nullable=True)
    subject = Column(String(128), nullable=True)
    city = Column(String(128), nullable=True)

    password = Column(String(128), nullable=False)  # A must

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
    subjects = relationship("Subject", secondary=subject_teacher,
                            viewonly=True)
    institutions = relationship('Institution', secondary=institution_teacher,
                                viewonly=True)
    classes = relationship('Clas', secondary=clas_teacher, viewonly=True)
    students = relationship('Student', secondary=teacher_student,
                            viewonly=True)


def hash_password_before_insert_or_update(_, __, teacher):
    if teacher.password is not None:
        # Hash the password using sha256
        teacher.password = sha256(teacher.password.encode()).hexdigest()


event.listen(Teacher, 'before_insert', hash_password_before_insert_or_update)
event.listen(Teacher, 'before_update', hash_password_before_insert_or_update)
