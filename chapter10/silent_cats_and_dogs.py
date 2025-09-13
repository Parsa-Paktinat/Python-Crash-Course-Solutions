from pathlib import Path

def print_content(path):
    """Read the file and print its content"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        names = contents.split()
        for name in names:
            print(name)

files = ['dogs.txt', 'cats.txt']
for file in files:
    path = Path(file)
    print_content(path)