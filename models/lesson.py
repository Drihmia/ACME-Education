#!/usr/bin/python
""" holds class Lesson"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from models.clas import clas_lesson
from models.student import student_lesson
from models.institution import institution_lesson


class Lesson(BaseModel, Base):
    """Representation of Lesson """
    __tablename__ = 'lessons'
    __table_args__ = (
        UniqueConstraint('name', 'subject_id', 'teacher_id'),
    )

    # Normal attributes
    name = Column(String(128, collation='utf8mb4_unicode_ci'),
                  nullable=False)                               # A must
    download_link = Column(String(1024, collation='utf8mb4_unicode_ci'),
                           nullable=False)                      # A must
    description = Column(String(1024, collation='utf8mb4_unicode_ci'),
                         nullable=True)
    public = Column(Boolean, nullable=True, default=True)

    # Many to one relationship's attributes.
    # institution_id = Column(String(60), ForeignKey('institutions.id'),
    # nullable=False)                     # A must
    subject_id = Column(String(60), ForeignKey('subjects.id'),
                        nullable=False)                         # A must
    teacher_id = Column(String(60), ForeignKey('teachers.id'),
                        nullable=False)                         # A must

    # many to many relationship's attributes.
    classes = relationship('Clas', secondary=clas_lesson, viewonly=True)
    students = relationship('Student', secondary=student_lesson, viewonly=True)
    institutions = relationship('Institution', secondary=institution_lesson,
                                viewonly=True)
