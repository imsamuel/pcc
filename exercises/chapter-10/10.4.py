"""
10-4. Guest Book: 
Write a while loop that prompts users for their name. When they enter their 
name, print a greeting to the screen and add a line recording their visit in a 
file called guest_book.txt. Make sure each entry appears on a new line in the 
file.
"""

while True:
    name = input("What is your name? (enter 'q' to quit) ")
    if name == "q":
        break
    print(f"Hello {name}!")
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")
