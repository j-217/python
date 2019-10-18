from functools import reduce


def sum_for_list(lst):
    d, f_lst = {}, []
    for num in set(lst):
        d[num] = p_factors(num)
    total_factors = sorted(reduce(lambda x, y: x.union(y), d.values()))
    for p in total_factors:
        sum_of_nums = 0
        for num in lst:
            if num % p == 0:
                sum_of_nums += num
        f_lst.append([p, sum_of_nums])
    return f_lst


def p_factors(num):
    num = abs(num)
    lst = []
    while num >= 2:
        for p in range(2, num + 1):
            if num % p == 0:
                lst.append(p)
                num = num // p
                break
    return set(lst)


sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100])
