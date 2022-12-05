import random
import string


def generate_random_code():
    length_of_random_code = 6
    random_code = ''.join(random.choices(
        string.ascii_letters, k=length_of_random_code))
    print('random_code', random_code)
    return random_code


the_random_code = generate_random_code()
print(the_random_code)
