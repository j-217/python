# def digital_root(n):
#     """
#     In this kata, you must create a digital root function.
#
#     A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
#
#     Here's how it works:
#
#     digital_root(16)
#     => 1 + 6
#     => 7
#
#     digital_root(942)
#     => 9 + 4 + 2
#     => 15 ...
#     => 1 + 5
#     => 6
#     """
#     str_num = str(n)
#     if len(str_num) > 1:
#         temp_str = ""
#         sum_num = 0
#         print("=>", end="")
#         for i in range(len(str_num)):
#             print("{}+".format(str_num[i]), end="")
#             sum_num += int(str_num[i])
#             temp_str += str_num[i] + ","
#             i += 1
#         print("\n=>{}".format(sum_num))
#         return digital_root(sum_num)
#     else:
#         sum_num = int(str_num)
#     print("=>{}".format(sum_num))
#

def digital_root(n):
    while n >= 10:
        n = sum(map(int, str(n)))
        digital_root(n)
    return n

digital_root(123456)