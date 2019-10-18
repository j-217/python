# from math import log, ceil
#
#
# def dbl_linear(n):
#     x = ceil(log((n+1), 2))
#     a_list = gen_list(x)
#     while len(a_list) - 1 < n:
#         x *= 2
#         a_list = gen_list(x)
#     print(a_list)
#     print(len(a_list))
#     print(a_list[n])
#     print(a_list[50])
#     return a_list[n]
#
#
# def gen_list(i):
#     a_list = [1]
#     if i == 1:
#         print(a_list)
#         return a_list
#     for x in range(1, i):
#         for num in a_list[-(2**(x - 1)):]:
#             b_list = []
#             l_num = 2*num + 1
#             r_num = 3*num + 1
#             b_list.append(l_num)
#             b_list.append(r_num)
#             a_list.extend(sorted(b_list))
#     # print(a_list)
#     # print(sorted(list(set(a_list))))
#     a_list = sorted(list(set(a_list)))
#     return a_list


from collections import deque


def dbl_linear(n):
    h = 1
    count = 0
    q2, q3 = deque([]), deque([])
    while True:
        if count >= n:
            print(h)
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]:
            h = q2.popleft()
        if h == q3[0]:
            h = q3.popleft()
        count += 1

# def dbl_linear(n):
#     num_list = [1]
#     for i in num_list:
#         num_list.append((i * 2) + 1)
#         num_list.append((i * 3) + 1)
#         if len(num_list) > n * 10:
#             break
#     print(sorted(list(set(num_list)))[n])
#     return sorted(list(set(num_list)))[n]

# gen_list(5)
dbl_linear(50000)
# dbl_linear(30)