import string
import random


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    #create key sections
    key_sections = []
    for sections in range(parts):
        one_section = ''.join(random.choice(string.ascii_uppercase + string.digits) for sections in range(chars_per_part))
        key_sections.append(one_section)
    return '-'.join(key_sections)

print(gen_key(parts=3, chars_per_part=4))




"""
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
"""
