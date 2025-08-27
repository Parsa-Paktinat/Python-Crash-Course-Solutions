class Restaurant:
    """Model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and its cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the attributes of the restaurant."""
        print(f"Restaurant's name:\n\t-{self.restaurant_name}")
        print(f"Restaurant's cuisine type:\n\t-{self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")


rest1 = Restaurant("parsa", "Irani")
rest1.describe_restaurant()

rest2 = Restaurant("shamshiri", "fast food")
rest2.describe_restaurant()

rest3 = Restaurant("Mac donald", "fast food")
rest3.describe_restaurant()