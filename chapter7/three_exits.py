prompt = "Enter your age.\nEnter 'quit' to exit the program. "

user_age = ""
while user_age != 'quit':
    user_age = input(prompt)
    if user_age != 'quit':
        user_age = int(user_age)

        if user_age < 3:
            print("Your ticket is free.\n")
        elif 3 <= user_age < 12:
            print("Your ticket is $10.\n")
        elif user_age >= 12:
            print("Your ticket is $15.\n")


is_running = True
while is_running:
    user_age = input(prompt)
    if user_age == 'quit':
        is_running = False

    else:
        user_age = int(user_age)

        if user_age < 3:
            print("Your ticket is free.\n")
        elif 3 <= user_age < 12:
            print("Your ticket is $10.\n")
        elif user_age >= 12:
            print("Your ticket is $15.\n")


while True:
    user_age = input(prompt)
    if user_age == 'quit':
        break

    user_age = int(user_age)

    if user_age < 3:
        print("Your ticket is free.\n")
    elif 3 <= user_age < 12:
        print("Your ticket is $10.\n")
    elif user_age >= 12:
        print("Your ticket is $15.\n")