"""
4-7. Threes: 
Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the 
numbers in your list.
"""

nums = [value * 3 for value in range(3, 31)]

for num in nums:
    print(num)
