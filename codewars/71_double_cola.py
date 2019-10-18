from math import log, ceil


def who_is_next(names, r):
    a = r / len(names)
    # b为该计算循环的层数
    b = ceil(log(a + 1, 2))
    # c为最后一次循环后的剩余总数
    c = r - (2**(b - 1) - 1)*len(names)
    for i in range(len(names)):
        if c - 2**(b - 1) <= 0:
            print(names[i])
            return names[i]
        else:
            c -= 2**(b - 1)
    print(names[i])
    return names[i]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
who_is_next(names, 1)