from itertools import zip_longest


def add_polynomials(a, b):
    return [sum(x) for x in zip_longest(a, b, fillvalue=0)]


def multiply_polynomials(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


a = [1, 2, 3]
b = [4, 5, 6]
print(add_polynomials(a, b))
print(multiply_polynomials(a, b))
