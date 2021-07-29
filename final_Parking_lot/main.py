from parking import parking
from art import logo
while True:
    print(logo)
    print("PLEASE SELECT BELOW MENU")
    print("1. CREATE PARKING LOT")
    print("2. PARK YOUR VEHICLE")
    print("3. CHECK STATUS")
    print("4. FREE UP THE SLOT")
    print("5. CHECK REGISTRATION NUMBER OF VEHICLE USING COLOUR ")
    print("6. CHECK SLOT NUMBER OF VEHICLE USING REG.NO.")
    print("7. CHECK SLOT NUMBER OF VEHICLE USING COLOUR")
    print("8. EXIT APPLICATION")
    choice = input()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8':
        parking.show(choice)
    else:
        print("Please enter valid input")
