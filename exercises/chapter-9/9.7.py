"""
9-7. Admin: 
An administrator is a special kind of user. Write a class called Admin that 
inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 
9-5 (page 171). Add an attribute, privileges, that stores a list of strings 
like "can add post", "can delete post", "can ban user", and so on. Write a 
method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method.
"""


class User:
    """A simple attempt to model a user."""

    def __init__(self, fname, lname, age, nationality):
        """Initialize fname, lname, age, and nationality attributes."""
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


class Admin(User):
    """A simple attempt to model an administrator."""

    def __init__(self, fname, lname, age, nationality, privileges):
        """Initiate fname, lname, age, nationality and previliges attributes."""
        super().__init__(fname, lname, age, nationality)
        self.privileges = privileges

    def show_privileges(self):
        """Display the admin's privileges."""
        for privilege in self.privileges:
            print(privilege)


admin1 = Admin("samuel", "yap", 19, "Singaporean", ["can add post", "can delete post"])

admin1.show_privileges()

