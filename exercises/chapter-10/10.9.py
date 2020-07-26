"""
10-9. Silent Cats and Dogs: 
Modify your except block in Exercise 10-8 to fail silently if either file is 
missing.
"""

try:
    with open("cats.txt") as file:
        for cat in file.readlines():
            print(cat.rstrip())
    with open("dogs.txt") as file:
        for dog in file.readlines():
            print(dog.rstrip())
except FileNotFoundError:
    pass
