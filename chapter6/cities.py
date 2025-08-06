cities = {
    'Venice': {
        'country': 'Italy',
        'pop': 2000_000,
        'fact': "old city"
    },

    'Tehran': {
        'country': 'Iran',
        'pop': 20_000_000,
        'fact': "Cpital of iran"
    },

    'Mashhad': {
        'country': 'Iran',
        'pop': 5_000_000,
        'fact': "Holy shrine in it"
    }
}

for city_name, info in cities.items():
    print(city_name.title() + ":")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")