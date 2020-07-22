"""
7-9. No Pastrami: 
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
'pastrami' appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out of 
pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
from sandwich_orders. Make sure no pastrami sandwiches end up in 
finished_sandwiches.
"""

ordered_sandwiches = ["pastrami", "pastrami", "pastrami"]
print("The deli has ran out of pastrami")
while "pastrami" in ordered_sandwiches:
    ordered_sandwiches.remove("pastrami")

assert "pastrami" not in ordered_sandwiches
