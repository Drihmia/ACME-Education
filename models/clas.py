#!/usr/bin/python3
""" holds class Clas"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


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
                     extend_existing=True)


class Clas(BaseModel, Base):
    """Representation of Clas """
    __tablename__ = 'classes'

    # Normal attributes
    name = Column(String(128), nullable=False)

    # Many to one relationship's attributes.
#     institution_id = Column(String(60), ForeignKey('institutions.id'),
# nullable=False)

# teacher_id = Column(String(60), ForeignKey('teachers.id'),
# nullable=False)

# lesson_id = Column(String(60), ForeignKey('lessons.id'),
# nullable=False)

# One to many relationship's attributes.
# teachers = relationship("Teacher",
# backref="classes",
# cascade="all, delete, delete-orphan")


# many to many relationship's attributes.
lessons = relationship("Lesson", secondary=clas_lesson, viewonly=False)


teachers = relationship("Teacher", secondary=clas_teacher, viewonly=False)