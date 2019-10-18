def narcissistic(value):
    # str_num = str(value)
    # sum_num = 0
    # for x in str_num:
    #     sum_num += int(x)**len(str_num)
    # if sum_num == value:
    #     return True
    #     # print("True")
    # else:
    #     return False
    #     # print("False")
    str_num = str(value)
    sum_num = sum(int(x)**len(str_num) for x in str_num)
    print(sum_num)

narcissistic(153)