def show_messages(messages):
    """Displays the messages"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Display each message and move it to the sent messages"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = [
    "Hello world",
    "Do your job",
    "Be happy",
    "Be normal"
]
sent_messages = []

print("messages:")
show_messages(messages)
print("")

send_messages(messages, sent_messages)

print("\nmessages:")
show_messages(messages)
print("\nsent messages:")
show_messages(sent_messages)
