def smallest(n):
    s = str(n)
    min1, from1, to1 = n, 0, 0
    for i in range(len(s)):
        removed = s[:i] + s[i + 1:]
        for j in range(len(removed) + 1):
            num = int(removed[:j] + s[i] + removed[j:])
            if num < min1:
                min1, from1, to1 = num, i, j
    return [min1, from1, to1]

