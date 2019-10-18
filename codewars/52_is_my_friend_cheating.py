def removeNb(n):
    sum_n = sum(range(1, int(n)+1))
    lst = []
    for a in range(1, int(n)+1):
        b = (sum_n - a) / (a + 1)
        if a != b and b == int(b) and int(b) <= int(n):
            lst.append((a, int(b)))
        else:
            continue
    return lst


removeNb(26)