"""
Final exam will be Friday 13th 6-8 pm, rooms to be announced soon.

    Final = Midterm 1 + Midterm 2 + Hex + Sorting.
        Length will be about Midterm 2


Asymptotic Analysis:

    When we solve problems, the amount of time it takes is usually dependent on the input size
        of the problem.

    Sorting is always a good example => well i know that bubble sort takes n^2 steps if
        the list is of size n.

    Merge Sort takes n lg(n) steps to sort a list.  Instead of taking 1000 -> 10000

    10000 * log(10000) / [ 1000 * log(1000) ]
    10 * log(10000) / log(1000) = (4/3) * 10 = 13.3333 ...

    10^6 * log(10^6) / (10^5 * log(10^5)) = 10 * 6/5 = 12


    We want to understand how the runtime of algorithms increases as the input size increases

    Bubble Sort, SelectionSort, InsertionSort all run in worst case n^2 steps [n^2 time]

    SelectionSort always runs in n^2 steps (approx), both its best and worst cases

    BubbleSort can run in about n steps but will probably do n^2 steps most of the time
        if the lists arent sorted.
        Best case is a sorted list that runs in n steps [approx] Omega(n)
        worst case is a random garbage list or reverse sorted -> n^2 steps  O(n^2)


Focus on O(g(n)) notation.  Called big-O.
    Stolen from number theory by Don Knuth.


How many steps does a computer do in a second?
    Problems with this question:
        We all have different computers (different processors, different amounts of ram, different bus speeds)
        This is why we don't count in time we count in steps.
        not all steps are the same, * way more expensive 8x more than +/-
        Division is probably 2x as expensive as *

    Moral of the story here: this is complex.  Benchmarks are useful but not always exactly informative.


Solution:
    if you have an algorithm that takes 5n^2 steps
        and another that takes 3 n^2 steps which is faster?
        You cant trick me... that is a trick question.

    Want a mathematical process that focuses on the leading term of the increase in time
        and it ignores constants.  Considers 3n^2 and 5n^2 "the same class"

    Define Big-O to be this:

f(n) is O(g(n)) when there exists (there are) constants C, N such that
f(n) <= C g(n) for n >= N.

Ex:
    5n^2 is O(n^2)
    Good news: we get to pick this constant C.
    C = 5
    C = 17 also works
    C = 2004 definitely works
    C != 4 (doesn't work)
    5n^2 <= C * n^2

    5n^2 is O(n^2) [think: 5n^2 is a member of the class of quadratic functions]
Ex:
    2n^2 + 3n + 5 <= 2n^2 + 3n^2 + 5n^2 = 10 n^2
    All true except in the region (-1, 1) or n = 0

    We can set N as well.  [Think: N means after this point, or eventually]
    N = 10

Ex: 5 n * log(n) + 7n is O(n log(n))
5n log(n) + 7n <= C n log(n)
C = 6
N = 10,000,000
Even if you set C = 100,
log(0) = -infinity or undefined
N >= 1 get away from the log(0) happening


n^3 / (n - 5) is O(n^2)

n^3 / (n - 5) <= 2n^2
Proof:
n^3 < 2n^2 (n - 5) = 2n^3 - 5n^2
Set C = 2
N = 6 [or something]

Idea of the mathematics is that you can adjust C and N until the equation is true.

is it true that n^4 is O(n^3)? no

n^4 <= C * n^3
divide by n^3
n <= C [contradiction]
This statement is false so n^4 is NOT O(n^3)


We get to say things like Bubble Insertion and Selection sort are all O(n^2)
Merge sort is O(n lg(n)) this class is 'superior' to O(n^2) because it grows slower
    the amount of time of any algorithm in the n lg(n) class will eventually beat an n^2 alg.
"""


def get_middle_element(a_list):
    """
        Constant time algorithm (it runs the same steps regardless of the input size)
    """
    if not a_list:
        return 0

    return a_list[len(a_list) // 2]


"""
    QuickSort
    
    How does it work?
        split a list but in half [that's merge sort]
        pick a pivot, pivot = the first element in the list
        partition anything less goes into a less_list anything greater(or equal) goes into
            the greater list.  
        recursively sort the less and greater lists
        answer:
            return less_list + [pivot] + greater_list
    
    
    [5, 8, 9, 1, 3, 7, 4, 5, 2]
    pivot = 5
    [1, 3, 4, 2] 5 [8, 9, 7, 5]
    
    [1, 3, 4, 2]
    pivot = 1
    [] 1 [3, 4, 2]
    QS [3, 4, 2]
    pivot = 3
    [2] 3 [4] => [2, 3, 4] => [1, 2, 3, 4]
    
    QS [8, 9, 7, 5]
    pivot = 8
    [7, 5] 8 [9]
    pivot = 7
    [5] 7 []
    
    Pivot doesn't live in either of the two lists avoids infinite recursion.
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
imagine it splits the list in about half each time

    n / 2^divisions ~= 1
    n ~= 2^divisions
    lg(n) ~= divisions (steps)
    
    the number of steps we're doing per division is n [we have to partition all the elements again]

    Total : n lg(n)
    
    
What happens on a sorted list?

[1, 2, 3, 4, 5, 6 ,7, 8]
pivot = 1
[] 1 [2, 3, 4, 5, 6, 7, 8]
pivot = 2
[] 2 [3, 4, 5, 6 ,7, 8]
[] 3 [4, 5, 6, 7, 8]
[] 4 [5, 6, 7, 8]
[] 5 [6, 7, 8]
[] 6 [7, 8]
[] 7 [8]

Total cost: n^2

Problem with QS: most of the time it's great, works faster than merge.  But in a very simple condition
    where the list is sorted, then it produces its worst case.  
"""



import random

for _ in range(20):
    sort_list = [random.randint(0, 100) for _ in range(1000)]
    if quick_sort(sort_list) == sorted(sort_list):
        print('Yep')
    else:
        print('aaugh')