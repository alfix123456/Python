''' This application is for a test
'''

#this will be the first fucntion

#in this part we take the variables needed for our program
print("This is a new program")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
currentDate=int(input("Enter The Year today: "))

#The Function to Calculate The Year of Birth
def Date_calculate (a,b):
    dateBorn=b-a
    return dateBorn

#This part is how we get the output to the user
print(name,"you Where Born on",Date_calculate(age,currentDate))
input("Press any key to exit")
