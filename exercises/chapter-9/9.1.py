"""
9-1. Restaurant: 
Make a class called Restaurant. The __init__() method for Restaurant should 
store two attributes: a restaurant_name and a cuisine_type. Make a method 
called describe_restaurant() that prints these two pieces of information, and a 
method called open_restaurant() that prints a message indicating that the 
restaurant is open. Make an instance called restaurant from your class. Print 
the two attributes individually, and then call both methods.
"""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        "Initialize name and cuisine attributes."
        super().__init__()
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Display the name of the restaurant and the cuisine it serves."""
        print(f"Our restaurant {self.name} provides {self.cuisine} food.")

    def open(self):
        """Announce the opening of the restaurant."""
        print("The restaurant is open.")


tonito = Restaurant("Tonito", "Latin")

tonito.describe()
tonito.open()

