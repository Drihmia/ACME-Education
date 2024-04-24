#!/usr/bin/python3
""" holds class State"""
from sqlalchemy import Column, String, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import cities_institutions

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
    __table_args__ = (UniqueConstraint('name', 'city'), )

    # Normal attributes
    # +I've approach it as nullable is False.
    name = Column(String(128), nullable=False)

    # As I've created city's and state's objects, we can set nullable's attribute
    # +Of state and city to True, so we make them optional.
    # +For more information see the file : main_test_1.py to see how
    state = Column(String(128), nullable=True)
    city = Column(String(128), nullable=False)

    # One to many relationship's attributes.
    lessons = relationship("Lesson",
                           backref="institutions",
                           cascade="all, delete, delete-orphan")

    students = relationship("Student",
                           backref="institutions",
                           cascade="all, delete, delete-orphan")

    # many to many relationship's attributes.
    teachers = relationship("Teacher", secondary=institution_teacher,
                            viewonly=False)
    subjects = relationship("Subject", secondary=institution_subject,
                            viewonly=False)
    classes = relationship('Clas', secondary=institution_clas, viewonly=False)

    cities = relationship('City', secondary=cities_institutions, viewonly=True,
                          back_populates="institutions")
