"""
9-8. Privileges: 
Write a separate Privileges class. The class should have one attribute, 
privileges, that stores a list of strings as described in Exercise 9-7. Move 
the show_privileges() method to this class. Make a Privileges instance as an 
attribute in the Admin class. Create a new instance of Admin and use your 
method to show its privileges.
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
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        """Display the admin's privileges."""
        for privilege in self.privileges:
            print(privilege)


class Privileges:
    """A simple attempt to model the privileges of a user."""

    def __init__(self, privileges):
        """Initialize privileges attribute."""
        super().__init__()
        self.privileges = privileges

    def show_privileges(self):
        """Display the user's privileges."""
        for privilege in self.privileges:
            print(privilege)


admin1 = Admin("Samuel", "Yap", 19, "Singaporean", ["can add post", "can delete post"])

admin1.privileges.show_privileges()
