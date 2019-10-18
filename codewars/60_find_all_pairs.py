def duplicates(arr):
    # if len(arr) <= 1:
    #     return 0
    # for n in num_set:
    #     pairs += (arr.count(n) // 2)
    # return sum((arr.count(n) // 2) for n in set(arr))
    return sum((arr.count(n) // 2) for n in set(arr)) if arr else 0


duplicates([54])