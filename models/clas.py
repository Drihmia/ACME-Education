#!/usr/bin/python3
""" holds class Clas"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from models.institution import institution_clas


# A class can have many lessons as a lesson can belog to many classes.
clas_lesson = Table('clas_lesson', Base.metadata,
                    Column('clas_id', String(60),
                           ForeignKey('classes.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    Column('lesson_id', String(60),
                           ForeignKey('lessons.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    UniqueConstraint('clas_id', 'lesson_id'),
                    extend_existing=True)

# A class can have many teachers as a teacher can teach many classes.
clas_teacher = Table('clas_teacher', Base.metadata,
                     Column('clas_id', String(60),
                            ForeignKey('classes.id', onupdate='CASCADE',
                                       ondelete='CASCADE'),
                            primary_key=True),
                     Column('teacher_id', String(60),
                            ForeignKey('teachers.id', onupdate='CASCADE',
                                       ondelete='CASCADE'),
                            primary_key=True),
                     UniqueConstraint('clas_id', 'teacher_id'),
                     extend_existing=True)


class Clas(BaseModel, Base):
    """Representation of Clas """
    __tablename__ = 'classes'

    # Normal attributes
    name = Column(String(128, collation='utf8mb4_unicode_ci'),
                  nullable=False, unique=True)

    # one to Many relationship's attributes.
    students = relationship("Student",
                            backref="classes",
                            cascade="all, delete, delete-orphan")

    # many to many relationship's attributes.
    lessons = relationship("Lesson", secondary=clas_lesson, viewonly=False)

    teachers = relationship("Teacher", secondary=clas_teacher, viewonly=False)

    institutions = relationship('Institution', secondary=institution_clas,
                                viewonly=True)
