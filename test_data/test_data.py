import names
import random
import string

def generte_random_phone_number(number_length=10):
    phone_num = ''
    while len(phone_num) <= number_length:
        phone_num += str(random.randint(0,9))
    return phone_num

def random_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

name = names.get_first_name()

last_name = names.get_last_name()

phone_number = generte_random_phone_number()

valid_email = name.lower() + '.' + last_name.lower() + '@ggmail.com'

password = random_generator()