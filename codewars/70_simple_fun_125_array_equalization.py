def array_equalization(a, k):
    counts_lst = []
    for i in range(len(a)):
        a_lst = a.copy()
        counts_lst.append(counts(a_lst, k, i))
    return min(counts_lst)


def counts(a_lst, k, i):
    same_num, start_index, count = a_lst[i], 0, 0
    while start_index < len(a_lst):
        if a_lst[start_index] == same_num:
            start_index += 1
        else:
            for i in range(k-1, -1, -1):
                if start_index + i == len(a_lst) - 1:
                    count += 1
                    return count
                elif start_index + i < len(a_lst) - 1:
                    count += 1
                    start_index += i
                    a_lst[start_index] = same_num
                    break
                elif start_index + i > len(a_lst) - 1:
                    continue
    return count




# array_equalization([1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1], 2)
# array_equalization([6, 2, 10, 8, 2, 9, 9, 10, 4, 6, 9, 7, 7, 1, 1, 9, 4, 10, 6, 9], 7)
array_equalization([6, 3, 4, 5, 2, 4, 6, 5, 7, 1, 4, 3], 2)