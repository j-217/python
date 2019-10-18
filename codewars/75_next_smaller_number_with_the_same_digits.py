def next_smaller(n):
    s_n = str(n)
    flag = have_next(s_n)
    if flag == -1:
        print(flag)
        return flag
    tail = list(s_n[flag - 1:])
    head_num = s_n[:flag - 1] if s_n[:flag - 1] else ''
    tail_head = max([x for x in tail if int(x) < int(tail[0])])
    tail.remove(tail_head)
    tail_tail = sorted(tail, reverse=True)
    tail_num = tail_head + ''.join(tail_tail)
    return int(head_num + tail_num) if len(str(int(head_num + tail_num))) == len(s_n) else -1


def have_next(s_n):
    for i in range(len(s_n) - 1, 0, -1):
        if int(s_n[i]) >= int(s_n[i - 1]):
            continue
        else:
            return i
    return -1


next_smaller(1027)
