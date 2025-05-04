# Randomization and Lists

# 1. Randomization
# Randomization is the process of making something random. 
# - In practice, randomization is not truly random, but rather pseudo-random. 
# - This video explains that: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# In Python, we can use the `random` module to generate random numbers, select random elements from a list, and shuffle lists.
# - random documentation: https://docs.python.org/3/library/random.html

import random
print("Randomization")
random_number = random.randint(1, 10) # Generates a random integer between 1 and 10 (inclusive)
print(random_number)

random_number = random.random() # Generates a random float between 0.0 and 1.0 (exclusive)
print(random_number)

random_number = random.random() * 10 # Generates a random float between 0.0 and 10.0 (exclusive)
print(random_number)

random_number = random.uniform(1, 10) # Generates a random float between 1.0 and 10.0 (inclusive)
print(random_number)



#  2. Lists
# Lists are a data structure in Python that can hold multiple values.
# - Lists are mutable, meaning you can change their contents after creation.
# - Lists can hold different data types, including other lists.
# - Lists are ordered, meaning the order of elements is preserved.
# - Lists are indexed, meaning you can access elements by their index (starting from 0).
# - Lists documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
print("\nLists")

fruits = ["apple", "banana", "cherry"]
print(fruits) # Prints the entire list
print(fruits[0]) # Prints the first element of the list (index 0)
print(fruits[-2]) # Prints the second to last element of the list (index -2)
print(fruits[1:3]) # Prints a slice of the list from index 1 to 2 (exclusive of index 3)

fruits.append("orange") # Adds "orange" to the end of the list
print(fruits) 




# Bonus: Custom Module
print("\nCustom Module")

from my_module import my_module
print(my_module.my_favorite_number)
