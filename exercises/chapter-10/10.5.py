"""
10-5. Programming Poll: 
Write a while loop that asks people why they like programming. Each time 
someone enters a reason, add their reason to a file that stores all the 
responses.
"""

while True:
    reason = input("Why do you like programming? (enter 'q' to quit) ")
    if reason == "q":
        break
    with open("reasons.txt", "a") as file:
        file.write(reason + "\n")
