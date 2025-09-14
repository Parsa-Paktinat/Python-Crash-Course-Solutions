from pathlib import Path
import json

# Writing to file section
user_dictionary_dump = {}

username = input("What is your username? ")
age = int(input("What is your age? "))
city = input("What is your city? ")

user_dictionary_dump['username'] = username
user_dictionary_dump['age'] = age
user_dictionary_dump['city'] = city

for key, value in user_dictionary_dump.items():
    print(f"I remembered your {key}. It's '{value}'.")

# Reading from file section
write_path = Path('user_dictionary.json')
contents = json.dumps(user_dictionary_dump)
write_path.write_text(contents)

read_path = Path('user_dictionary.json')
readed_contents = read_path.read_text()
user_dictionary_readed = json.loads(readed_contents)

for key, value in user_dictionary_readed.items():
    print(f"I know your {key}. It's '{value}'.")