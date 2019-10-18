def closest(strng):
    lst = strng.split(' ')
    weight_lst = []
    weight_dict = {}
    final_lst = []
    for l in lst:
        weight = 0
        for x in l:
            weight += int(x)
        weight_lst.append(weight)
    for index, w in enumerate(weight_lst):
        if w not in weight_dict:
            weight_dict[w] = [index]
        elif w in weight_dict:
            weight_dict[w].append(index)
    print(weight_dict)
    print(sorted(weight_dict))
    for i in sorted(weight_dict):
        if len(weight_dict[i]) > 1:
            print([[i, weight_dict[i][0], int(lst[weight_dict[i][0]])], [i, weight_dict[i][1], int(lst[weight_dict[i][1]])]])
            return [[i, weight_dict[i][0], int(lst[weight_dict[i][0]])], [i, weight_dict[i][1], int(lst[weight_dict[i][1]])]]
        else:
            continue
    dif = 100
    nums = []
    for j in range(len(sorted(weight_dict)) - 1):
        if sorted(weight_dict)[j+1] - sorted(weight_dict)[j] < dif:
            dif = sorted(weight_dict)[j+1] - sorted(weight_dict)[j]
            nums = [sorted(weight_dict)[j], sorted(weight_dict)[j+1]]
        else:
            continue
    for k in nums:
        final_lst.append([k, weight_dict[k][0], int(lst[weight_dict[k][0]])])
    print(lst[7])
    print(final_lst)



# closest("456899 50 11992 176 272293 163 389128 96 290193 85 52")
closest("239382 162 254765 182 485944 134 468751 62 49780 108 54")
