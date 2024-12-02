"""
    Recall how bubble, selection and insertion sort work
        find out how fast they run
        characterize that in terms of input size
    Talk about Merge and Quick Sort if possible.


Bubble sorts works by asking if it needs to swap the adjacent elements
    if it does then it scans from the first to the last element - i [ith iteration]

    Count the number of swaps that are performed / loop iterations

    Pretend it takes n swaps on the 0 iteration to swap the first time
                     n - 1 swaps on the 1 iteration
                     n - 2 swaps on the 2 iteration
                     ...
                     1 swap on the   n - 1 iteration
                     0 swaps on the  n iteration

        plug in n = 10 for instance:
        10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1  [arithmetic sum, Gauss sum]

        1 + 2 + 3 + ... + (n - 2) + (n - 1) + n = n(n + 1) / 2
        counting up the number of possible swaps / iterations through the inner loop
        Why is this true?

        1 + 2 + 3 + 4 + 5 + 6 = 6 * 7 / 2 = 21
        |                   |
            |           |
                |   |
                if i add these pairs i always get 7
                6 / 2 = 3
                3 * 7 = 21 = 6 * 7 / 2
        1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 21 + 7 + 8 = 36 = 8 * (8 + 1) / 2 = 4 * 9 = 36
        |                           |
            |                   |
                |           |
                    |   |
            all add to 9, there's 8/2 = 4 pairs so 4 * 9 = 36 and we're right
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 7 * 8 / 2 = 28 yes again.. 21 + 7
    |                       |
       |                |
           |        |
                | trick half pair

                notice that 7 elements 7/2 = 3.5 pairs

    Bubble sort takes n(n + 1) / 2 steps for an input size of n.
    Super-Guesstimate here:
    n^2 / 2 # steps
    n       steps
    1       1^2 / 2 = 1/2
    10      10^2 / 2 = 100 / 2 = 50 steps
    100     100^2 / 2 = 10,000 / 2 = 5000 steps
    1000    1000^2 / 2 = 500,000 steps
    10,000  100 M / 2 = 50M
    100,000 10B / 2 = 5B  ==> 5B / 1M = 5000 seconds...
"""

"""
Analysis of selection and insertion sort:
    def selection_sort(the_list):
    for i in range(len(the_list)):  # 0 to n - 1 , n times
        # print(the_list)
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
    
    n - 1
    n - 2
    n - 3
    n - 4
    ...
    3
    2
    1
    I know what this is... this is the gauss sum reversed again.  
    
    Good news: the running time of selection sort is also n^2 / 2 approx.  
    
    Is this always the running time? Yes, for selection sort.
    
    For bubble sort, the best case is when the list is sorted and it takes approx n steps.  
                    the worst case is still n^2 /2 ~ n^2 steps because its quadratic
    
    

def insertion_sort(the_list):
    for i in range(len(the_list)):  # goes from 0 to n - 1, no choice
        j = i  # pull back index
        while j > 0 and the_list[j] < the_list[j - 1]: # hmm... 
            temp = the_list[j]
            the_list[j] = the_list[j - 1]
            the_list[j - 1] = temp

            j -= 1

    return the_list

    # for the best case of insertion sort, its going to take about n steps
        the reason is that the inner loop doesnt need to run
        "linear time"
    # for the worst case of insertion sort, it's going to do the same kind of thing
        as the others..
        
        
        i = 0 cant pull back 0 steps
        i = 1 can pull that element back 1
        i = 2 can pull that element back 2
        ...
        i = n - 1 can pull that element back n - 1 steps
        1 + 2 + 3 + 4 + ... + (n - 3) + (n - 2) + (n - 1) = n (n - 1) / 2 ~n^2 / 2 steps
        so it's also quadratic

    Total lesson:
        Bubble and Insertion sort can sometimes do n steps but mostly do n^2 / 2 steps
        Selection sort ALWAYS does n^2/2 steps

Merge Sort - the answer to our problems

    divides the list in half
    recursively calls merge sort on the halves
    puts the lists back together [once they've been sorted]
    
[1, 5, 9]
       |
[2, 4, 5]
          |
[1, 2, 4, 5, 5, 9] # clean up and take whatever is left in the other list
"""
def put_together(a_list, b_list):
    # these lists come in sorted
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
        total_list.append(a_list[i])

    for j in range(b_index, len(b_list)):
        total_list.append(b_list[j])

    return total_list


"""

[5, 9, 2, 8, 1, 4, 3, 7]
[5, 9, 2, 8] [1, 4, 3, 7]
[5, 9] [2, 8] [1, 4] [3, 7]
[5] [9] [2] [8] [1] [4] [3] [7] 
([5] [9]) ([2] [8]) ([1] [4]) ([3] [7])
([5, 9], [2, 8]), ([1, 4], [3, 7])
[2, 5, 8, 9] [1, 3, 4, 7]
[1, 2, 3, 4, 5, 7, 8, 9]
"""

def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    n = len(the_list)
    first_half = the_list[0: n//2]
    second_half = the_list[n//2: n]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return put_together(first_half, second_half)  # merging together n elements, takes about n steps

"""
How many times does the recursion call? lg(n) = log_2(n)

n * lg(n) = total runtime of the algorithm.  

256 -> divides 8 times
128 - > divides 7 times
64
32
16
8
4
2
1
"""

import time
import random

def sort_time(the_sort, a_list):
    copy_of_list = list(a_list)
    start_time = time.process_time()
    the_sort(copy_of_list)
    print(the_sort.__name__, 'took', time.process_time() - start_time, 'sec')


for x in [10, 100, 1000, 10000, 100000, 1000000]:
    big_list = [random.randint(0, x) for _ in range(x)]
    sort_time(merge_sort, big_list)