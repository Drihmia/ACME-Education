#!/usr/bin/python3
"""
This script populate our database's ACME education website with states
and cities of Morocco
"""
from json import load
from sqlalchemy.exc import IntegrityError
from models import storage
from models.state import State
from models.city import City


with open('schools.json', 'r') as file:
    data = load(file)

    for shool in data:
        state_found = 0
        state_name = shool.get('REGION')
        for state_obj in storage.all(State).values():
            if state_obj.name == state_name:
                state_found = 1
                city_name = shool.get('PROVINCE')
                city = City(name=city_name, state_id=state_obj.id)
                try:
                    storage.new(city)
                    print("adding :", city.name)
                except IntegrityError as e:
                    print(e)
                    storage.rollback()
                try:
                    storage.save()
                except IntegrityError:
                    storage.rollback()
                    print("**********************************************")
        if not state_found:
            print(f'state: {state_name} not found')

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City)
}
print(stats)
