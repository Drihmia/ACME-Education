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


with open('schools.json', 'r', encoding="utf-8") as file:
    data = load(file)

    dic = {}
    for state in storage.all(State).values():
        dic.update({state.name: state.id})

    cities = storage.all(City).values()
    cities_name = [city.name for city in cities]

    count = 0
    refresh = 0
    length = len(data)
    for shool in data:
        city_name = shool.get('PROVINCE')
        if city_name in cities_name:
            continue
        refresh = refresh + 1
        if not refresh % 20:
            refresh = 0
            cities = storage.all(City).values()
            print(len(cities_name), "+++++++++++++++++++ before refreshing")
            cities_name = [city.name for city in cities]
            print(len(cities_name), "+++++++++++++++++++ after refreshing")

        state_name = shool.get('REGION')
        state_id = dic.get(state_name, 'None')

        count = count + 1
        if state_id == 'None':
            print(f"---------------------------    {state_name} not found")
            continue

        print(f'--------------------------{count} of {length / 8} : {refresh}')

        city = City(name=city_name, state_id=state_id)
        print("creating :", city.name)
        storage.new(city)

        try:
            storage.save()
            print("added :", city.name)
        except IntegrityError:
            storage.rollback()
            print(".")

print('statistics:')
stats = {
    'states': storage.count(State),
    'cities': storage.count(City)
}
print(stats)
