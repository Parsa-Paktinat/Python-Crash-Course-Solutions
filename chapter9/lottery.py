from random import choice

series = [1, 2, 55, 43, 28, 71, 23, 65, 49, 86, 'hello', 'this', 'is', 'Python']
lottery = []

for i in range(4):
    letter_or_number = choice(series)
    lottery.append(letter_or_number)

print("The winner is the person whose lottery ticket has these words:")
for phrase in lottery:
    print(phrase)
