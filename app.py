command = ""
while True:
    command=input(">").lower()
    if command=="start":
        print("Car started...")
    elif command == "stop":
        print("Car Stopped...")
    elif command == "help":
        print("""
        Start - to start the car
        Stop - to stop the car
        Quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand that!")
