def sum_two_smallest_numbers(numbers):
    list = sorted(numbers)
    sum_number = list[0] + list[1]
    print(sum_number)


sum_two_smallest_numbers([5, 8, 12, 18, 22])