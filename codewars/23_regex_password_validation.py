import re


def password_validation(passwd):
    re.compile(r"(?=.*\d+)(?=.*[a-z]+)(?=.*[A-Z]+)^\w{6,}$")