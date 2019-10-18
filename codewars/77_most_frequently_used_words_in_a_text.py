import re


def top_3_words(text):
    lst = []
    pattern = re.compile(r"[']?[a-z]+[']?[a-z]*")
    t_lst = re.findall(pattern, text.lower())
    print(t_lst)
    if not t_lst:
        return t_lst
    for word in set(t_lst):
        lst.append((word, t_lst.count(word)))
    lst.sort(key=lambda x: (-x[1], x[0]))
    lst = lst[:3] if len(lst) >= 3 else lst
    print(lst)
    return [x[0] for x in lst]


top_3_words("  '  ")
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
top_3_words("  //wont won't won't ")
