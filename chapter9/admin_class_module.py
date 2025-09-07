from user_class_module import User

class Admin(User):
    """Admin is a special user."""

    def __init__(self, first_name, last_name, email, age, password):
        """Initialize Admin class."""
        super().__init__(first_name, last_name, email, age, password)
        self.privileges = Privileges('can add post', 'can delete post', 'can ban user')


class Privileges:
    """A class for privileges"""

    def __init__(self, *privileges_list):
        """Initialize Privileges class"""
        self.privileges = []
        for privilege in privileges_list:
            self.privileges.append(privilege)

    def show_privileges(self):
        """Display the privileges."""
        print("Admin's privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}.")

