"""
8-6. City Names: 
Write a function called city_country() that takes in the name of a city and its 
country. The function should return a string formatted like this: 
"Santiago, Chile". Call your function with at least three city-country pairs, 
and print the value that’s returned.
"""


def city_country(name, country):
    """Return the name and country of a city, neatly formatted."""
    return f"{name}, {country}"


print(city_country("Singapore", "Singapore"))
print(city_country("Santiago", "Chile"))
print(city_country("New York", "USA"))
