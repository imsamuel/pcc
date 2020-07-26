"""11-3. Employee: 
Write a class called Employee. The __init__() method should take in a first 
name, a last name, and an annual salary, and store each of these as attributes. 
Write a method called give_raise() that adds $5000 to the annual salary by 
default but also accepts a different raise amount. Write a test case for 
Employee. Write two test methods, test_give_ default_raise() and 
test_give_custom_raise(). Use the setUp() method so you don’t have to create a 
new employee instance in each test method. Run your test case, and make sure 
both tests pass."""

"""A class that can be used to represent an employee."""


class Employee:
    """A simple attempt at modelling an employee."""

    def __init__(self, fname, lname, salary):
        """Initialize fname, lname and salary attributes."""
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def give_raise(self, amount=5000):
        """Raises the employee's annual salary by the given amount."""
        self.salary += amount
