#!/usr/bin/python3
"""
This script populate our database's ACME education website with states
and cities of Morocco
"""
from json import load
from sqlalchemy.exc import IntegrityError
from models import storage
from models.institution import Institution
from models.city import City
from models.state import State


with open('schools.json', 'r') as file:
    data = load(file)

    for shool in data:
        city_found = 0
        school_name = shool.get('NOM_ETABLISSENTFR')
        city_name = shool.get('PROVINCE')
        for city in storage.all(City).values():
            if city.name == city_name:
                city_found = 1
                institution = Institution(name=school_name,
                                          city=city_name,
                                          city_id=city.id)
                try:
                    storage.new(institution)
                    storage.save()
                except IntegrityError:
                    storage.rollback()
                else:
                    print(institution.name)
        if not city_found:
            print(f'city: {city_name} not found')

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City),
    'institutions': storage.count(Institution)
}
print(stats)
