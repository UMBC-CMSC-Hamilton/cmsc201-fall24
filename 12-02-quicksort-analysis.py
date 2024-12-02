"""
Dec 13th Friday 6-8 pm. Final Date and Time

Rooms to be announced soon.

"""

"""
what is asymptotic analysis?

    Algorithms or programs take certain amounts of time depending on the input size.
        Think: sorting (bubble, selection, insertion => n^2 steps for a list of size n)
            

what is big-O?


"""

def mat_mul(a_mat, b_mat):
    """
        For two things of size n x n it takes n^3 steps
    """
    c_mat = [[0 for _ in range(len(b_mat[0]))] for _ in range(len(a_mat))]
    for i in range(len(a_mat)):         # outer loop also executes n times (n * n * n total = n^3 steps)
        for j in range(len(b_mat[0])):  # next loop executes n times (inner executes n^2)
            for k in range(a_mat[0]):  # inner loop goes n times
                c_mat[i][j] += a_mat[i][k] * b_mat[k][j]
    return c_mat


def is_prime(n):
    """
        if n == 25, sqrt(25) = 5
        range(2, 5 + 1)
        n ** (1/2) = sqrt(n)
        runs about sqrt(n) - 2 steps
    """
    for x in range(2, int(n ** (1/2)) + 1):
        if n % x == 0:
            return False

    return True

"""
    Some number theorists invented a notation that helps us here.
        
    Every computer runs differently.
        Every computer has a different processor, different ram, different OS potentially
            x64 arch vs arm vs risc-V
    If my algorithm does two times the number of steps that yours does, is yours better?
        Maybe. It depends on the actual speed of each instruction/step.
    
    5n^2 "steps"
    3n^2 "steps" which is faster?
    I dont know.  Answer: race them against each other and time it.  
    
    Big-O solves this problem by classing different runtimes together, classes them by their
        asymptotic behavior (n -> infinity).
    
    If you have an O(n^2) algorithm what we're saying is that as you increase the data set by
        a factor 'f' you increase the runtime by a factor f^2
    
    If you have an O(n lg(n)) algorithm, same thing, except if you increase by a factor f
        f * lg(f)
        

Definition of O(g(n))

f(n) is O(g(n)) when there are constants C, N so that :
f(n) <= C * g(n) for n >= N.

What does it mean?

    We get to pick C and N
    C = a multiplying factor to allow us to ignore the difference between
        3n^2, 6n^2, 200n^2 all n^2 type algorithms.  
        
        
    g(n) = n^2
    C = 3, C = 6, C = 500
    200n^2 <= 500n^2
    
Example:
    2n^2 + 5n + 1 is O(n^2)
    <= 2n^2 + 5n^2 + n^2 = 8n^2 pick C = 8
    <= 8 n^2 there we go.  

    Issue: n = 0 it's false [annoying, not useful at all but mathematically true]
    2(0^2) + 5(0) + 1 <= 8 * 0^2 no
    1 <= 0 nope so what do we do?
    Set N = 1 or N = 10 or N = 2 get past 0
        Think about N as "eventually" there is some point where this formula becomes true
            stays true afterward.  
            
    when you set n = 0, you get the problem, not a big problem.  We probably don't care how fast
    the algorithm runs on a size of 0.  
    
    
    5 n * lg(n) + sqrt(n) < 10 * n * lg(n) => n lg(n) Choose C = 10.
    
    N = 2 push yourself away from the asymptote and then everything works.  
    N = 0, lg(0) = undefined or -infinity or something equally useless.  
        
    Again that's why the definition gives us some kind of way out of that.
        N is the starting point so we don't have to worry.  
        
    
    Big-O is used for worst case analysis in general to show us the upper bound of how much time
        we expect to take.  
        
    the other reason why big-O matches with worst case is that it uses the <= symbol.
    
    time(algorithm) <= C * the function we are using to describe it [that's what we mean by worst case]
    

Best Case:
    Big-Ω
    
    All basically the same as Big-O the difference is that we flip <= into >= 
    
    f(n) is Ω(g(n)) when there are constants C, N so that
        f(n) >= C g(n) for n >= N
    g(n) bounds the runtime from below, it has to be at least what we're saying or bigger
        therefore it is a "best case" analysis. 


    BubbleSort best case is Ω(n) and the worst case is O(n^2)
        Bubble sort scans through the list the first time, and if it is sorted, it exits
            the while loop. That is where the best case comes in.  
    Same for insertion sort.  You scan through and do not do any swaps so you never execute the
        inner while loop inside of the for loop in the insertion sort.  
        
    Selection sort always goes Ω(n^2) AND O(n^2) because they always run in the same time
        there's not really any choices or ways to shortcut the algorithm.  
        
    
    351
    175 (176)
    87 (88)
    43 (44)
    21
    10
    5
    2
    1
    
    lg(351) = 8 (8 to 9) = 8.45 ~ 8 or 9
    log_2(n) = 
    
    ln(x) = log_e(x)
    log(x) = log_10(x)
    
    ln(n)/ ln(2) = lg(n)
    log(n) / log(2) = lg(n)
    
    Base Change in Logs:
        log_a(x) = log_b(x) / log_b(a)
        
    
    merge sort: O(n lg(n)) steps
    
"""

