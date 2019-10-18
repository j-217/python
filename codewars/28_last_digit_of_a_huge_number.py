# def last_digit(lst):
#     if len(lst) == 1:
#         print(int(str(lst[0])[-1]))
#         return int(str(lst[0])[-1])
#     elif len(lst) > 1:
#         base_num = int(str(lst.pop(0))[-1])
#         if base_num in (2, 3, 7, 8):
#             n = lst.pop(0)
#             exponet = n if n == 0 else n % 4 if n % 4 != 0 else 4
#             while lst:
#                 n = lst.pop(0)
#                 exponet = 1 if n == 0 else exponet ** n % 4 if exponet ** n % 4 != 0 else 4
#         elif base_num in (4, 9):
#             n = lst.pop(0)
#             exponet = n if n == 0 else n % 2 if n % 2 != 0 else 2
#             while lst:
#                 n = lst.pop(0)
#                 exponet = 1 if n == 0 else exponet ** n % 2 if exponet ** n % 2 != 0 else 2
#         elif base_num in (0, 1, 5, 6):
#             # n = lst.pop(0)
#             # exponet = 1 if n != 0 else 0
#             while lst:
#                 n = lst.pop(0)
#                 exponet = 1 if n != 0 else 0
#         lst_num = int(str(base_num ** exponet)[-1])
#         print(lst_num)
#         return lst_num
#     else:
#         print(1)
#         return 1


# def power(lst):
#     x = lst.pop()
#     n = int(str(lst.pop())[-1])
#     if x == 0:
#         last_num = 1
#     elif n in {2, 3, 7, 8}:
#         exponet = x % 4 if x % 4 != 0 else 4
#         last_num = int(str(n ** exponet)[-1])
#     elif n in {4, 9}:
#         exponet = x % 2 if x % 2 != 0 else 2
#         last_num = int(str(n ** exponet)[-1])
#     elif n in {0, 1, 5, 6}:
#         last_num = n
#     lst.append(last_num)
#     return lst

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        # 如果直接写x ** (n % 4 + 4) ,当n是0时结果就会出错
        n = x ** (n if n < 4 else n % 4 + 4)
    print(n % 10)
    return n % 10


# last_digit([2, 2, 2, 0])
# last_digit([0, 0, 0])
# last_digit([])
# last_digit([0, 0])
# last_digit([4, 3, 6])
last_digit([7, 6, 21])
last_digit([12, 30, 21])