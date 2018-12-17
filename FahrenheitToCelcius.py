#This Program Concerts Fahrenheit Degrees to Celcius Degrees

def FahrToCelc(__FarDeg):
    __newCelcDegree=(__FarDeg-32)*5/9
    return __newCelcDegree

__farDeg=float(input("Please Enter The Farenheit Degree: "))

if __farDeg<-273:
    print("This Value is not Valid, at least on Earth!")
else:
    print(FahrToCelc(__farDeg),"Degrees Celcius")
