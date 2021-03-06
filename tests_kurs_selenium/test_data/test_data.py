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

def random_lower_case_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def generate_valid_email(name, last_name):
    return name.lower() + '.' + last_name.lower() + '@ggmail.com'

# random string but with correct email format xxx.yyy@zzz.com
def generate_invalid_email_valid_format(num1=5, num2=10, num3=6):
    return f'{random_lower_case_generator(num1)}.{random_lower_case_generator(num2)}@{random_lower_case_generator(num3)}.{random_lower_case_generator(random.randint(2,3))}'

def login_time(time1, time2):
    print(f'{time2 - time1} time needed to login to my account')

def generate_all_data():
    name = names.get_first_name()
    last_name = names.get_last_name()
    full_name = name + ' ' + last_name
    email = generate_valid_email(name, last_name)
    return {
        "name": name,
        "last name": last_name,
        "full name": full_name,
        "email": email
    }

name = names.get_first_name()

last_name = names.get_last_name()

full_name = name + ' ' + last_name

phone_number = generte_random_phone_number()

password = random_generator()