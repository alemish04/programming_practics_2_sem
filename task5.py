from functools import reduce


def numbers_to_string(numbers):
    return reduce(lambda x, y: x + ' ' + y, map(str, numbers))


numbers = [1, 15, 246, 156930]
print(numbers_to_string(numbers))
print(type(numbers_to_string(numbers)))