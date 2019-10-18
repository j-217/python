# def decompose(n):
#     a = n
#     while a > 1:
#         goal = n ** 2
#         decompose_list = []
#         for i in range(a-1, 0, -1):
#             if (goal - i**2) >= 0:
#                 goal -= i**2
#                 decompose_list.append(i)
#                 if goal == 0:
#                     print(sorted(decompose_list))
#                     return sorted(decompose_list)
#         a -= 1
#     print("None")
#     return None

#
from math import sqrt, floor, ceil

#
# def decompose(n):
#     a = n
#     while a > 1:
#         goal = n ** 2
#         decompose_list = []
#         next_num = a - 1
#         while goal > 0:
#             goal -= next_num**2
#             decompose_list.append(next_num)
#             next_num = floor(sqrt(goal))
#             # print(next_num)
#             if goal == 0 and len(set(decompose_list)) == len(decompose_list):
#                 print(sorted(decompose_list))
#                 return sorted(decompose_list)
#         a -= 1
#     print("None")
#     return None


def decompose(n):
    def recurse(goal, next_num):
        if goal == 0:
            return []
        for i in range(next_num, 0, -1):
            if str(sqrt(goal - i**2)).isdigit():
                next_num = sqrt(goal - i**2) - 1
            else:
                next_num = floor(sqrt(goal - i**2))
            sub = recurse(goal - i**2, next_num)
            if sub is not None:
                return sub + [i]
    print(recurse(n**2, n - 1))


# def decompose(n):
#     def recurse(s, i):
#         if s < 0:
#             return None
#         if s == 0:
#             return []
#         for j in range(i - 1, 0, -1):
#             sub = recurse(s-j**2, j)
#             if sub != None:
#                 return sub+[j]
#     # return recurse(n**2, n)
#     print(recurse(n**2, n))

# decompose(5)
# decompose(50)
decompose(12)
# decompose(8)
# decompose(7654320)
# decompose(1234566)
# decompose(7654322)