Parking Lot

    Design a parking lot using Python

Commands

Setup

To create your own ParkingLot :

1.Clone the repository
2.Run python Parking.py on Command Prompt
Description

This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots.

main.py script defines the following functions

create_parking_lot N - Given N number of slots to create a parking lot
park regdno colour - Parks a vehicle with given registration number and color in the empty slot . If there are no more empty slots available, it display a message "Sorry, Parking lot is full".
status - Prints the slot number, registration number and color of the parked vehicles in tabular format.
leave N - Removes vehicle from slot number N
Running the app

To run the app, just open the main.py file on a console like Command Prompt.

Instructions and commands used by the program are as follows:

To create a parking lot, "create_parking_lot " example : create_parking_lot 6

To park a vehicle, "park " example : park KA-01-HH-1234 White

To check status of the parking lot "status"

To remove a car from a slot, "leave " example : leave 4

To get cars of a given color, "registration_numbers_for_cars_with_colour " example : registration_numbers_for_cars_with_colour White

To get slot number of cars with given color, "slot_numbers_for_cars_with_colour " example : slot_numbers_for_cars_with_colour Black

To search slot number of a car on registration number, "slot_number_for_registration_number " example : slot_number_for_registration_number MH-04-AY-1111

To end the program, "exit"