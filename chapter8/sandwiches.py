def sandwich_toppings(*toppings):
    """Print a summary of the sandwich that's being ordered."""
    print("Toppings of sandwich:")
    for topping in toppings:
        print(f"- {topping}")

sandwich_toppings("tomato")
sandwich_toppings("tomato", "lettuce")
sandwich_toppings("tomato", 'lettuce', 'pickles', 'sauce')
