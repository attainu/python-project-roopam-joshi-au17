from vehicle import Vehicle
from prettytable import PrettyTable
import time
import os


class Parking(Vehicle):
    def __init__(self):
        self.capacity = 0
        self.slotId = 0
        self.occupiedSlots = 0

    def createParkingSlot(self, capacity):
        self.capacity = capacity
        self.slots = [-1] * capacity
        return self.capacity

    def empty(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, regno, color):
        if self.occupiedSlots < self.capacity:
            slotId = self.empty()
            self.slots[slotId] = Vehicle(regno, color)
            self.slotId += 1
            self.occupiedSlots += 1
            return slotId + 1
        else:
            return -1

    def status(self):
        x = PrettyTable()
        x.field_names = ["Slot No", "Regd No", "Colour"]
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                x.add_row([i+1, self.slots[i].regno, self.slots[i].color])
        print(x)
        print("\n")

    def leave(self, slotId):
        if self.occupiedSlots > 0 and self.slots[slotId-1] != -1:
            self.slots[slotId-1] = -1
            self.occupiedSlots = self.occupiedSlots - 1
            return True
        else:
            return False

    def getRegdnoByColor(self, color):
        regnos = []
        for i in self.slots:
            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

    def findSlotByRegdno(self, regno):
        for i in range(len(self.slots)):
            if self.slots[i] != -1 and self.slots[i].regno == regno:
                return i+1
            else:
                continue
        return -1

    def findSlotByColor(self, color):
        slotnos = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i+1))
        return slotnos

    def show(self, choice):
        if choice == '1':
            n = int(input("Enter the number of slots you want to make:"))
            res = self.createParkingSlot(n)
            print(f"Created a parking lot with {res} slots\n")

        elif choice == '2':
            regno = input("Enter the Registration number: ")
            color = input("Enter the color of the vehicle: ").lower()
            res = self.park(regno, color)
            if res == -1:
                print("Sorry, Parking lot is full\n")
            else:
                print(f"Allocated slot number : {res}\n")

        elif choice == '3':
            self.status()

        elif choice == '4':
            slotId = int(input("Enter the slot id: "))
            status = self.leave(slotId)
            if status:
                print(f"Slot number {slotId} is free\n")

        elif choice == '5':
            color = input("Enter the color of the vehicle: ").lower()
            regnos = self.getRegdnoByColor(color)
            print(', '.join(regnos))
            print("\n")

        elif choice == '6':
            regno = input("Enter the registration number: ")
            slotno = self.findSlotByRegdno(regno)
            if slotno == -1:
                print("Not found")
                print("\n")
            else:
                print(slotno)
                print("\n")

        elif choice == '7':
            color = input("Enter the colour of the vehicle: ").lower()
            slotnos = self.findSlotByColor(color)
            print(', '.join(slotnos))
            print("\n")

        elif choice == '8':
            exit(0)
        time.sleep(5)
        os.system("cls")
parking = Parking()
