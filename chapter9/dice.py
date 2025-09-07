from random import randint

class Die:
    """A simple model of a dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die1 = Die()
for i in range(10):
    die1.roll_die()

print("")
die2 = Die(10)
for i in range(10):
    die2.roll_die()

print("")
die3 = Die(20)
for i in range(10):
    die3.roll_die()
