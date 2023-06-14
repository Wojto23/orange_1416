import functools


def deko(func):
    @functools.wraps(func)
    def _deko(a, b):
        result = func(a, b + 5)
        name = func.__name__
        print(f"{name}({a}, {b}) -> {result}")
        return result

    return _deko


def dekorek(func):
    @functools.wraps(func)
    def _deko(*args):
        result = func(*args)
        name = func.__name__
        print(f"{name}({args}) -> {result}")
        return result + 5

    return _deko


@dekorek
def add(a, b):
    return a + b


@dekorek
def sub(a, b, c):
    return a - b + c


def add2(a, b, /):
    return a + b


def add3(*, a, b):
    return a + b


# print(add3(b=1, a=2))
# print(add2(1, 2))
# print(add2(a=1, b=2))

# print(add(1, 2))
# print(sub(1, 2, 3))

def track(function=None, label=None):
    if label and not function:
        return functools.partial(track, label=label)

    print(f"init function: {label}")

    @functools.wraps(function)
    def _track(*args, **kwargs):
        print(f'calling: {label}')
        function(*args, **kwargs)
        print(f"called: {label}")

    return _track


# @track(label="outer")
# @track(label="inner")
# def func1():
#     print("func1")


# func1()


def add_x(function=None, add_n=0):
    if not callable(function):
        if function is not None:
            add_n = function
        return functools.partial(add_x, add_n=add_n)

    @functools.wraps(function)
    def _add_x(n):
        return function(n) + add_n

    return _add_x

@add_x
def add_zero(n):
    return n

@add_x(5)
def add_five(n):
    return n

print(add_zero(1))
print(add_five(1))