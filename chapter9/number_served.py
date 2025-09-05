class Restaurant:
    """Model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and its cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the attributes of the restaurant."""
        print(f"Restaurant's name:\n\t-{self.restaurant_name}")
        print(f"Restaurant's cuisine type:\n\t-{self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, new_number):
        """Set the number of customers that you have served."""
        self.number_served = new_number

    def increment_number_served(self, num):
        """Increment the number of served customers."""
        self.number_served += num


restaurant = Restaurant("parsa", "Irani")
print(restaurant.number_served)

restaurant.number_served = 12
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(18)
print(f"{restaurant.number_served} customers were served in a day of business.")