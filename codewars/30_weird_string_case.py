def to_weird_case(string):
    lst = string.split(' ')
    change_lst = []
    for word in lst:
        change_lst.append(change_word(word))
    return " ".join(word for word in change_lst)

def change_word(word):
    c_word = ''
    for i in range(len(word)):
        if i % 2 == 0:
            c_word += word[i].upper()
        else:
            c_word += word[i].lower()
    return c_word


to_weird_case('should return the correct value for a single word')
