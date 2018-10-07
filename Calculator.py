
def calculate():
    options = ["add", "sub", "mult", "div"]
    first_number = ()
    second_number = ()
    for option in options:
        Calc = input("What calculation would you like to do? (add, sub, mult, div) ")
        if Calc == "add":
            first_number = int(input("What is your first number? "))
            second_number = int(input("What is your second number? "))
            result = first_number + second_number
            print (result)
            break
        if Calc == "sub":
            first_number = int(input("What is your first number? "))
            second_number = int(input("What is your second number? "))
            result = first_number - second_number
            print (result)
            break
        if Calc == "mult":
            first_number = int(input("What is your first number? "))
            second_number = int(input("What is your second number? "))
            result = first_number * second_number
            print (result)
            break
        if Calc == "div":
            first_number = int(input("What is your first number? "))
            second_number = int(input("What is your second number? "))
            result == first_number / second_number
            print (result)
            break
        else:
            print("Please try again.")
            calculate
    calculate()
calculate()






    # first_number = int(input("What is your first number? "))
    # second_number = int(input("What is your second number? "))
    # add = first_number + second_number
    # sub = first_number - second_number
    # mult = first_number * second_number
    # div = first_number / second_number

# print (option)

result = ()
