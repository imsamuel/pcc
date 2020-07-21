"""
6-5. Rivers: 
Make a dictionary containing three major rivers and the country each river runs
through. One key-value pair might be 'nile': 'egypt'. 

• Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt. 
• Use a loop to print the name of each river included in the dictionary. 
• Use a loop to print the name of each country included in the dictionary.
"""

countries = {"nile": "egypt", "mississippi": "usa", "yangtze": "china"}

for river, country in countries.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in countries:
    print(river)

for country in countries.values():
    print(country)

