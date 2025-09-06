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


class IceCreamStand(Restaurant):
    """A simple attempt to model a ice cream stand."""

    def __init__(self, ice_cream_stand_name, cuisine_type):
        """Initilize the ice cream stand name and its cuisine"""
        super().__init__(ice_cream_stand_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate', 'cantaloupe']

    def display_flavors(self):
        """Display flavors of the ice cream stand."""
        for flavor in self.flavors:
            print(f"{self.restaurant_name}'s ice cream stand has {flavor} ice cream.")


ice_cream_stand = IceCreamStand("Parsa", "Ice cream")
ice_cream_stand.display_flavors()
