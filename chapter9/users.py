class User:
    """Model a user."""

    def __init__(self, first_name, last_name, email, age, password):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.password = password

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"name: {self.first_name.title()} {self.last_name.title()}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"password: {self.password}\n")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. What's your main goal today?\n")

user1 = User("parsa", "paktinat", "parsapaktinat63@gmail.com", 18, "1234rewq")
user2 = User("Hassan", "shamaei-zade", "hassan@gmail.com", 70, "12345678")
user3 = User("Alinaghi", "vaziri", "alivaz@yahoo.com", 105, "taramobederefigh")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()