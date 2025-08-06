rivers = {
    'nile': 'egypt',
    'Volga': 'russia',
    'danube': 'germany'
}

for key, value in rivers.items():
    print (f"The {key.title()} runs through {value.title()}.")

for river_name in rivers.keys():
    print (river_name)

for country in rivers.values():
    print (country)
