from pathlib import Path

def count_common_words(path, word):
    """Returns the number of common words in the text."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} not found.")
    else:
        return contents.lower().count(word)
    
books = ['alice.txt', 'moby.txt', 'romeo.txt']

for book in books:
    path = Path(book)
    print(f"approximate number of 'the' in {path}: {count_common_words(path, 'the ')}")