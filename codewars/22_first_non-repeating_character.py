# def first_non_repeating_letter(string):
#     str = string.lower()
#     # 不区分大小写
#     for i in str:
#         if len(str.split("{}".format(i)) - 1 == 1:
#             # 遍历str，如果该字母将str分为两份，说明该字母只出现一次
#             return string[str.find(i)]
#     return None

def first_non_repeating_letter(string):
    str = string.lower()
    for i, letter in enumerate(str):
        if len(str.split(letter)) == 2:
            return string[i]
    return ""
