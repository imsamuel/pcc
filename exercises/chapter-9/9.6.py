"""
9-6. Ice Cream Stand: 
An ice cream stand is a specific kind of restaurant. Write a class called 
IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
(page 166) or Exercise 9-4 (page 171). Either version of the class will work; 
just pick the one you like better. Add an attribute called flavors that stores 
a list of ice cream flavors. Write a method that displays these flavors. Create 
an instance of IceCreamStand, and call this method.
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


class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes."""
        super().__init__(name, cuisine)
        self.flavors = ["chocolate", "strawberry", "vanilla"]

    def display_flavors(self):
        """Display the ice cream flavors the stand offers."""
        for flavor in self.flavors:
            print(flavor)


apiary = IceCreamStand("apiary", "ice cream")

apiary.display_flavors()
