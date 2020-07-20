"""
3-10. Every Function: 
Think of something you could store in a list. For example, you could make a 
list of mountains, rivers, countries, cities, languages, or anything else you’d
like. Write a program that creates a list containing these items and then uses
each function introduced in this chapter at least once.
"""

countries = ["India", "China", "Malaysia"]

countries.insert(0, "Singapore")
print(countries)

countries.append("Italy")
print(countries)

del countries[4]
print(countries)

malaysia = countries.pop()
print(malaysia)
print(countries)

print(sorted(countries))
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)

print(len(countries))

