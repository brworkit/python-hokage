import re

def is_valid_email(email, regex):
    if email is None:
        return False
    if not isinstance(email, str):
        return False
    if email.strip() == "":
        return False
    return re.search(regex, email.lower())
