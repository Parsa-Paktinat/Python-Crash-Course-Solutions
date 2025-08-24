sandwich_orders = ['grilled', 'pastrami', 'cheese', 'club', 'pastrami', 'italian', 'pastrami', 'reuben', 'pastrami']
finished_sandwiches = []
print("Deli has run out of pastrami")

pastrami = 'pastrami'
while pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami)

while sandwich_orders:
    type_of_sandwich = sandwich_orders.pop()
    print (f"I made your {type_of_sandwich} sandwich.")
    finished_sandwiches.append(type_of_sandwich)

print("All the sandwiches have been made. List of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
