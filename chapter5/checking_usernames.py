current_users = ['parsa', 'saeid', 'king12345432', 'majid', 'hasan', 'admin']
new_users = ['parsa', 'John', 'micheal', 'Franklin', 'Sara']

current_users_lowercase = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print("This username is alredy exist. Make a new one!")
    else:
        print("This username is available.")
