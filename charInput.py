from datetime import date
def get_info():
    #get name and age of user
    name = input("Please enter your name ")
    age = input("Please enter your age ")
    return name, age

def calc_age(x):
    
    years = 100 - int(x)
    curr_year = date.today().year
    yr100 = int(curr_year) + int(years)
    return yr100

def print_message():
    values = get_info()
    #stores name and age in variable values
    print("Hi " + values[0])
    yr100 = calc_age(values[1])
    print("In " + str(yr100) + " you will be 100!")

print_message()
