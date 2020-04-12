def get_number():
    number = input("Please enter a number to find out if it is even or odd: ")
    return number

def evaluation():
    num_to_eval = get_number()
    if int(num_to_eval) % 4 == 0:
        print("Your number is divisible by 4")
    else:
        pass
    if int(num_to_eval) % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
    
evaluation()
