"""
7-10. Dream Vacation: 
Write a program that polls users about their dream vacation. Write a prompt 
similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll.
"""

responses = {}
while True:
    name = input("What is your name?(enter 'quit' to quit) ")
    if name == "quit":
        break
    place = input("If you could visit one place in the world, what would it be? ")
    responses[name] = place

for name, place in responses.items():
    print(f"{name} would go to {place}")
