"""
3-7. Shrinking Guest List: 
You just found out that your new dinner table won’t arrive in time for the 
dinner, and you have space for only two guests. 

• Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner. 

• Use pop() to remove guests from your list one at a time until only two names 
remain in your list. Each time you pop a name from your list, print a message 
to that person letting them know you’re sorry you can’t invite them to dinner. 

• Print a message to each of the two people still on your list, letting them 
know they’re still invited. 

• Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program.
"""

guests = ["Malcolm X", "Lee Kuan Yew", "Lim Bo Seng"]

print("Good news guys, I found a bigger table!")

guests.insert(0, "Barack Obama")

guests.insert(2, "Harriet Tubman")

guests.append("Adnan Bin Saidi")

print("I'm really sorry guys but I can only invite two people at the moment.")

adnan = guests.pop()
print("I'm really sorry " + adnan + " but I can't invite you for dinner.")

lim_bo_seng = guests.pop()
print("I'm really sorry " + lim_bo_seng + " but I can't invite you for dinner.")

lee_kuan_yew = guests.pop()
print("I'm really sorry " + lee_kuan_yew + " but I can't invite you for dinner.")

harriet_tubman = guests.pop()
print("I'm really sorry " + harriet_tubman + " but I can't invite you for dinner.")


print(guests)

print("Hey " + guests[0] + ", just to let you know, you're still invited!")
print("Hey " + guests[1] + ", just to let you know, you're still invited!")

del guests[0]
del guests[0]

print(guests)
