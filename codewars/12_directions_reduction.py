# def dirReduc(arr):
#     while len(arr):
#         final_dir = []
#         final_dir.append(arr.pop(0))
#         while len(arr):
#             next_dir = arr.pop(0)
#             if next_dir == 'NORTH' and final_dir.count('SOUTH') == 0:
#                 final_dir.append(next_dir)
#             elif next_dir == 'NORTH' and final_dir.count('SOUTH') != 0:
#                 final_dir.remove('SOUTH')
#             if next_dir == 'SOUTH' and final_dir.count('NORTH') == 0:
#                 final_dir.append(next_dir)
#             elif next_dir == 'SOUTH' and final_dir.count('NORTH') != 0:
#                 final_dir.remove('NORTH')
#             if next_dir == 'WEST' and final_dir.count('EAST') == 0:
#                 final_dir.append(next_dir)
#             elif next_dir == 'WEST' and final_dir.count('EAST') != 0:
#                 final_dir.remove('EAST')
#             if next_dir == 'EAST' and final_dir.count('WEST') == 0:
#                 final_dir.append(next_dir)
#             elif next_dir == 'EAST' and final_dir.count('WEST') != 0:
#                 final_dir.remove('WEST')
#         print(final_dir)

import copy


def dirReduc(arr):
    if len(arr) >= 2:
        i = 0
        arr_b = copy.copy(arr)
        while len(arr) and i <= len(arr)-2:
            first_str = arr[i]
            second_str = arr[i+1]
            if first_str == 'NORTH' and second_str == 'SOUTH':
                arr.pop(i)
                arr.pop(i)
                continue
            elif first_str == 'SOUTH' and second_str == 'NORTH':
                arr.pop(i)
                arr.pop(i)
                continue
            elif first_str == 'WEST' and second_str == 'EAST':
                arr.pop(i)
                arr.pop(i)
                continue
            elif first_str == 'EAST' and second_str == 'WEST':
                arr.pop(i)
                arr.pop(i)
                continue
            else:
                i += 1
        if arr == arr_b:
            # print(arr)
            return arr
        # print(arr)
        return dirReduc(arr)
    elif len(arr) == 1:
        # print(arr)
        return arr
    else:
        # print([])
        return []


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
dirReduc([])
dirReduc(["NORTH"])

