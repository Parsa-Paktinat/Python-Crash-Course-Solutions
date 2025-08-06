favorite_places = {
    'Parsa': ['Venice', 'Rome', 'Florance'],
    'Ali': ['Amsterdam', 'Vancour', 'paris'],
    'Hassan': ['Madine', 'Make', 'Karbala']
}

for person, cities in favorite_places.items():
    print(f"{person.title()} wants to go to these cities:")
    for city in cities:
        print("\t"+city)
