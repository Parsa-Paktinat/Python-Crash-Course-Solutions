def make_shirt(shirt_size="L", shirt_text="I love Python"):
    """Print size of shirt and text on it"""
    print(f"\nSize of the shirt is {shirt_size}.")
    print(f"This message '{shirt_text}' should be printed on it.")

make_shirt()
make_shirt("M")
make_shirt("S", "Vim is cool")