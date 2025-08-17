def car_info(manufacturer, model_name, **info):
    """Build a dictionary about a car."""
    info['manufacturer'] = manufacturer
    info['model_name'] = model_name
    return info

car = car_info('subaru', 'outback', color='blue', two_package=True)
print(car)
