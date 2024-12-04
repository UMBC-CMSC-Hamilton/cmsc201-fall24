"""
    Talk about the running times of bubble insertion and selection sort
"""


def selection_sort(the_list):
    for i in range(len(the_list)):  # 0 to n - 1 , n times
        min_index = i
        # this loop is doing n - i - 1 [things, technically]
        for j in range(i, len(the_list)):  # don't go back to the things we already sorted
            if the_list[j] < the_list[min_index]:
                min_index = j

        if i != min_index:
            temp = the_list[i]
            the_list[i] = the_list[min_index]
            the_list[min_index] = temp
    return the_list

"""

Goal: add up the number of steps that we're taking.

    0 1 2 3 4 5
    start at i = 2, n = 6
    n - i things left to do.
    for the outer loop it's going to scan from 0 to n - 1
        inner loop is going to do n - i operations
        
    n = 6
    i = 0   6 - 0 = 6
    i = 1   6 - 1 = 5
    i = 2   6 - 2 = 4
    i = 3   6 - 3 = 3
    i = 4   6 - 4 = 2
    i = 5   6 - 5 = 1
            + total number of operations
        
    1 + 2 + 3 + 4 + 5 + 6 [arithmetic sum, gauss sum]
                          = 21 = 6 * 7 / 2 ??
    |                   |
        |           |
            |   |
    7s coming out... how many of them? 6/2 pairs
    (6/2) * 7 = 6 (6 + 1)/2
    
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 [arithmetic sum, gauss sum]
    |                           |     = 21 + 7 + 8 = 36 = 8(9)/2 ?? yes
       |                    |
            |           |
                |   |
    8/2 pairs * 9 (sum of each pair)
    
    1 + 2 + 3 + ... + (n - 2) + (n - 1) + n [n even]
    
    n + 1
    (n - 1) + 2 = n + 1
    (n - 2) + 3 = n + 1 all n + 1
    how many pairs are there?
    n/2 pairs
    (n + 1) * n/2 = n (n + 1)/ 2
    
    
    1 + 2 + 3 + 4 + 5 + 6 + 7
    |                       |
        |               |
            |       |
                |
        7 elements
        7/2 = 3.5
    Real question:
    1 + 2 + 3 + ... + (n - 1) + (n) = n (n + 1) / 2
    
    Selection sort is going to run in about n (n + 1) / 2 steps for a list of size n
                                                n^2 / 2
                                                
    
"""
def bubble_sort(the_list):
    swapped = True
    iteration = 0
    while swapped:
        swapped = False
        for i in range(len(the_list) - 1 - iteration):
            if the_list[i] > the_list[i + 1]:
                swapped = True
                # swap process
                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp

        iteration += 1

    return the_list


"""
The best case of bubble sort is about n - 1 steps.


What's the worst case of bubble sort?

    How many swaps did we just do?
        n [really n - 1] we're going to be cavalier
        n - 1 swaps
        n - 2
        n - 3
        ...
        1 swap
        + 
    = 1 + 2 + 3 + 4 + ... + (n - 3) + (n - 2) + (n - 1) + n = n(n + 1) / 2 steps


n       # steps
---------------
1           n(n + 1) / 2 = 1 ( 2) / 2 = 1 step ??
10          n^2/2 100 / 2 = 50 steps
100         (100^2) / 2 = 5,000 steps
1000         1000^2 / 2 = 1M/2 = 500,000 steps
10000       100M / 2 = 50M
100,000     100000^2 / 2 = 10B/2 = 5B
"""

import time
import random



def insertion_sort(the_list):
    for i in range(len(the_list)):
        # print(i, the_list[i], the_list)
        j = i  # j is going to be the index that we're pulling back
        while j > 0 and the_list[j] < the_list[j - 1]:
            # swap j and j - 1
            temp = the_list[j]
            the_list[j] = the_list[j - 1]
            the_list[j - 1] = temp

            j -= 1 # very important easy to forget

    return the_list


def timer_of_sort(the_sort, the_list):
    the_copy = list(the_list)
    start = time.process_time()
    the_sort(the_copy)
    delta = time.process_time() - start
    print('The sort took', delta, 'seconds on length', len(the_list))


"""
    Merge Sort
    
    Recursive sort
    
        Idea:
            divide the list in half - first half and second half
            merge sort the first half [recursive]
            merge sort the second half [recursive] 
            
            put together the two lists
                Idea: we have two sorted lists we have to put them back together into a sorted list
                
            [2, 5, 6, 9]
                |
            [1, 2, 3, 4]
                         |
            [1, 2, 2, 3, 4, 5, 6, 9]
            [1, 1, 1, 1] |
            [2, 2, 2, 2]
              |
            [1, 1, 1, 1, 2, 2, 2, 2] 
"""

def put_together(a_list, b_list):
    total_list = []
    a_index = 0
    b_index = 0
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] <= b_list[b_index]:
            total_list.append(a_list[a_index])
            a_index += 1
        else:
            total_list.append(b_list[b_index])
            b_index += 1

    for i in range(a_index, len(a_list)):
        total_list.append(a_list[a_index])
    for j in range(b_index, len(b_list)):
        total_list.append(b_list[b_index])

    return total_list


def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list

    n = len(the_list)
    first_half = the_list[0: n // 2]
    second_half = the_list[n//2: len(the_list)]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return put_together(first_half, second_half)

"""

[4, 9, 2, 7, 6, 8, 2, 1]
[4, 9, 2, 7]  [6, 8, 2, 1]
[4, 9] [2, 7] [6, 8] [2, 1]
[4] [9] [2] [7] [6] [8] [2] [1] (base case) returning
([4] [9]) ([2] [7]) ([6] [8]) ([2] [1])
([4, 9] [2, 7]) ([6, 8] [1, 2])
([2, 4, 7, 9] [1, 2, 6, 8])
[1, 2, 2, 4, 6, 7, 8, 9]

[2, 9, 4, 5, 1]
[2, 9] [4, 5, 1]
[2][9] [4][5, 1]
           [5][1]
           [1, 5]
[2, 9] [1, 4, 5]
[1, 2, 4, 5, 9]

[4, 7, 4, 9, 3, 8, 6, 5, 2, 6]
[4, 7, 4, 9, 3] [8, 6, 5, 2, 6]
[4, 7] [4, 9, 3] [8, 6] [5, 2, 6]
[4][7] [4][9, 3] [8][6] [5][2, 6]
           [9][3]           [2][6]
           [3, 9]           [2, 6]
([4, 7] [3, 4, 9]) ([8, 6] [2, 5, 6])
[3, 4, 4, 7, 9] [2, 5, 6, 6, 8]
[2, 3, 4, 4, 5, 6, 6, 7, 8, 9]

Each element at each level gets put into a bigger total_list once. Cost: n steps / level

n / 2 
(n / 2 ) / 2 = n / 4
n / 8
n / 16
n / 32
n / 64
n / 2^7 = n / 128
n / 2^8 = n / 256
...
n / 2^steps ~~= 1

n = 2^steps
lg(n) = lg(2^steps)
lg(n) = log_2(n)

lg(n) levels * n cost / level = n * lg(n) [log-linear]
"""



for x in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    my_list = [random.randint(0, x) for _ in range(x)]
    timer_of_sort(merge_sort, my_list)