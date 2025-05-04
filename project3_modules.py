def only_int(a):
    if a.isdigit()==True:
            return int(a)
    
    while type(a)!=int:
        print("Wrong input..")
        a = input("Enter again:")
        if a.isdigit()==True:
            return int(a)


def only_str(a):
    if a.isalpha()==True:
            return a
    else:
        while a.isalpha()==False:
            print("Wrong input..")
            a = input("Enter again:")
            if a.isalpha()==True:
                return a

def date_input():
    while True:
        date = input("Enter date in the format: DD-MM-YYYY): ")
        try:
            parsed_date = datetime.strptime(date, "%d-%m-%Y")
            print("Parsed date:", parsed_date)
            break
        except ValueError:
            print("Invalid date format. Please use the format: DD-MM-YYYY")
    return parsed_date