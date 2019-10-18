def mixbonacci(pattern, length):
    if all([pattern, length]):
        dict = {'fib': fibonacci(), 'pad': padovan(), 'jac': jacobstahl(), 'pel': pell(), 'tri': tribonacci(), \
                'tet': tetranacci()}
        lst = []
        while length:
            for k in pattern:
                if length > 0:
                    lst.append(dict[k].__next__())
                    length -= 1
                else:
                    break
        return lst
    else:
        return []


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def padovan():
    a, b, c = 1, 0, 0
    while True:
        yield a
        a, b, c = b, c, a+b


def tribonacci():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c


def jacobstahl():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, 2 * a + b


def tetranacci():
    a, b, c, d = 0, 0, 0, 1
    while True:
        yield a
        a, b, c, d = b, c, d, a + b + c + d


def pell():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + 2 * b


# mixbonacci(['fib'], 10)
# mixbonacci(['pad'], 10)
# mixbonacci(['jac'], 10)
# mixbonacci(['pel'], 10)
# mixbonacci(['tri'], 10)
# mixbonacci(['tet'], 10)
# mixbonacci(['fib', 'tet'], 10)
mixbonacci(['jac', 'jac', 'pel'], 10)
