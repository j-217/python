import re


def alphanumeric(string):
    pattern = re.compile(r'[a-zA-Z0-9]+')
    print(re.fullmatch(pattern, string))
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


alphanumeric("PassW0rd")