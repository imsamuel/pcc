"""
8-9. Magicians: 
Make a list of magician’s names. Pass the list to a function called 
show_magicians(), which prints the name of each magician in the list.
"""


def show_magicians(magicians):
    """Display each magician from the given list of magicians."""
    for magician in magicians:
        print(magician)


magicians = ["David Blaine", "David Copperfield"]
show_magicians(magicians)
