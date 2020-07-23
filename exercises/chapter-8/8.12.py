"""
8-12. Sandwiches: 
Write a function that accepts a list of items a person wants on a sandwich. The 
function should have one parameter that collects as many items as the function 
call provides, and it should print a summary of the sandwich that is being 
ordered. Call the function three times, using a different number of arguments 
each time.
"""


def display_sandwich(*fillings):
    """Display the contents of an ordered sandwich."""
    for filling in fillings:
        print(f"{filling} added")


display_sandwich("cheese", "salami")
display_sandwich("lettuce", "olives")
display_sandwich("cheese", "meatballs", "bacon")
