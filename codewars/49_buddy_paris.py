from math import sqrt, ceil


def buddy(start, limit):
    while start <= limit:
        m = sum(factor_set(start)) - 1
        if m > start and sum(factor_set(m))-1 == start:
            return [start, m]
        start += 1
    print('1')
    return "Nothing"


def factor_set(num):
    f_set = {1, }
    for f in range(2, ceil(sqrt(num))):
        if num % f == 0:
            f_set.add(f)
            f_set.add(num//f)
    print(f_set)
    return f_set

# buddy(10,50)
# factor_set(5775)
# factor_set(6218)
buddy(2177, 4357)