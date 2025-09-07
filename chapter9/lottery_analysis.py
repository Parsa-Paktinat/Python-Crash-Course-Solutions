from random import choice

series = [1, 2, 55, 43, 28, 71, 23, 65, 49, 86, 'hello', 'this', 'is', 'Python']

lottery = []
my_ticket = [2, 43, 'hello', 'is']
counter = 0

while True:
    for i in range(4):
        letter_or_number = choice(series)
        lottery.append(letter_or_number)

    counter += 1
    if lottery == my_ticket:
        print(f"{counter} times the loop had to run to give you a winning ticket.")
        break
    else:
        lottery.clear()
