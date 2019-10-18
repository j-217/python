def high_and_low(numbers):
    list_num = sorted(list(map(int, numbers.split(" "))))
    # print(sorted(list(map(int, numbers.split(" ")))))
    max_num = list_num[len(list_num) - 1]
    min_num = list_num[0]
    numbers = str(max_num) + " " + str(min_num)
    return numbers
    # print(numbers)

high_and_low("-10 9 8 7 6 5")