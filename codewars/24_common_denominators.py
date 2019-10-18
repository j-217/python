# import decimal
#
# def convertFracts(lst):
#     if len(lst) < 2:
#         return lst
#     lcm_r = lst[0][1]
#     convert_lst = []
#     for i in range(1, len(lst)):
#         gcd_r = gcd(lcm_r, lst[i][1])
#         lcm_r = lcm(lcm_r, lst[i][1], gcd_r)
#         print(gcd_r)
#         print(lcm_r)
#     for i in range(0, len(lst)):
#         convert_lst.append([int(lcm_r / lst[i][1] * lst[i][0]), int(lcm_r)])
#     print(convert_lst)
#     # return convert_lst
#
#
# def gcd(a, b):
#     """
#     计算a,b最大公约数
#     """
#     if a % b == 0:
#         return b
#     else:
#         a, b = b, a % b
#         return gcd(a, b)
#
#
# def lcm(a, b, gcd_ab):
#     """
#     计算a,b最小公倍数
#     """
#     return decimal.Decimal(a * b / gcd_ab)

import math
import functools


def convertFracts(lst):
    lcm = lambda a, b: a*b // math.gcd(a, b)
    tmp_list = list(map(lambda x: x[1], list(lst)))
    lcm_num = functools.reduce(lcm, tmp_list)
    print(list(map(lambda x: [x[0] * lcm_num // x[1], lcm_num], list(lst))))
    return list(map(lambda x: [x[0] * lcm_num // x[1], lcm_num], list(lst)))

# convertFracts([[1, 2], [1, 3], [1, 4]])
convertFracts([[27115, 5262], [87546, 11111111], [43216, 255689]])
