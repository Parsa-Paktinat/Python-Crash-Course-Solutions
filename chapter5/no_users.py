usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, welcome back. Would you like to see the reports?")
        else:
            print(f"Hello {username}, welcome back.")
else:
    print("We need to find some users!")
