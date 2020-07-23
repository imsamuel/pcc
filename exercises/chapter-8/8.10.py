"""
8-10. Great Magicians: 
Start with a copy of your program from Exercise 8-9. Write a function called 
make_great() that modifies the list of magicians by adding the phrase the Great 
to each magician’s name. Call show_magicians() to see that the list has 
actually been modified.
"""


def show_magicians(magicians):
    """Display each magician from the given list of magicians."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Transform the given magicians into great magicians."""
    return list(map((lambda magician: magician + " the Great"), magicians))


magicians = ["David Blaine", "David Copperfield"]

show_magicians(make_great(magicians))
