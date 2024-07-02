

import time
from functools import wraps

ATTEMPS = 3
TIMEOUT = 0.1


def with_attempts(attemps=ATTEMPS, timeout=TIMEOUT):
    
    def decorator(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            error = None
            for item in range(1, attemps + 1):
                try:
                    return old_function(*args, **kwargs)
                except Exception as e:
                    error = e
                    print(f"При вызове {old_function.__name__} получена ошибка {e} при попытке {item}")
                    time.sleep(timeout)
            raise error
        return new_function

    return decorator