"""
6-11. Cities: 
Make a dictionary called cities. Use the names of three cities as keys in your 
dictionary. Create a dictionary of information about each city and include the 
country that the city is in, its approximate population, and one fact about 
that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the 
information you have stored about it.
"""

cities = {
    "singapore": {
        "country": "singapore",
        "population": 7_000_000,
        "fact": "multiracial",
    },
    "tokyo": {"country": "japan", "population": 9_000_000, "fact": "fresh sashimi"},
    "chicago": {"country": "usa", "population": 3_000_000, "fact": "gang activity"},
}

for city, attributes in cities.items():
    print(f"{city}:")
    for attribute, value in attributes.items():
        print(f"{attribute} is {value}")
