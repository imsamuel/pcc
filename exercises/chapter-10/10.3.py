"""
10-3. Guest: 
Write a program that prompts the user for their name. When they respond, write 
their name to a file called guest.txt.
"""

name = input("What is your name? ")

with open("guest.txt", "w") as file:
    file.write(name)

