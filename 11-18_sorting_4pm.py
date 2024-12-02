"""
    Sorting - https://visualgo.net/en/sorting
        A bunch of different algorithms that will take an unsorted list and make it sorted.

        Bubble Sort
        Selection Sort
        Insertion Sort

    Idea:
        What if we swap adjacent elements if they're out of order. Scan through the list.

        2, 9, 1, 8, 7, 3 look at 2 9 no swap
        2, 9, 1, 8, 7, 3 look at 9 1 => swap
        2, 1, 9, 8, 7, 3 look at 9 and 8 => swap
        2, 1, 8, 9, 7, 3 look at 9 and 7 => swap
        2, 1, 8, 7, 9, 3 look at 9 and 3 => swap
        2, 1, 8, 7, 3, 9 closer.... let's do it again

        1, 2, 7, 3, 8, 9 after the next loop through the process we end up with this
        do it one more time
        1, 2, 3, 7, 8, 9 it is sorted
"""

import random
import time


def bubble_sort(the_list):
    """
        Idea: we're going to go until the list stops swapping
            We're going to track it with a boolean flag.
    """
    swapped = True  # setting up the variable to get into the loop the first time
    while swapped:
        swapped = False
        # print(the_list)
        for i in range(len(the_list) - 1):  # first scan costs us n operations, but if its sorted, then that's it
            if the_list[i] > the_list[i + 1]:
                swapped = True

                temp = the_list[i]
                the_list[i] = the_list[i + 1]
                the_list[i + 1] = temp

    return the_list


bubble_list = [random.randint(0, 100) for _ in range(7)]
print(bubble_list)
bubble_sort(bubble_list)
print('Final: ', bubble_list)

"""
    Idea of Selection Sort:
        What if you get the minimum and put it at the front...
        What if you get the next min and put it at index 1
        What if you get next-next-min and put it at index 2....
        keep doing that until you're done
"""


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


sel_list = [random.randint(0, 50) for _ in range(15)]
selection_sort(sel_list)
print(sel_list)

"""
    insertion sort - like bubble sort but instead of shifting elements up, it pulls them back
        "pull back sort"
"""


def insertion_sort(the_list):
    for i in range(len(the_list)):
        j = i  # pull back index
        while j > 0 and the_list[j] < the_list[j - 1]:
            temp = the_list[j]
            the_list[j] = the_list[j - 1]
            the_list[j - 1] = temp

            j -= 1

    return the_list


i_list = [random.randint(0, 100) for _ in range(13)]
print(i_list)
insertion_sort(i_list)
print(i_list, i_list == sorted(i_list))


def sort_time(the_sort, a_list):
    copy_of_list = list(a_list)
    start_time = time.process_time()
    the_sort(copy_of_list)
    print(the_sort.__name__, 'took', time.process_time() - start_time, 'sec')


for x in [10, 100, 1000, 10000, 100000]:
    big_list = [random.randint(0, x) for _ in range(x)]
    sort_time(bubble_sort, big_list)
# sort_time(selection_sort, big_list)
# sort_time(insertion_sort, big_list)