#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


# A city can have many different institutions as
# +an institution be in different cities.
cities_institutions = Table('cities_institutions', Base.metadata,
                            Column('institution_id', String(60),
                                   ForeignKey('institutions.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True),
                            Column('city_id', String(60),
                                   ForeignKey('cities.id',
                                              onupdate='CASCADE',
                                              ondelete='CASCADE'),
                                   primary_key=True))


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'

    # Normal attributes
    name = Column(String(128), nullable=False, unique=True)

    # Many to one relationship's attributes.
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Many to many relationship's attributes.
    institutions = relationship('Institution', secondary=cities_institutions,
                                viewonly=False, back_populates="cities")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
