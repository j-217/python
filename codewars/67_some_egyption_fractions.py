from fractions import Fraction
from math import ceil


def decompose(n):
    if n == '0':
        return []
    n = Fraction(n).limit_denominator()
    x = n.numerator
    y = n.denominator
    print(x, y)
    if y is 1:
        return [str(x)]
    dec_lst = []
    while x > 0:
        dec_lst.append(Fraction(1, ceil(y/x)))
        x, y = (-y) % x, y * ceil(y/x)
    return list(map(str, dec_lst))

decompose('0.66')
decompose('21/23')
# decompose('3/4')
# decompose('75/3')