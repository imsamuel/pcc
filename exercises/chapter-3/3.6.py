"""
3-6. More Guests: 
You just found a bigger dinner table, so now more space is available. Think of 
three more guests to invite to dinner. 

• Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print 
statement to the end of your program informing people that you found a bigger 
dinner table. 

• Use insert() to add one new guest to the beginning of your list. 

• Use insert() to add one new guest to the middle of your list. 

• Use append() to add one new guest to the end of your list. 

• Print a new set of invitation messages, one for each person in your list.
"""

guests = ["Malcolm X", "Lee Kuan Yew", "Lim Bo Seng"]

print("Good news guys, I found a bigger table!")

guests.insert(0, "Barack Obama")

guests.insert(2, "Harriet Tubman")

guests.append("Adnan Bin Saidi")

print("Hey " + guests[0] + ", I would love to invite you for dinner.")
print("Hey " + guests[1] + ", I would love to invite you for dinner.")
print("Hey " + guests[2] + ", I would love to invite you for dinner.")
print("Hey " + guests[3] + ", I would love to invite you for dinner.")
print("Hey " + guests[4] + ", I would love to invite you for dinner.")
print("Hey " + guests[5] + ", I would love to invite you for dinner.")
