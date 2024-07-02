

from functools import wraps
import requests
from datetime import datetime


def cached(old_function):

    cache = {}

    @wraps(old_function)
    def new_function(*args, **kwargs):
        key = f"{args}_{kwargs}"
        if key in cache:
            return cache[key]
        
        result = old_function(*args, **kwargs)
        cache[key] = result
        return result
    
    new_function.cache = cache
    
    return new_function


def swapi_get_people(people_id):
    return requests.get(f'https://swapi.py4e.com/api/people/{people_id}').json()  

if __name__ == '__main__':
    t_people = cached(swapi_get_people)

    start = datetime.now()
    result = t_people(1)
    print(datetime.now() - start)
    # print(result)

    start = datetime.now()
    result = t_people(1)
    print(datetime.now() - start)
    # print(result)

    print(t_people.cache)