from pathlib import Path

user_name = input("Tell me your name azizam: ")

path = Path('guest.txt')
path.write_text(user_name)
