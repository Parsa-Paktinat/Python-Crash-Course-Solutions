while True:
    number1 = input("Enter your first numebr: ")
    number2 = input("Enter your second numebr: ")

    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print("Sorry, inputs must be numbers.\n")
    else:
        sum = number1 + number2
        print(f"{sum}\n")