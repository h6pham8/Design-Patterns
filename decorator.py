"""
Implementation example of decorator design pattern in Python
"""


def math_wrapper(func):
    def wrapper(x, y):
        print func(x, y) + 1

    return wrapper


# this is equivalent to add = math_wrapper(add(x, y))

@math_wrapper
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


@math_wrapper
def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


add(1, 1)    # should output 3 instead of 2
multiply(2, 2)    # should output 5 instead of 4
