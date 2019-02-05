import numpy as np

a = [1, 2, 3, 4, 5]
b = [2, 3, 5]

a2 = ["some", "cat2", "plane", "water"]
b2 = ["water", "cat2", "cat", "dog", "human", "ufo"]

def matching_values(a, b):
    return sum([1 if i in b else 0 for i in a])

print(matching_values(a, b))
print(matching_values(a2, b2))