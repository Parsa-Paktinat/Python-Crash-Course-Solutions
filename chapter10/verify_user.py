from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def store_username(path):
    """Store username in path."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"The current username is: {username}")
        is_correct_user = input('Is this your username? (y/n) ')
        if is_correct_user == 'y':
            print(f"welcome back, {username}!")
        elif is_correct_user == 'n':
            username = store_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = store_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()