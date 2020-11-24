'''
COMP 125 - Programming Jam Session #2
November 23-24-25, 2020

Bubble sort
'''
# length: 5
# [3, 2, 5, 1, 2]
# i = 1, j = 4
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort(lst):
    iters = 0
    length = len(lst)
    for i in range(length): # 6
        iters += 1
        for j in range(length - 1): # 5
            iters += 1
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    print(iters)
    return lst


def faster_bubble_sort(lst):
    iters = 0
    length = len(lst)
    for i in range(length): 
        iters += 1
        for j in range(length - 1 - i): 
            iters += 1
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
    print(iters)
    return lst

lst = [6, 2, 1, 5, 3, 3, 9, 7, 6, 4, 6, 9, 1, 2]
print(bubble_sort(lst))
print(faster_bubble_sort(lst))
