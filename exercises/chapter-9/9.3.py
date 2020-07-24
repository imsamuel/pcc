"""
9-3. Users: 
Make a class called User. Create two attributes called first_name and 
last_name, and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints a 
summary of the user’s information. Make another method called greet_user() that 
prints a personalized greeting to the user. Create several instances 
representing different users, and call both methods for each user.
"""


class User:
    """A simple attempt to model a user."""

    def __init__(self, fname, lname, age, nationality):
        """Initialize fname and lname attributes."""
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality

    def describe(self):
        """Display the attributes of the user."""
        print(f"I'm {self.fname} {self.lname}, a {self.age} y'old {self.nationality}!")

    def greet_user(self):
        """Give the user a personalized greeting."""
        print(f"Welcome back {self.fname}!")


samuel = User("Samuel", "Yap", 19, "Singaporean")
samuel.describe()
samuel.greet_user()

jiet = User("Jiet", "Ng", 21, "Malaysian")
jiet.describe()
jiet.greet_user()

