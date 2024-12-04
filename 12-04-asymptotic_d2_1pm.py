"""
Final Exam:
    Friday Dec 13th, 6-8pm Rooms TBA
    Released the first practice exam
    I'll review it monday maybe a little today
"""

"""
Asymptotic Analysis
    linear search - if you want to find an element in a list, you scan the list with a for loop
        The worst case of a linear search is O(n) = linear time in the size of the list
        a lot of times theres not a way around it.  
    binary search - if you have a sorted list, you can do this process
    
        [1, 5, 9, 12, 21, 29, 32, 57, 99] 9 elements 
        say i'm looking for 5
        middle element is 21, and the list is sorted
        just look at the list
        [1, 5, 9, 12] len = 4, 4 // 2 = 2
        9 is the "middle element"
        [1, 5] len = 2, 2//2 == 1
        middle element is 5 this time and we found it.  return True up the recursive stack.  
        
        
        Every time we double the list size we do one more step in binary search.
            This makes sense: first step is going to cut the list in half.  
            Then you get down to a list which you know how many operations it will take.
            
        Given a list of size n, how many steps does it take?
        1 step on a list of size 1      2^0 = 1
        2 steps on a list of size 2     
        3 steps on a list of size 4
        4 steps on a list of size 8
        5 steps on a list of size 16
        6 steps on a list of size 32
        7 steps on a list of size 64
        8 steps on a list of size 128   2^(steps - 1)
        etc...
        
        2^steps = n
        lg(2^steps) = lg(n)
        steps = lg(n)
        This algorithm runs in O(lg(n))
        
    In conclusion:
        binary search is a lot more efficient than linear search
        requirement is that the list is sorted, and that's expensive
        O(n lg(n)) the cost of a merge sort or a good quicksort.  
        O(n) is the cost of a linear search.  
"""


def linear_search(a_list, the_element):
    for i in range(len(a_list)):
        if a_list[i] == the_element:
            return True

    return False


def binary_search(a_list, the_element):
    if not a_list:
        print('Did not find it in the list.')
        return False

    middle = len(a_list) // 2
    print(a_list, middle, a_list[middle])

    if a_list[middle] == the_element:
        return True
    elif the_element < a_list[middle]:
        return binary_search(a_list[0: middle], the_element)
    else:
        return binary_search(a_list[middle + 1:], the_element)



import random
rand_list = [random.randint(0, 1000) for _ in range(80)]
rand_list.sort()
print(rand_list)
search_for = int(input('What do you want to search for? '))
binary_search(rand_list, search_for)


def quick_sort(the_list):
    if len(the_list) <= 1:
        return the_list

    less_list = []
    greater_list = []

    pivot = the_list[0]
    for i in range(1, len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)

    return less_list + [pivot] + greater_list

"""
    Problem with quicksort:
        if you have a sorted list, reversed sorted list, or some other lists that are weird
            you'll end up not with O(n lg(n)) but O(n^2) which is the actual worst case.  
        
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        pivot = 10
        [9, 8, 7, 6, 5, 4, 3, 2 , 1] 10 []
        pivot = 9
        [8, 7, 6, 5, 4, 3, 2 , 1] 9 []
        ...
        
        n total steps (n = 10) problem is that the amount of time it takes to divide (partition)
        the list is also n, n (steps) * n(ops/step) = n^2
        
        [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        pivot = 1
        [] 1 [10, 2, 9, 3, 8, 4, 7, 5, 6]
        pivot = 10
        [2, 9, 3, 8, 4, 7, 5, 6] 10 []
        pivot = 2
        [] 2 [9, 3, 8, 4, 7, 5, 6]
        still requires n total steps to divide the list
        
        What's the fix?
            2 possible fixes... 1 is sorta not 100% guaranteed the other is
            Probabilistic Fix: super easy, pick a random pivot.
                replace
                    pivot = a_list[0]
                with
                    pivot = a_list[random.randint(0, len(a_list))]
            Better fix [a little harder]
                There is a linear time O(n) time median finder algorithm.  It's the 
                same cost as the partition for loop.  O(n) + O(n) = O(n)
                f(n) <= C n
                g(n) <= D n 
                f(n) + g(n) <= (C + D) n
                pivot = median(a_list)
                Guarantees you O(n lg(n)) performance all the time.  
                
"""

"""
Write an expression which returns True if and only if the list scotsmen is 
non-empty and ship_of_theseus has at least 12 elements in it.  
"""
scotsmen = []
ship_of_theseus = []

scotsmen and len(ship_of_theseus) >= 12
len(scotsmen) >= 1 and len(ship_of_theseus) >= 12

"""
Write an expression which returns True if and only if the string game is 
either equal to chess or checkers (in lower case) and the board_size (a 2d list) is 8x8.  
Assume that the number of columns is the same for every row.  
"""
game = 'chess'
board_size = []
(game == "chess" or game == "checkers") and len(board_size) == 8 and len(board_size[0]) == 8


"""
Write an expression that returns True if and only if the string the_semester
 is "over" regardless of case, or the integer num_assignments 
 is between 5 and 13 inclusively (can be 5 and 13).  

"""
the_semester = 'over'
num_assignments = 7
the_semester == 'over' or 5 <= num_assignments <= 13

