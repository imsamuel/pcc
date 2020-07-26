"""
10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 
into one file. If the number is already stored, report the favorite number to 
the user. If not, prompt for the user’s favorite number and store it in a file. 
Run the program twice to see that it works.
"""

import json

try:
    with open("number.txt") as file:
        number = json.load(file)
        print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    with open("number.txt", "w") as file:
        number = input("What is your favorite number? ")
        json.dump(number, file)
