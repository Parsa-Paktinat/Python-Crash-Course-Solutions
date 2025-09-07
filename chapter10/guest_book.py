from pathlib import Path

names = ''
while True:
    name = input('Tell me your name azizam: \nYou can type "q" for quiting. ')
    if name == 'q':
        break
    names += name
    names += '\n'

path = Path('guest_book.txt')
path.write_text(names)
