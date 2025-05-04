import datetime
from project3_modules import *

class Hotel:
    rooms = {i:True for i in range(1,101)}
    room_types={"Type_A":{"cost":6000, "availability":2},
                "Type_B":{"cost":5000, "availability":2},
                "Type_C":{"cost":4000, "availability":2},
                "Type_D":{"cost":3000, "availability":2}}
    
    def __init__(self, name="Radisson Blue Hotel"):
        self.name = name
        
    def game_bill(room_number):
        print("*******GAME MENU*******")
        print (" 1. Table Tennis => 60$\n","2. Bowling      => 80$\n","3. Snooker      => 70$\n","4. Video Games  => 90$\n","5. Pool         => 50$\n","6. Exit\n")
        total_bill = 0
        while True:
            item = only_int(input("Choose option (eg; for Table Tennis, enter 1):"))
            if item ==6:
                break
            elif item <6:
                quantity = only_int(input(f"Enter number of hours of game play {item}:"))
                if item ==1:
                    total_bill += 60*quantity
                elif item ==2:
                    total_bill += 80*quantity
                elif item ==3:
                    total_bill += 70*quantity
                elif item == 4:
                    total_bill += 90*quantity
                elif item == 5:
                    total_bill += 50*quantity
            else:
                print("Invalid input")
        Guest.guests_details[room_number]["Game_bill"] += total_bill
        return total_bill
        
    def laundary_bill(room_number):
        print("*******LAUNDARY MENU*******")
        print(" 1. Shorts   => 5$\n", "2. Trousers => 15$\n","3. Shirt    => 10$\n","4. Jeans    => 10$\n","5. Girlsuit => 100$\n","6. Exit\n")

        total_bill = 0
        while True:
            item = only_int(input("Choose option (eg; for Shorts, enter 1):"))
            if item ==6:
                break
            elif item <6:
                quantity = only_int(input(f"Enter quantity of item {item}:"))
                if item ==1:
                    total_bill += 5*quantity
                elif item ==2:
                    total_bill += 15*quantity
                elif item ==3:
                    total_bill += 10*quantity
                elif item == 4:
                    total_bill += 10*quantity
                elif item == 5:
                    total_bill += 100*quantity
            else:
                print("Invalid input")
        Guest.guests_details[room_number]["Laundary_bill"] += total_bill
        return total_bill
                
    def restaurant_bill(room_number):
        print("*******RESTAURANT MENU*******")
        print(" 1. Water Bottle   => 20$\n","2. Tea            => 10$\n","3. Breakfast Combo=> 90$\n","4. Lunch          => 110$\n","5. Dinner         => 150$\n","6. Exit\n")
        total_bill = 0
        while True:
            item = only_int(input("Choose option (eg; for Water Bottle, enter 1):"))
            if item ==6:
                break
            elif item <6:
                quantity = only_int(input(f"Enter quantity of item {item}:"))
                if item ==1:
                    total_bill += 20*quantity
                elif item ==2:
                    total_bill += 10*quantity
                elif item ==3:
                    total_bill += 90*quantity
                elif item == 4:
                    total_bill += 110*quantity
                elif item == 5:
                    total_bill += 150*quantity
            else:
                print("Invalid input")
        Guest.guests_details[room_number]["Restaurant_bill"] += total_bill
        return total_bill
    @classmethod
    def room_rent(cls):
        print("******WE HAVE DIFFERENT TYPES OF ROOM******")
        for i in Hotel.room_types:
            print(f'{i} => {Hotel.room_types[i]["cost"]}$')
            
        room_type = input("Select your room type (eg; enter A for Type_A):")
        if room_type=="A" or room_type=="a":
            if Hotel.room_types["Type_A"]["availability"] >0:
                print("Congratulation! your room is availale..")
                Hotel.room_types["Type_A"]["availability"]-=1
                return Hotel.room_types["Type_A"]["cost"]
            else:
                return None
        elif room_type=="B" or room_type=="b":
            if Hotel.room_types["Type_B"]["availability"] >0:
                print("Congratulation! your room is availale..")
                Hotel.room_types["Type_B"]["availability"]-=1
                return Hotel.room_types["Type_B"]["cost"]
            else:
                return None
        elif room_type=="C" or room_type=="c":
            if Hotel.room_types["Type_C"]["availability"]>0:
                print("Congratulation! your room is availale..")
                Hotel.room_types["Type_C"]["availability"]-=1
                return Hotel.room_types["Type_C"]["cost"]
            else:
                return None
        elif room_type=="D" or room_type=="d":
            if Hotel.room_types["Type_D"]["availability"]>0:
                print("Congratulation! your room is availale..")
                Hotel.room_types["Type_D"]["availability"]-=1
                return Hotel.room_types["Type_D"]["cost"]
            else:
                return None
class Guest:
    guests_details = {}
    def __init__(self):
        for i in Hotel.rooms:
            if Hotel.rooms[i] ==True:
                self.cdate = datetime.date.today()
                self.name = input("Enter your name:")
                self.address = input("Enter your address:")
                self.cost = Hotel.room_rent()
                self.days = only_int(input("Enter number of days to book this room:")) 
                if self.cost:
                    Guest.guests_details[i]={"Name":self.name, "Address":self.address,
                                        "Entry_date":self.cdate, "Room_rent":self.cost*self.days,
                                             "Restaurant_bill":0, "Laundary_bill":0,
                                             "Game_bill":0}
                    Hotel.rooms[i] =False
                    print("Details are added, alloted room number is:", i)
                    break
                else:
                    print("Sorry, no rooms available of this type.")
                    break
        else:
            print("Sorry, there is no empty room in the hotel..")
    @classmethod
    def guest_details(cls):
        cls.room_number = only_int(input("Enter your room number:"))
        for i in Guest.guests_details:
            if i ==cls.room_number:
                for j,k in Guest.guests_details[i].items():
                    print(f'{j} => {k}')
                else:
                    break
        else:
            print("Invalid room number")

    def room_rent(room_number):
        try:
            rent = Guest.guests_details[room_number]["Room_rent"]
            return rent
        except KeyError:
            return None

    def total_bill(room_number):
        bill = Guest.guests_details[room_number]["Room_rent"]+Guest.guests_details[room_number]["Restaurant_bill"]+Guest.guests_details[room_number]["Laundary_bill"]+Guest.guests_details[room_number]["Game_bill"]
        return bill        
