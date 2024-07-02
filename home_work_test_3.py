import types
from datetime import datetime
from functools import wraps


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            create_log = (f"Функция {function_name} с аргументами {args} и "
                        f"{kwargs} была вызвана {current_time} и вернула '{result}'")
            print(create_log)

            with open(path, 'w') as log_file:
                log_file.write(create_log + '\n')

            return result

        return new_function

    return __logger

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item

@logger('task_3.log')
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        # print(flat_iterator_item)

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    return "Тест пройден успешно"


if __name__ == '__main__':
    test_4()