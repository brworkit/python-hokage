import re

CASES = [' ', ";", ","]

def is_valid_email(email, regex):
    if email is None:
        return False
    if not isinstance(email, str):
        return False
    if email.strip() == "":
        return False
    for case in CASES:
        if case in email:
            return False
    return re.search(regex, email.lower())
