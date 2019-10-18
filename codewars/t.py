def test():
    l = [0] * 10
    for i in range(10):
        l[i] = a(i)
    return l


def a(x):
    print(x)


test()
