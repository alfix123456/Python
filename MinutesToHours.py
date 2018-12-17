print("This Program Will Help you Calculate Hours!")
def MinuteToHours(minutes):
    hours = minutes / 60
    return hours

_minutes=input("Enter Total Minutes: ")
print(MinuteToHours(float(_minutes)))
