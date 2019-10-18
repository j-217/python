from math import ceil


def encode_str(strng, shift):
    shifted_str = ''
    prefix_a = strng[0].lower()
    prefix_b = chr(ord(prefix_a) + shift % 26) if ord(prefix_a) + shift % 26 <= 122 else\
        chr(ord(prefix_a) + shift % 26 - 26)
    prefix = prefix_a + prefix_b
    for letter in strng:
        if letter.isalpha() and letter.isupper():
            shifted_str += chr(ord(letter) + shift % 26) if ord(letter) + shift % 26 <= 90 else\
                chr(ord(letter) + shift % 26 - 26)
        elif letter.isalpha() and letter.islower():
            shifted_str += chr(ord(letter) + shift % 26) if ord(letter) + shift % 26 <= 122 else\
                chr(ord(letter) + shift % 26 - 26)
        else:
            shifted_str += letter
    shifted_str = prefix + shifted_str
    n = ceil(len(shifted_str)/5)
    return [shifted_str[:n], shifted_str[n:n*2], shifted_str[n*2:n*3], shifted_str[n*3:n*4], shifted_str[n*4:]] if \
        shifted_str[n*4:] else [shifted_str[:n], shifted_str[n:n*2], shifted_str[n*2:n*3], shifted_str[n*3:n*4]]


def decode(arr):
    prefix = arr[0][:2]
    shifted_str = ''.join(arr)[2:]
    shift = ord(prefix[1]) - ord(prefix[0]) if prefix[1] > prefix[0] else \
        ord(prefix[1]) - ord(prefix[0]) + 26
    strng = ''
    for letter in shifted_str:
        if letter.isalpha() and letter.isupper():
            strng += chr(ord(letter) - shift % 26) if ord(letter) - shift % 26 >= 65 else\
                chr(ord(letter) - shift % 26 + 26)
        elif letter.isalpha() and letter.islower():
            strng += chr(ord(letter) - shift % 26) if ord(letter) - shift % 26 >= 97 else\
                chr(ord(letter) - shift % 26 + 26)
        else:
            strng += letter
    return strng



encode_str("I should have known that you would have a perfect answer for me!!!", 1)