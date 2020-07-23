"""
8-4. Large Shirts: 
Modify the make_shirt() function so that shirts are large by default with a 
message that reads I love Python. Make a large shirt and a medium shirt with 
the default message, and a shirt of any size with a different message.
"""


def make_shirt(size="L", text="I love Python"):
    """Display the specs of the requested shirt."""
    print(f"The size of the shirt should be {size} and it should have text: '{text}'")


make_shirt()

make_shirt(text="I love Java")
