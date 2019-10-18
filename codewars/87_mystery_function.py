from math import log, ceil


def mystery(n):
    """
    n: index of T(m)
    """
    # if n <= 1:
    #     return n
    # s = ''
    # m = int(ceil(log(n + 1, 2)))
    # while m >= 1:
    #     if n > 2**(m - 1) - 1:
    #         s += '1'
    #         n = (2**(m - 1) - 1) - (n - 2**(m - 1))
    #         m -= 1
    #     else:
    #         s += '0'
    #         m -= 1
    # return int(s, 2)
    print(n ^ (n >> 1))


def mystery_inv(n):
    n = bin(n)[2:]
    m = len(n)
    low, high, inv = 0, 2**m - 1, 0
    for i in n:
        if inv == 0:
            if i == '1':
                low += (high - low + 1) // 2
                inv = 1
            elif i == '0':
                high -= (high - low + 1) // 2
        elif inv == 1:
            if i == '1':
                high -= (high - low + 1) // 2
                inv = 0
            elif i == '0':
                low += (high - low + 1) // 2
    print(low, high)
    return low


def name_of_mystery():
    return 'Gray code'


# mystery(1753749276131411421)
mystery_inv(9)
