sandwich_orders = ['grilled', 'cheese', 'club', 'italian', 'reuben']
finished_sandwiches = []

while sandwich_orders:
    type_of_sandwich = sandwich_orders.pop()
    print (f"I made your {type_of_sandwich} sandwich.")

    finished_sandwiches.append(type_of_sandwich)


print("All the sandwiches have been made. List of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)