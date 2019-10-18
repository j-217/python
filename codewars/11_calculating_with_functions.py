def zero(function = None):
    print("*" * 10)
    print("zero")
    return 0 if function is None else function(0)


def one(function = None):
    print("*" * 10)
    print("one")
    return 1 if function is None else function(1)


def two(function = None):
    return 2 if function is None else function(2)


def three(function = None):
    return 3 if function is None else function(3)


def four(function = None):
    return 4 if function is None else function(4)


def five(function = None):
    return 5 if function is None else function(5)


def six(function = None):
    return 6 if function is None else function(6)


def seven(function = None):
    return 7 if function is None else function(7)


def eight(function = None):
    return 8 if function is None else function(8)


def nine(function = None):
    return 9 if function is None else function(9)


def plus(b):
    print("*" * 10)
    print("plus")
    # b = function
    def calc(a):
        print(a + b)
    return calc
    # return lambda a: a + b


def minus(function):
    b = function
    return lambda a: a - b


def times(function):
    b = function
    return lambda a: a * b


def divided_by(function):
    b = function
    return lambda a: a // b


# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y

zero(plus(one()))
# two(minus(three()))