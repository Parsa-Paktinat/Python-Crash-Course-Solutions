while True:
    user_age = input("Enter your age: ")
    user_age = int(user_age)

    if user_age < 3:
        print("Your ticket is free.\n")
    elif 3 <= user_age < 12:
        print("Your ticket is $10.\n")
    elif user_age >= 12:
        print("Your ticket is $15.\n")