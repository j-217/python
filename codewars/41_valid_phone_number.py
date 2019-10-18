import re


def validPhoneNumber(phoneNumber):
    pattern = re.compile(r'\(\d{3}\)\s{1}\d{3}-\d{4}')
    return True if re.match(pattern, phoneNumber) is not None else False