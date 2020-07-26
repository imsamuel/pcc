"""
10-7. Addition Calculator: 
Wrap your code from Exercise 10-6 in a while loop so the user can continue 
entering numbers even if they make a mistake and enter text instead of a 
number.
"""

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(num1 + num2)
    except ValueError:
        print("a non-numerical value was entered")
