from collections import deque


# def parts_sums(ls):
#     sums_lst = []
#     sums = sum(ls)
#     ls = deque(ls)
#     while ls:
#         sums_lst.append(sums)
#         sums -= ls.popleft()
#     sums_lst.append(0)
#     print(sums_lst)
#     return sums_lst

def parts_sums(ls):
    ds, res = deque(ls), deque([0])
    while ds:
        res.appendleft(res[0] + ds.pop())
    print(res)
    return list(res)


parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358])