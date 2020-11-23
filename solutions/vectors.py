'''
COMP 125 - Programming Jam Session #2
November 23-24-25, 2020

Implement the following functions for vectors given as a list of size 3
* add_vector:       input two vectors, returns resulting vector
* length_vector:    input a vector, returns the magnitude of the vector    
* dot_product:      input two vectors, returns the dot product of the vectors
* angle_vector:     input a vector, returns the angle the vector makes with the x-axis
'''
import math

'''
READ THIS FIRST:
    I've also included solutions with different approaches below. 
    You don't have to spend time with, but you can look more into them if you are interested in more advanced features of Python. 
    I've specifically used these two:
    - the zip() method -> https://www.programiz.com/python-programming/methods/built-in/zip
    - list comprehensions -> https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    These don't let you you anything new, but can help you write shorter code.
'''

# ----- ADD VECTORS -----

def add_vector(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result

# Using the zip() method
def add_vector_2(v1, v2):
    result = []
    for (val1, val2) in zip(v1, v2):
        result.append(val1 + val2)
    return result

# Using list comprehensions and the zip() method
def add_vector_3(v1, v2):
    return [val1 + val2 for (val1, val2) in zip(v1, v2)]

# ----- VECTOR LENGTH -----

def length_vector(vector):
    total = 0
    for val in vector:
        total += val ** 2
    return math.sqrt(total)

# Using list comprehensions
def length_vector_2(vector):
    total = sum([val ** 2 for val in vector])
    return math.sqrt(total)

# ----- DOT PRODUCT -----

def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

# Using zip()
def dot_product_2(v1, v2):
    result = 0
    for (val1, val2) in zip(v1, v2):
        result += val1 * val2
    return result

# Using list comprehensions and zip()
def dot_product_3(v1, v2):
    return sum([val1 * val2 for (val1, val2) in zip(v1, v2)])

# ----- VECTOR ANGLE -----

def angle_vector(vector):
    value = vector[0] / length_vector(vector)
    return math.degrees(math.acos(value))
