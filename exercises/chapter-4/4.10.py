"""
4-10. Slices: 
Using one of the programs you wrote in this chapter, add several lines to the 
end of the program that do the following: 

• Print the message, `The first three items in the list are:`. Then use a slice
to print the first three items from that program’s list. 

• Print the message, `Three items from the middle of the list are:`. 
Use a slice to print three items from the middle of the list. 

• Print the message, `The last three items in the list are:`. Use a slice to 
print the last three items in the list.
"""

nums = list(range(1, 10))

print("The first three items in the list are: ", nums[:3])
print("Three items from the middle of the list are: ", nums[3:6])
print("The last three items in the list are: ", nums[-3:])
