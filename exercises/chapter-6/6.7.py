"""
6-7. People: 
Start with the program you wrote for Exercise 6-1 (page 102). Make two new 
dictionaries representing different people, and store all three dictionaries in 
a list called people. Loop through your list of people. As you loop through the 
list, print everything you know about each person.
"""

samuel = {"first_name": "samuel", "last_name": "yap", "age": 19, "city": "Singapore"}
jiet = {"first_name": "jiet", "last_name": "ng", "age": 21, "city": "Malaysia"}
kaien = {"first_name": "kaien", "last_name": "beh", "age": 19, "city": "Malaysia"}

people = [samuel, jiet, kaien]
for person in people:
    for attribute, value in person.items():
        print(f"{attribute}: {value}")
