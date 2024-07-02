from functools import wraps

def printable(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        print(f"Вызов функции {old_function.__name__} с аргументами {args} и {kwargs}")
        result = old_function(*args, **kwargs)
        print(f"Получен результат {result}")
        return result

    return new_function