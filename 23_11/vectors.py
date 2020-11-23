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

# v1: [4, 5, 6]
# v2: [1, 2, 2] 
# -> [5, 7, 8]
def add_vector(v1, v2):
    result = [0, 0, 0]
    for i in range(3):
        result[i] = v1[i] + v2[i]
    return result


def add_vector_general(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result


def length_vector(vector):
    total = 0
    for i in vector:
        total += i ** 2
    return math.sqrt(total)


# v1:[4, 5, 6]
# v2:[1, 2, 3]
# v1 * v2 = 4*1 + 5*2 + 6*3
def dot_product(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total


# arccos(vector[x] / length(vector))
def vector_angle(vector):
    return math.degrees(math.acos((vector[0] / length_vector(vector))))

