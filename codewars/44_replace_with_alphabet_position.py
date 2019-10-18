def alphabet_position(text):
    text = text.lower()
    print(' '.join([str(ord(l)-96) for l in text if l.isalpha()]))


alphabet_position("The sunset sets at twelve o' clock.")