"""
    quicksort - worst O(n^2) best Ω(n lg(n))
    
    how does quicksort work?
    
    Idea: you pick a pivot (the first element of the list)
    
        Kind of like merge sort (divides the list in half)
        partitions the list into two parts
        less_list            greater_list
        if the element you look at is less than the pivot it goes into the less list
        if the element is greater than or equal to the pivot it goes into the greater list.
        
        # now that we have two lists, we quicksort both of the lists
        when it comes back, the two lists are sorted and then we dont need to put them together
            in the same way as merge sort does
            we can just concatenate them.
            [3, 6, 8, 9]  12  [14, 15, 16, 17]
            
    
    Example of quicksort:
    
    [4, 8, 2, 7, 9, 1, 5, 6]
    pivot = 4
    [2, 1] 4 [8, 7, 9, 5, 6]
    quicksort [2, 1]
    pivot = 2
    [1]  2  [] greater is empty here
    ==> [1, 2] (one side done)
    
    quicksort [8, 7, 9, 5, 6]
    pivot = 8
    [7, 5, 6] 8 [9]
    quicksort [7, 5, 6]
    [5, 6] 7 []
    quicksort [5, 6]
    pivot = 5
    [] 5 [6]
    
    [5, 6] 
    [5, 6, 7]
    [5, 6, 7, 8, 9] other half done
    
    [1, 2] 4 [5, 6, 7, 8, 9]
"""


def quicksort(the_list):
    if len(the_list) <= 1:
        return the_list

    pivot = the_list[0]
    less_list = []
    greater_list = []

    for i in range(1, len(the_list)):
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])

    less_list = quicksort(less_list)
    greater_list = quicksort(greater_list)

    return less_list + [pivot] + greater_list

"""
What's good about this?
    it has n lg(n) running time most of the time as good as merge sort (often outperforms merge sort a bit)
    
What's bad about this?
    [1, 2, 3, 4, 5, 6, 7, 8]
    pivot = 1
    [] 1 [2, 3, 4, 5, 6, 7, 8]
    pivot = 2
    [] 2 [3, 4, 5, 6, 7, 8]
    pivot = 3
    [] 3 [4, 5, 6, 7, 8]
    pivot = 4
    [] 4 [5, 6, 7, 8]
    pivot = 5
    [] 5 [6, 7, 8]
    pivot = 6
    [] 6 [7, 8]
    pivot = 7
    [] 7 [8]
    
    Each one of these steps costs 'about' n operations and there's n steps
    n^2 steps
    more technically its actually 1 + 2 + 3 + 4 + ... + n = n(n + 1)/2 steps [O(n^2)]
    
"""