def rot_90_clock(strng):
    return map(list, zip(*strng[::-1]))


def diag_1_sym(strng):
    return map(list, zip(*strng))


def selfie_and_diag1(strng):
    diag = diag_1_sym(strng)
    symbol_lst = [['|'] * len(strng)]
    return map(list, zip(*diag, *symbol_lst, *strng))


def oper(fct, s):
    array = []
    for line in s.splitlines():
        letter_lst = []
        for letter in line:
            letter_lst.append(letter)
        array.append(letter_lst)
    print('\n'.join(map(''.join, fct(array))))


