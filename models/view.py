#!/usr/bin/python
""" holds class Recently_signed_students_by_class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Recently_signed_students_by_class(BaseModel, Base):
    """Representation of a table that view all recently
    signed up students by class
    """
    __tablename__ = 'recently_signed_students_by_class'

    # -------------------------------------------------------------
    # Ignored attributes from the BaseModel:
    id = None

    # -------------------------------------------------------------
    # Normal attributes
    full_name = Column(String(256, collation='utf8mb4_unicode_ci'),
                        primary_key=True)  # A must.
    email = Column(String(128, collation='utf8mb4_unicode_ci'),
                   nullable=False, unique=True)  # A must.

    # -------------------------------------------------------------
    # Optional attributes.
    alias = Column(String(16, collation='utf8mb4_unicode_ci'),
                         nullable=True)
    phone_number = Column(String(14), nullable=True)


class Recently_signed_teachers(BaseModel, Base):
    """Representation of a table that view all recently
    signed up teachers
    """
    __tablename__ = 'recently_signed_teachers'

    # -------------------------------------------------------------
    # Ignored attributes from the BaseModel:
    id = None

    # -------------------------------------------------------------
    # Normal attributes
    full_name = Column(String(256, collation='utf8mb4_unicode_ci'),
                        primary_key=True)  # A must.
    email = Column(String(128, collation='utf8mb4_unicode_ci'),
                   nullable=False, unique=True)  # A must.

    # -------------------------------------------------------------
    # Optional attributes.
    phone_number = Column(String(14), nullable=True)
