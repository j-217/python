def accum(s):
    """
    This time no story, no theory. The examples below show you how to write function accum:

    Examples:

    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"

    The parameter of accum is a string which includes only letters from a..z and A..Z.
    """
    str = ""
    list = []
    for i in range(0, len(s)):
        j = i
        word = s[i].upper()
        while j > 0:
            word += s[i].lower()
            j -= 1
        list.append(word)
    str = "-".join(list)
    # print(str)
    return str

accum("abCd")