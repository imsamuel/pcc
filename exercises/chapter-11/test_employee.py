"""A collection of functions for working with an employee."""

from employee import Employee

def test_give_default_raise():
     """Test that a default raise works correctly."""
     maria = Employee("Maria", "Hernandez", 5000)
     maria.give_raise()
     assert maria.salary == 10000

def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    joe = Employee("Joe", "Mama", 5000)
    joe.give_raise(10000)
    assert joe.salary == 15000
    