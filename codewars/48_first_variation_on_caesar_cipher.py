from math import ceil


def moving_shift(s, shift):
    shifted_s = ''
    for letter in s:
        if letter.isalpha() and letter.isupper():
            shifted_s += chr(ord(letter) + shift % 26) if ord(letter) + shift % 26 <= 90 else \
                chr(ord(letter) + shift % 26 - 26)
            shift += 1
        elif letter.isalpha() and letter.islower():
            shifted_s += chr(ord(letter) + shift % 26) if ord(letter) + shift % 26 <= 122 else \
                chr(ord(letter) + shift % 26 - 26)
            shift += 1
        else:
            shifted_s += letter
            shift += 1
    n = ceil(len(s)/5)
    lst = [shifted_s[:n]] + [shifted_s[n:2*n]] + [shifted_s[2*n:3*n]] + [shifted_s[3*n:4*n]] + [shifted_s[4*n:]]
    print(n)
    print(lst)
    return lst


def demoving_shift(s, shift):
    unshift_s = ''
    s = ''.join(string for string in s)
    for letter in s:
        if letter.isalpha() and letter.isupper():
            unshift_s += chr(ord(letter) - shift % 26) if ord(letter) - shift % 26 >= 65 else \
                chr(ord(letter) - shift % 26 + 26)
            shift += 1
        elif letter.isalpha() and letter.islower():
            unshift_s += chr(ord(letter) - shift % 26) if ord(letter) - shift % 26 >= 97 else \
                chr(ord(letter) - shift % 26 + 26)
            shift += 1
        else:
            unshift_s += letter
            shift += 1
    return unshift_s


moving_shift("I should have known that you would have a perfect answer for me!!!", 1)