#!/usr/bin/python
""" holds class Teacher"""
import bcrypt
from sqlalchemy import Column, event, String
from models.base_model import BaseModel, Base


class Dev(BaseModel, Base):
    """Representation of Developer """
    __tablename__ = 'devs'

    # -------------------------------------------------------------
    # Normal attributes.
    first_name = Column(String(64), nullable=False, default='dev')
    last_name = Column(String(64), nullable=False, default='one')
    email = Column(String(64), nullable=False, unique=True, default='dev1@gmail.com')
    password = Column(String(64), nullable=False, default='dev1')

    # -------------------------------------------------------------
    # Optional attributes.
    gender = Column(String(1), nullable=True)
    phone_number = Column(String(14), nullable=True)



def hash_password_before_insert_or_update(_, __, dev):
    """Hashing the password before store it into database"""
    if dev.password is not None and isinstance(dev.password, str):
        # Generate a salt and hash the password using bcrypt
        if len(dev.password) != 60:
            salt = bcrypt.gensalt()
            dev.password = bcrypt.hashpw(
                dev.password.encode('utf-8'), salt)


event.listen(Dev, 'before_insert', hash_password_before_insert_or_update)
event.listen(Dev, 'before_update', hash_password_before_insert_or_update)
