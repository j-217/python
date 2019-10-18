def sort_array(source_array):
    if len(source_array) == 0:
        return []
    else:
        odd_list = []
        for i in range(0, len(source_array)):
            if source_array[i] % 2 != 0:
                odd_list.append(source_array[i])
                source_array[i] = "odd"
            else:
                continue
        odd_list = sorted(odd_list, reverse=True)
        if odd_list:
            for j in range(0, len(source_array)):
                if source_array[j] == "odd":
                    source_array[j] = odd_list.pop()
                else:
                    continue
            # print(source_array)
            return source_array
        else:
            # print(source_array)
            return source_array

sort_array([5, 3, 2, 8, 1, 4])
sort_array([5, 3, 1, 8, 0])