#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# An institutions can have many teachers as
# + a teacher can  work in many institutions.
institution_teacher = Table('institution_teacher', Base.metadata,
                            Column('institution_id', String(60),
                                   ForeignKey('institutions.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True),
                            Column('teacher_id', String(60),
                                   ForeignKey('teachers.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True))

# A teacher can teach many subjects as subject can have many teachers.
institution_subject = Table('institution_subject', Base.metadata,
                            Column('institution_id', String(60),
                                   ForeignKey('institutions.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True),
                            Column('subject_id', String(60),
                                   ForeignKey('subjects.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True))

# An institution can have many classes as
# +classes can belong to many institutions.
institution_clas = Table('institution_clas', Base.metadata,
                         Column('institution_id', String(60),
                                ForeignKey('institutions.id',
                                           onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True),
                         Column('clas_id', String(60),
                                ForeignKey('classes.id',
                                           onupdate='CASCADE',
                                           ondelete='CASCADE'),
                                primary_key=True),
                         extend_existing=True)


class Institution(BaseModel, Base):
    """Representation of institution """
    __tablename__ = 'institutions'

    # Normal attributes
    city = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    state = Column(String(128), nullable=True)

    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="institutions",
                           cascade="all, delete, delete-orphan")

    # many to many relationship's attributes.
    teachers = relationship("Teacher", secondary=institution_teacher,
                            viewonly=False)
    subjects = relationship("Subject", secondary=institution_subject,
                            viewonly=False)
    classes = relationship('Clas', secondary=institution_clas, viewonly=False)

    # classes = relationship("Class",
    # backref="institutions",
    # cascade="all, delete, delete-orphan")
