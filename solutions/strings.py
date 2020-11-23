'''
COMP 125 - Programming Jam Session #2
November 23-24-25, 2020

1. Write a function dna_replica, which takes  a DNA sequence of arbitrary length as input, and returns the complementary sequence as a string. 

2. Implement a function, remove_whites, which takes a string as input and returns a new string by removing the extra white space characters (“ “, tab character, newline character). In the return string all words should be separated by just a single space character.
'''

# Check each character with if-elif-else statements and append to the result.
def dna_replica(dna):
    result = ''
    for char in dna:
        if char == 'A':
            result += 'T'
        elif char == 'T':
            result += 'A'
        elif char == 'C':
            result += 'G'
        else:
            result += 'C'
    return result


def remove_whites(text):
    result = ''
    for char in text:
        if char == ' ':
            if result[-1] != ' ':
                result += char
        elif char not in ['\n', '\t']:
            result += char
    return result