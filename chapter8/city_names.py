def city_country(city_name, country_name):
    """Returns the city name and its country."""
    city_and_country = f"{city_name}, {country_name}"
    return city_and_country.title()

print (city_country("Yazd","iran"))
print (city_country("paris", "france"))
print (city_country("chicago", "the United States"))