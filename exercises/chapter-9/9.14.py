"""
9-14. Dice: 
The module random contains functions that generate random numbers in a variety 
of ways. The function randint() returns an integer in the range you provide. 
The following code returns a number between 1 and 6: 

from random import randint 
x = randint(1, 6)

Make a class Die with one attribute called sides, which has a default value of 
6. Write a method called roll_die() that prints a random number between 1 and 
the number of sides the die has. Make a 6-sided die and roll it 10 times. Make 
a 10-sided die and a 20-sided die. Roll each die 10 times. 
"""

from random import randint


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides):
        """Initialize sides attribute."""
        super().__init__()
        self.sides = sides

    def roll(self):
        """Displays a random number on the dice."""
        print(randint(1, self.sides))


die6 = Die(6)
for i in range(10):
    die6.roll()

die10 = Die(10)
for i in range(10):
    die10.roll()

die20 = Die(20)
for i in range(20):
    die20.roll()
