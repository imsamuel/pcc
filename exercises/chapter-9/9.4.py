"""
9-4. Number Served: 
Start with your program from Exercise 9-1 (page 166). Add an attribute called 
number_served with a default value of 0. Create an instance called restaurant 
from this class . Print the number of customers the restaurant has served, and 
then change this value and print it again. Add a method called set_number_served() 
that lets you set the number of customers that have been served. Call this 
method with a new number and print the value again. Add a method called 
increment_number_served() that lets you increment the number of customers 
who’ve been served. Call this method with any number you like that could 
represent how many customers were served in, say, a day of business.
"""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        "Initialize name, cuisine, and number_served attributes."
        super().__init__()
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Display the name of the restaurant and the cuisine it serves."""
        print(f"Our restaurant {self.name} provides {self.cuisine} food.")

    def increment_number_served(self, increment):
        """Increment the number of people the restaurant has served by the given value."""
        self.number_served += increment

    def open(self):
        """Announce the opening of the restaurant."""
        print("The restaurant is open.")

    def set_number_served(self, number_served):
        """Set the number of people the restaurant has served to the given value."""
        self.number_served = number_served


tonito = Restaurant("Tonito", "Latin")

tonito.set_number_served(100)
assert tonito.number_served == 100

tonito.increment_number_served(5)
assert tonito.number_served == 105
