# def lcs(x, y):
#     short_str = x if len(x) <= len(y) else y
#     long_str = x if short_str is y else y
#     common_str = ""
#     for i in range(0, len(short_str)):
#         if short_str[i] in long_str:
#             common_str += short_str[i]
#         else:
#             continue
#     print(common_str)
#     # return common_str


# def lcs(x, y):
#     common_str = ""
#     for y_index in range(0, len(y)):
#         # 遍历子列表y
#         x_index = x.find(y[y_index])
#         # 在父列表x中查看是否包含子列表y的字母
#         if x_index == -1:
#             # 未找到返回-1，继续查找子列表下一字母
#             continue
#         elif x_index == len(x) - 1:
#             # 如果找到的字母在父列表最后一位，添加至共通列表并退出循环
#             common_str += y[y_index]
#             break
#         else:
#             # 如果找到的字母并且未达到父列表的最后一位，根据找到的字母将父列表切片，继续查找
#             common_str += y[y_index]
#             x = x[x_index:]
#     print(common_str)
#     # return common_str

def lcs(x, y):
    common_str = ""
    for y_index in range(0, len(y)):
        # 遍历子列表y
        x_index = x.find(y[y_index])
        # 在父列表x中查看是否包含子列表y的字母
        if x_index == -1:
            # 未找到返回-1，继续查找子列表下一字母
            continue
        elif x_index <= len(x) - 1:
            common_str += y[y_index]
            x = x[x_index + 1:]
    print(common_str)
    # return common_str


lcs('a', 'b')
lcs("abcdef", "abc")
lcs("anothertest", "notatest")
lcs("132535365", "123456789")
lcs("abcdefgx", "xax")