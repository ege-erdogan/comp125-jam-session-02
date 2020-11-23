'''
COMP 125 - Programming Jam Session #2
November 23-24-25, 2020

Bubble sort
'''

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


# the iters variable is there to let you see how many fewer iterations the better version takes.
# it has nothing to do with the the functionality of the algorithm
def bubble_sort(lst):
    length = len(lst)
    iters = 0
    for i in range(length-1):
        iters += 1
        for j in range(0, length-1):
            iters += 1
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    print(f'Normal bubble sort took {iters} iterations with list of length {length}.')
    return lst


def better_bubble_sort(lst):
    length = len(lst)
    iters = 0
    for i in range(length-1):
        iters += 1
        for j in range(0, length-1-i):
            iters += 1
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    print(f'Better bubble sort took {iters} iterations with list of length {length}.')
    return lst
