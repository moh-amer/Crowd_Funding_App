import re

def is_valid_email(email):
    mailregex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return len(email) and re.fullmatch(mailregex, email)
