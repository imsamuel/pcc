"""
9-13. OrderedDict Rewrite: 
Start with Exercise 6-4 (page 108), where you used a standard dictionary to 
represent a glossary. Rewrite the program using the OrderedDict class and make 
sure the order of the output matches the order in which key-value pairs were 
added to the dictionary.
"""

from collections import OrderedDict

programming_terms = OrderedDict()
programming_terms["logical error"] = "problem occurs in code logic"
programming_terms[
    "list comprehension"
] = "combines the for loop and the creation of new elements into one line"
programming_terms[
    "conditional test"
] = "an expression that can be evaluated as True or False"

for programming_term, meaning in programming_terms.items():
    print(programming_term + ": " + meaning)
