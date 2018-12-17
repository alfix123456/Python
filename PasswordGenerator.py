"""
    This Program will generate passwordfiles
    Created by SomeOne
"""
import random
import string

def Generator():
    letter=random.choice(string.ascii_letters)
    return(letter)

passlength=input("Enter The number of letters in your password: ")
passCount=input("Enter the number of Passwords You Want: ")
for j in range(int(passCount)):
    password=""
    for i in range(int(passlength)):
        password=password+Generator()
    print(password)