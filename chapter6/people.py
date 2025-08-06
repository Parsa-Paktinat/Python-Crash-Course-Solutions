person1 = {
    'first_name': 'parsa',
    'last_name': 'paktinat',
    'age': 19,
    'city': 'Yazd'
}
person2 = {
    'first_name': 'Majid',
    'last_name': 'Majidi',
    'age': 70,
    'city': 'Tehran'
}
person3 = {
    'first_name': 'Hasan',
    'last_name': 'Zare',
    'age': 19,
    'city': 'Yazd'
}

people = [person1, person2, person3]

for person in people:
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")