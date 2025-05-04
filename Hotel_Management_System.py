from project3_modules import *
from project3_classes import *


while True:
    print("             *********WELCOME TO RADISSON BLUE HOTEL**********")
    print("1. Enter Customer Data")
    print("2. Calculate Room Rent")
    print("3. Calculate Restaurant Bill")
    print("4. Calculate Laundary Bill")
    print("5. Calculate Game Bill")
    print("6. Show Total Cost")
    print("7. Show Guest details")
    print("8. Exit")

    n = only_int(input("Enter your choice:"))
    
    if n ==1:
        guest = Guest()
        print("-"*62)
    elif n==2:
        room_number =only_int(input("Enter your room number:"))
        rent = Guest.room_rent(room_number)
        if rent:
            print("Your total room rent is:", rent)
        else:
            print("Invalid room number. Please try again")
        print("-"*62)
    elif n==3:
        room_number =only_int(input("Enter your room number:"))
        try:
            Guest.guests_details[room_number]
            print("Your hotel bill is = ",Hotel.restaurant_bill(room_number))
        except KeyError:
            print("Invalid room number. Please try again")
        print("-"*62)
    elif n==4:
        room_number =only_int(input("Enter your room number:"))
        try:
            Guest.guests_details[room_number]
            print("Your laundary bill is = ",Hotel.laundary_bill(room_number))
        except KeyError:
            print("Invalid room number. Please try again")
        print("-"*62)
    elif n==5:
        room_number =only_int(input("Enter your room number:"))
        try:
            Guest.guests_details[room_number]
            print("Your hotel bill is = ",Hotel.game_bill(room_number))
        except KeyError:
            print("Invalid room number. Please try again")
        print("-"*62)
    elif n==6:
        room_number =only_int(input("Enter your room number:"))
        try:
            Guest.guests_details[room_number]
            print("Your total bill is = ",Guest.total_bill(room_number))
        except KeyError:
            print("Invalid room number. Please try again")
        print("-"*62)
    elif n==7:
        Guest.guest_details()
        print("-"*62)
    elif n==8:
        exit()
    else:
        print("Wrong choice.")
