from itertools import permutations


def next_bigger(n):
    s_n = str(n)
    flag = have_next(s_n)
    if flag == -1:
        return flag
    tail = s_n[flag - 1:]
    head_num = int(s_n[:flag - 1]) * 10 ** len(tail) if s_n[:flag - 1] else 0
    tail_num = min([int(''.join(x)) for x in list(permutations(tail, len(tail))) if int(''.join(x)) > int(tail)])
    return head_num + tail_num


def have_next(s_n):
    for i in range(len(s_n)-1, 0, -1):
        if s_n[i] <= s_n[i-1]:
            continue
        else:
            return i
    return -1






    # lst = list(permutations(s_n, len(s_n)))
    # next_num = min([int(''.join(x)) for x in lst if int(''.join(x)) > n])
    # print(next_num if next_num else -1)
    # return next_num if next_num else -1


next_bigger(4023)