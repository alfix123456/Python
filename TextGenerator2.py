"""
This Program will generate random names and in future it will create password lists
"""
import string
import random

vowels='aeiou'
Consonants='bcdfghjklmnpqrstvwxyz'

letterInput_1=input("V for wovel, C for Consonants, L for any other letter: ")
letterInput_2=input("V for wovel, C for Consonants, L for any other letter: ")
letterInput_3=input("V for wovel, C for Consonants, L for any other letter: ")

#print(letterInput_1+letterInput_2+letterInput_3)


def Generator():
    if letterInput_1=='v':
        letter1=random.choice(vowels)
    elif letterInput_1=="c":
        letter1=random.choice(Consonants)
    elif letterInput_1=="l":
        letter1=random.choice(string.ascii_lowercase)
    else:
        letter1=letterInput_1

    if letterInput_2=='v':
        letter2=random.choice(vowels)
    elif letterInput_2=="c":
        letter2=random.choice(Consonants)
    elif letterInput_2=="l":
        letter2=random.choice(string.ascii_lowercase)
    else:
        letter2=letterInput_2

    if letterInput_3=='v':
        letter3=random.choice(vowels)
    elif letterInput_3=="c":
        letter3=random.choice(Consonants)
    elif letterInput_3=="l":
        letter3=random.choice(string.ascii_lowercase)
    else:
        letter3=letterInput_3
    name=letter1+letter2+letter3



    return(name)

for  i in range(20):
    print(Generator())

