"""
10-11. Favorite Number: 
Write a program that prompts for the user’s favorite number. Use json.dump() to 
store this number in a file. Write a separate program that reads in this value 
and prints the message, “I know your favorite number! It’s _____.”
"""

import json

number = input("What is your favorite number? ")

with open("number.txt", "w") as file:
    json.dump(number, file)

with open("number.txt") as file:
    number = json.load(file)
    print(f"I know your favorite number! It's {number}.")
