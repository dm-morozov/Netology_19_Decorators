

import requests
from datetime import datetime
from printable import printable
from cached_decor import cached
from attempts_decoraror import with_attempts


# Логирование
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)


# Проверка прав доступа
def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not has_permission(permission):
                raise PermissionError(f"Нет прав для выполнения функции {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"Удаление пользователя с id {user_id}")

# Функция has_permission должна быть определена, например:
def has_permission(permission):
    # Проверка прав доступа (для примера всегда True)
    return True

delete_user(1234)


# Кеширование
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def slow_function(n):
    # Симуляция медленного вычисления
    for _ in range(10**6):
        pass
    return n * n

print(slow_function(4))  # Долгий вызов
print(slow_function(4))  # Быстрый вызов из кеша


# Урок от Киррила Табельского
@with_attempts(attemps=5, timeout=0.5)
@cached
def swapi_get_people(people_id):
    return requests.get(f'https://swapi.py4e.com/api/people/{people_id}').json()  


# t_people = printable(swapi_get_people)

# t_people(1)


t_people = swapi_get_people

start = datetime.now()
result = t_people(1)
print(datetime.now() - start)
# print(result)

start = datetime.now()
result = t_people(1)
print(datetime.now() - start)
# print(result)

print(t_people.cache)