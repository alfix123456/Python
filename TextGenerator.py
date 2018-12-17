"""
This Program will generate random names and in future it will create password lists
"""
import string
import random

def Generator():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    name=letter1+letter2+letter3
    return(name)

print(Generator())

