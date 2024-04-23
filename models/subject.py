#!/usr/bin/python
""" holds class Subject"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.institution import institution_subject

# A subject can be taught by many teachers as a subject can have many teachers.
subject_teacher = Table('subject_teacher', Base.metadata,
                        Column('subject_id', String(60),
                               ForeignKey('subjects.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        Column('teacher_id', String(60),
                               ForeignKey('teachers.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True))

# A subject can be taught by many students as a subject can have many students.
subject_student = Table('subject_student', Base.metadata,
                        Column('subject_id', String(60),
                               ForeignKey('subjects.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True),
                        Column('student_id', String(60),
                               ForeignKey('students.id',
                                          onupdate='CASCADE',
                                          ondelete='CASCADE'),
                               primary_key=True))


class Subject(BaseModel, Base):
    """Representation of Subject """
    __tablename__ = 'subjects'

    # Normal attributes
    name = Column(String(128), nullable=False)

    # Many to one relationship's attributes.
    # institution_id = Column(String(60), ForeignKey('institutions.id'),
    # nullable=False)

    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="subjects",
                           cascade="all, delete, delete-orphan")

    # many to many relationship's attributes.
    teachers = relationship("Teacher", secondary=subject_teacher,
                            viewonly=False)
    institutions = relationship('Institution', secondary=institution_subject,
                                viewonly=True)
