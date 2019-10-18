# def solution(args):
#     # 效率太低
#     str_lst = []
#     while args:
#         if len(args) == 1:
#             str_lst += [str(args.pop())]
#             break
#         first_num = args[0]
#         for add, num in enumerate(args):
#             if first_num + add == args[len(args) - 1]:
#                 str_lst += [str(first_num) + "-" + str(first_num + add)]
#                 args = []
#                 break
#             if first_num + add + 1 in args:
#                 continue
#             if first_num + add + 1 not in args and add >= 2:
#                 str_lst += [str(first_num) + "-" + str(first_num + add)]
#                 args = args[add:]
#                 break
#             if first_num + add + 1 not in args and add == 1:
#                 str_lst += [str(first_num)]
#                 args = args[add:]
#                 break
#     print(",".join(string for string in str_lst))
#     return ",".join(string for string in str_lst)
from itertools import groupby


def solution(args):
    string_lst = []
    fun = lambda x: x[1] - x[0]
    for k, v in groupby(enumerate(args), fun):
        lst = [j for i, j in v]
        print(lst)
        if len(lst) > 2:
            string_lst += [str(min(lst)) + "-" + str(max(lst))]
        elif len(lst) == 2:
            # string_lst += [str(lst[0])]
            # string_lst += [str(lst[1])]
            string_lst += [str(v) for k, v in enumerate(lst)]
        else:
            string_lst += [str(lst[0])]
    print(",".join(string for string in string_lst))



solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
# solution([1,7])
# solution([1])
# solution([])
