"""
6-10. Favorite Numbers: 
Modify your program from Exercise 6-2 (page 102) so each person can have more 
than one favorite number. Then print each person’s name along with their 
favorite numbers.
"""

favorite_numbers = {
    "marie": [5, 6],
    "elliot": [14, 12],
    "samuel": [16, 3],
    "jerry": [19, 20, 21],
    "anna": [1, 5],
}

for person, favorite_numbers in favorite_numbers.items():
    print(f"{person} favorite numbers are: ")
    for number in favorite_numbers:
        print(number)
