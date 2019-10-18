def order_weight(strng):
    lst = strng.split(" ")
    dict = {}
    for n in lst:
        weight = str(sum(int(x) for x in n))
        if weight not in dict:
            dict[weight] = [n]
        elif weight in dict:
            dict[weight].append(n)
    weight_lst = sorted(map(lambda k: int(k), dict.keys()))
    blst = []
    for key in weight_lst:
        blst.append(' '.join(sorted(dict[str(key)])))
    print(' '.join(blst))




order_weight('103 123 4444 99 2000')