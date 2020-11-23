'''
COMP 125 - Programming Jam Session #2
November 23-24-25, 2020

Bubble sort
'''

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort(lst): 
    length = len(lst)
    for i in range(length - 1): 
        for j in range(length - 1):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    return lst


def better_bubble_sort(lst): 
    length = len(lst)
    for i in range(length - 1): 
        for j in range(length - 1 - i):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    return lst


lst = [3, 1, 6, 3, 8, 2, 5, 1, 2, 3, 1, 8, 9]
print(bubble_sort(lst))
print(better_bubble_sort(lst))