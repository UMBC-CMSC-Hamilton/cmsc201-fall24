"""
Final exam Friday 13th 6-8pm
    Rooms : TBA

Released the practice final.



"""

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
Best case, quick sort divides a list in half [pretty close to half]
O(n lg(n)) performance in the best case

Quicksort produces a problem though:

[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

pivot = 10
[ 9, 8, 7, 6, 5, 4, 3, 2, 1] 10 []
pivot = 9
[8, 7, 6, 5, 4, 3, 2, 1] 9 []
pivot = 8
[7, 6, 5, 4, 3, 2, 1] 8 []
pivot = 7
[6, 5, 4, 3, 2, 1] 7 []
pivot = 6
[5, 4, 3, 2, 1] 6 []
pivot = 5
[4, 3, 2, 1] 5 []
pivot = 4
[3, 2, 1] 4 []
pivot = 3
[2, 1] 3 []
pivot = 2
[1] 2 []
done
worst case that can happen, sorted lists, reverse sorted lists

[1, 6, 2, 5, 3, 4]
pivot = 1
[] 1 [6, 2, 5, 3, 4]
[2, 5, 3, 4] 6 []
this is actually the same problem as before

These all produce O(n^2) behavior

Problem:
    pivot is automatically picked as the_list[0]
    Is there a way to not pick the min or max? or anything close to it?
    
    Probabilistic Solution: pick the pivot at random from the list.
        Most of the time this will solve the issue.
        
        But you can also still construct weird cases
        
        [4, 3, 9, 1, 5, 2, 6]
        if you pick at random then you could theoretically accidentally pick the min or max
            then it produces bad behavior again.  
        pivot = the_list[random.randint(0, len(the_list))]
        
        the problem with the solution is that it doesnt decrease the number of bad cases.
        it hides them in a gigantic set of good cases.  
        
    Is there a way to divide a list perfectly in half every time?
        If you knew the median, you'd end up dividing the list in half "exactly."
        Generally to compute a median, you sort the list.
        [5, 2, 8, 9, 1, 4, 6, 7]
        [1, 2, 4, 5, 6, 7, 8, 9] issue is that this a chicken and egg problem
            
        Cool answer: when you take 441 you'll notice in the textbook there's a chapter on medians.
            turns out there is a recursive algorithm that gives you the median in O(n) time.  
            Partitioning (scanning the list takes O(n) time).
        O(n) + O(n) = O(n)
        f(n) <= C n
               g(n) <= D n
        f(n) + g(n) <= (C + D) n definition of O(n)
        
        If you use that algorithm:
        
        pivot = median(the_list)
        this guarantees O(n lg(n)) performance all the time, no O(n^2) anymore  
"""


"""
    Binary Search
    
    Linear Search - if you have a list and an element you scan through the list to find the element
        You have to scan every element O(n) time, linear time. 
        You can get lucky and find the the element in the list or maybe unlucky and it's at the 
        end or not in the list.  
    
    With binary search we ask "what if the list is sorted?"
    
    
        [1, 4, 5, 9, 12, 15, 21, 34, 55]
        
    Say we're searching for the element 4
    
    what is the middle element? 12 
    [1, 4, 5, 9] 
    what is the middle element? len = 4, 4//2 = 2 = index
    middle element = 5
    go left again
    [1, 4] middle = 4 
    len = 2, 2//2 = 1 at index 1 we see 4 => return True
    
    len = 17, 17//2 = 8, 
    [1, 3, 4, 6, 7, 9, 10, 11, 18, 21, 25, 29, 31, 35, 37, 42, 67, 72]
    
    middle = 18, looking for 67
    [21, 25, 29, 31, 35, 37, 42, 67, 72]
    [37, 42, 67, 72] len = 4, 4//2 = 2, middle = 67
    
    
    How many times do you have to cut a list in half before it's 1 element or 0?
    n // 2^steps = 1
    n ~= 2^steps
    lg(n) = #steps max number of things we're going to look at.  
    log(n) performs a lot better than n.  
"""

def linear_search(the_list, the_element):
    # this is the in keyword really, the_element in the_list
    for i in range(len(the_list)):
        if the_list[i] == the_element:
            return True

    return False


def binary_search(the_list, the_element):
    if not the_list:
        print('Did not find the element, got an empty list')
        return False

    middle = len(the_list) // 2

    print(the_list, middle, the_list[middle])
    if the_list[middle] == the_element:
        return True
    elif the_element < the_list[middle]:
        return binary_search(the_list[0:middle], the_element)
    else:
        return binary_search(the_list[middle + 1:], the_element)


import random
rand_list = [random.randint(0, 1000) for _ in range(80)] # list size is 20, range of the numbers is 0-1000
rand_list.sort()

print(rand_list)
x = int(input('What should we search for? '))
while x >= 0:
    binary_search(rand_list, x)
    x = int(input('What should we search for? '))

"""
lg(2n) = lg(2) + lg(n) = 1 + lg(n)
linear search: 
2n ===> 2n operations
"""

"""
Move on to the practice final


Write an expression which returns True if and only if the list scotsmen is non-empty and
 ship_of_theseus has at least 12 elements in it.  

"""
scotsmen = []
ship_of_theseus = []
# answer:
scotsmen and len(ship_of_theseus) >= 12
len(scotsmen) > 0 and len(ship_of_theseus) >= 12
"""
Write an expression which returns True if and only if the string game is either equal 
to chess or checkers (in lower case) and the board_size (a 2d list) is 8x8.  
Assume that the number of columns is the same for every row.  
"""
game = 'checkers'
board_size = []
# answer
(game == 'chess' or game == 'checkers') and len(board_size) == 8 and len(board_size[0]) == 8


"""
Write an expression that returns True if and only if the string the_semester is "over" 
regardless of case, or the integer num_assignments is 
between 5 and 13 inclusively (can be 5 and 13).
"""

the_semester = 'not over'
num_assignments = 17

#
the_semester == 'over' or 5 <= num_assignments <= 13
the_semester == 'over' or (5 <= num_assignments and num_assignments <= 13)

