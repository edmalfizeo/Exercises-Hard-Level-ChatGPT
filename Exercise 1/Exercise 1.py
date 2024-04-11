'''Nested List Comprehension: 
    Write a Python program to generate a 3x3 matrix with each element being the multiplication of its indices,
    using nested list comprehension
'''
matrix = [[row * column for column in range(3)] for row in range(3)]
print(matrix)   

# How can i improve my perfomance:
# My thought about trying to make it in list comprehesion was almost right but my row came first, but the column should come first
''' The bracket was closed wrong, I closed my bracket after the two for loops but should been closed on the first for,
letting the other for on the other bracket
'''