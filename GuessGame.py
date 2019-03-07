import random
randomNumber=random.randint(0,10)
guessCount=0
guessLimit=3
while guessCount< guessLimit:
    guess=int(input("Guess a number: "))
    guessCount +=1
    if guess==randomNumber:
        print("You Won!")
        break
else:
    print("You lost!")
