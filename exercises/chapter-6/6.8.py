"""
6-8. Pets: 
Make several dictionaries, where the name of each dictionary is the name of a 
pet. In each dictionary, include the kind of animal and the owner’s name. Store
these dictionaries in a list called pets. Next, loop through your list and as 
you do print everything you know about each pet.
"""

ruffles = {"type": "dog", "owner": "patricia"}
moshi = {"type": "cat", "owner": "grant"}

pets = [ruffles, moshi]
for pet in pets:
    for attribute, value in pet.items():
        print(f"{attribute} is {value}")
