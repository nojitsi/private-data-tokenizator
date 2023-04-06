import random
import string

def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

