class User:
    """Model a user."""

    def __init__(self, first_name, last_name, email, age, password):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"name: {self.first_name.title()} {self.last_name.title()}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"password: {self.password}\n")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. What's your main goal today?\n")

    def increment_login_attempts(self):
        """Increment login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login_attempts to 0"""
        self.login_attempts = 0

class Admin(User):
    """Admin is a special user."""

    def __init__(self, first_name, last_name, email, age, password):
        """Initialize Admin class."""
        super().__init__(first_name, last_name, email, age, password)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the privileges."""
        print("Admin's privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}.")


admin1 = Admin("Parsa", "Paktinat", "parsapaktinat63@gmail.com", "19", "helloworld")
admin1.show_privileges()
