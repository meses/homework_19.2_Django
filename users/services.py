import random
import string


def generate_code():
    random.seed()
    return str(random.randint(10000, 99999))

def generate_password():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(8))