"""
5-2. More Conditional Tests: 
You don’t have to limit the number of tests you create to 10. If you want to
try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following: 

• Tests for equality and inequality with strings
• Tests using the lower() function 
• Numerical tests involving equality and inequality, greater than and less 
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword 
• Test whether an item is in a list 
• Test whether an item is not in a list
"""

print("hello" == "Hello")
print("hello" == "Hello".lower())
print(1 > 0)
print(1 < 2)
print(1 >= 1)
print(1 <= 1)

numbers = [1, 2, 3]
print(1 in numbers)
print(4 not in numbers)
