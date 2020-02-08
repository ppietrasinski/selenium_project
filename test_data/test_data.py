import names
import random
import string
import pdb

def generte_random_phone_number(number_length=10):
    phone_num = ''
    while len(phone_num) <= number_length:
        phone_num += str(random.randint(0,9))
    return phone_num

def random_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def generate_valid_email(name, last_name):
    return name.lower() + '.' + last_name.lower() + '@ggmail.com'

# random string but with correct email format xxx.yyy@zzz.com
def generate_invalid_email_valid_format(num1=5, num2=10, num3=6):
    return f'{random_generator(num1)}.{random_generator(num2)}@{random_generator(num3)}.{random_generator(random.randint(2,3))}'

name = names.get_first_name()

last_name = names.get_last_name()

phone_number = generte_random_phone_number()

password = random_generator()