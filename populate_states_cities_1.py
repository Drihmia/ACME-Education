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


with open('state_cities.json', 'r') as file:
    json_data = load(file)

    cities_by_region = json_data.get('cities-by-region')
    # Data is a list
    data = cities_by_region.get('data')

    for state in data:
        state_name = state.get('region-name')
        state_obj = State(name=state_name)
        storage.new(state_obj)
        storage.save()

        state_id = state_obj.id
        # Cities is a list
        for city in state.get('cities'):
            city_name = city.get('names').get('en')
            city_obj = City(name=city_name, state_id=state_id)
            try:
                storage.new(city_obj)
                storage.save()
            except IntegrityError as e:
                print(e)
                storage.rollback()

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City)
}
print(stats)
