""" This is MultiLane Description
and it is just for fun
not important """
#input data
name=input("Enter your name : ")
age=int(input("Enetr your age: "))
CurrentDate=int(input("Enter the current year: "))

def BirthYear(a,b):
    BirthYear=b-a
    return(BirthYear)

#data output
print(name,"you Have been Born in",BirthYear(age,CurrentDate))
input("Enter a key to exit")
