places = {}

is_polling = True
while is_polling:
    name = input("Enter your name: ")
    place = input("If you could visit one place in the world, where would you go?: ")

    places[name] = place

    repeat = input("Would you like to let another person to respond? (y/n) ")
    if repeat == 'n':
        is_polling = False


print("/n--- Poll Results ---")
for name, place in places.items():
    print(f"{name.title()} would like to go to {place.title()}.")
