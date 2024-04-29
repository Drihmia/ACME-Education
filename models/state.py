#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'

    # Normal attributes
    name = Column(String(128, collation='utf8mb4_unicode_ci'),
                  nullable=False, unique=True)

    # One to many relationship's attribute
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
