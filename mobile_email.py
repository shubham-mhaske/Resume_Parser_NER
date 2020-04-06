import re

email_exp = r'\b[\w.-]+?@\w+?\.\w+?\b'
mobile_exp = r'\+?\d[\d -]{8,12}\d'


def get_mobile_email(text):
    email = re.findall(email_exp, text)
    mob = re.findall(mobile_exp, text)
    if len(email) > 0:
        email = email[0]
    if len(mob) > 0:
        mob = mob[0]

    return mob, email
