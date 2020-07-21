"""
6-4. Glossary 2: 
Now that you know how to loop through a dictionary, clean up the code from 
Exercise 6-3 (page 102) by replacing your series of print statements with a 
loop that runs through the dictionary’s keys and values. When you’re sure that 
your loop works, add five more Python terms to your glossary. When you run your
program again, these new words and meanings should automatically be included in 
the output .
"""

programming_terms = {
    "logical error": "problem occurs in code logic",
    "list comprehension": "combines the for loop and the creation of new elements into one line",
    "conditional test": "an expression that can be evaluated as True or False",
}

for programming_term, meaning in programming_terms.items():
    print(programming_term + ": " + meaning)

