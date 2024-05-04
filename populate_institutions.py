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


with open('schools.json', 'r', encoding='utf-8') as file:
    data = load(file)
    count = 0
    cities = storage.all(City).values()
    cities_name = [city.name for city in cities]

    dic = {}
    for city in storage.all(City).values():
        dic.update({city.name: city.id})

    institutions = storage.all(Institution).values()
    institutions_name = [institution.name for institution in institutions]

    length = len(data)
    for shool in data:
        count += 1
        print(f'{count} of {length}: {(count/length) * 100}%')
        school_name = shool.get('NOM_ETABLISSENTFR')
        if school_name is None:
            print(shool)
            continue

        if school_name in institutions_name:
            continue
        city_name = shool.get('PROVINCE')
        city_id = dic.get(city_name)
        institution = Institution(name=school_name,
                                  city=city_name,
                                  city_id=city_id)
        try:
            storage.new(institution)
            storage.save()
        except IntegrityError as e:
            print(e)
            storage.rollback()

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City),
    'institutions': storage.count(Institution)
}
print(stats)
