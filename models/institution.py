#!/usr/bin/python3
""" holds class State"""
from sqlalchemy import Column, String, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

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
                                   primary_key=True),
                            UniqueConstraint('institution_id', 'teacher_id'))

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
                                   primary_key=True),
                            UniqueConstraint('institution_id', 'subject_id'))

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
                         UniqueConstraint('institution_id', 'clas_id'),
                         extend_existing=True)

# An institution can have many lessons as
# +lessons can assigned to many institutions at once
# +since teacher can work in more than institution,
# +it would reduandant to create same lesson for each
# +institution separately.
institution_lesson = Table('institution_lesson', Base.metadata,
                           Column('institution_id', String(60),
                                  ForeignKey('institutions.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  primary_key=True),
                           Column('lesson_id', String(60),
                                  ForeignKey('lessons.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  primary_key=True),
                           UniqueConstraint('institution_id', 'lesson_id'),
                           extend_existing=True)


class Institution(BaseModel, Base):
    """Representation of institution """
    __tablename__ = 'institutions'
    __table_args__ = (UniqueConstraint('name', 'city', 'city_id'), )

    # Normal attributes
    # +I've approach it as nullable is False.
    name = Column(String(128, collation='utf8mb4_unicode_ci'),
                  nullable=False)  # A must

    # Frontend can provide the city's name or city's id.
    city = Column(String(128, collation='utf8mb4_unicode_ci'),
                  nullable=True)  # It's optional.

    # One to many relationship's attributes.
    students = relationship("Student",
                            backref="institutions",
                            cascade="all, delete, delete-orphan")

    # Many to one relationship's attributes.
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)  # A must

    # many to many relationship's attributes.
    teachers = relationship("Teacher", secondary=institution_teacher,
                            viewonly=False)

    subjects = relationship("Subject", secondary=institution_subject,
                            viewonly=False)

    classes = relationship('Clas', secondary=institution_clas,
                           viewonly=False)

    lessons = relationship('Lesson', secondary=institution_lesson,
                           viewonly=False)
