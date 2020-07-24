"""
9-5. Login Attempts: 
Add an attribute called login_attempts to your User class from Exercise 9-3 
(page 166). Write a method called increment_ login_attempts() that increments 
the value of login_attempts by 1. Write another method called 
reset_login_attempts() that resets the value of login_ attempts to 0. Make an 
instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and 
then call reset_login_attempts(). Print login_attempts again to make sure it 
was reset to 0.
"""


class User:
    """A simple attempt to model a user."""

    def __init__(self, fname, lname, age, nationality):
        """Initialize fname, lname, age, nationality and login_attempts attributes."""
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0

    def describe(self):
        """Display the attributes of the user."""
        print(f"I'm {self.fname} {self.lname}, a {self.age} y'old {self.nationality}!")

    def greet_user(self):
        """Give the user a personalized greeting."""
        print(f"Welcome back {self.fname}!")

    def increment_login_attempts(self):
        """Increment the user's login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the user's login attempts."""
        self.login_attempts = 0


samuel = User("Samuel", "Yap", 19, "Singaporean")

samuel.increment_login_attempts()
samuel.increment_login_attempts()
samuel.increment_login_attempts()
assert samuel.login_attempts == 3

samuel.reset_login_attempts()
assert samuel.login_attempts == 0
