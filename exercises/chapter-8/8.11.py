"""
8-11. Unchanged Magicians: 
Start with your work from Exercise 8-10. Call the function make_great() with a 
copy of the list of magicians’ names. Because the original list will be 
unchanged, return the new list and store it in a separate list. Call 
show_magicians() with each list to show that you have one list of the original 
names and one list with the Great added to each magician’s name.
"""


def show_magicians(magicians):
    """Display each magician from the given list of magicians."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Transform the given magicians into great magicians."""
    return list(map((lambda magician: magician + " the Great"), magicians))


magicians = ["David Blaine", "David Copperfield"]

show_magicians(magicians)
show_magicians(make_great(magicians))
