"""
Recursion

    Every recursion needs a base case (it stops the recursion from going on 'forever')
    In python, you can only have a depth of 1000 in a recursion (set the recursion limit, but we won't)

    Recursion is just when a function calls itself.
        You have to trust that the recursion call will produce the right answer
            for a given subproblem.

    Recursive palindromes
        hint: what is a palindrome?
        for us now it's going to be when the first letter matches the last letter
            and the inner part is a palindrome

        tacocat => first letter matches the last letter
            acoca => also a palindrome
            coc => palindrome
            o => this has to be

        abcddcba
        bcddcb
        cddc
        dd
        ''

        abcdeetcba
        bcdeetcb
        cdeetc
        deet => problem we'll return false
"""


def recursive_palindrome(a_string):
    print(a_string)
    if len(a_string) <= 1:
        return True

    if a_string[0] == a_string[-1]:  # same as len(a_string) - 1
        rest_of_string = a_string[1:len(a_string) - 1]
        is_it = recursive_palindrome(rest_of_string)
        print(a_string, is_it)
        return is_it
    else:
        return False


s = input('rec pal >> ')
while s != 'quit':
    print(recursive_palindrome(s))
    s = input('rec pal >> ')

"""
    subset sum
    
    [2, 8, 25, 47]
    pick a number = 10
    Can you make 10 out of these numbers (by addition)?
    2 + 8 = 10 good, you can ignore the rest
        you can add each number in the list once or zero times.
    pick a different number = 15
    you can't make 15 out of this list
    
    [1, 2, 4, 8]
    S = 11, 1 + 2 + 8
    S = 7, 1 + 2 + 4
    S = 3, 1 + 2
    S = 4, 4
    
    Can you make the given number by adding elements of the list?
    
    Either i need to to take the number of not.
        if i take the number then the sum im trying to get is S - a[i] where a[i] is that particular
            value.
    
    
    [3, 6, 12, 15]
    S = 24
    take 3, idea is that S = 21 = 24 - 3
    take 6, 21 - 6 = 15
    take 12, 15 - 12 = 3 no more ways to get to 3, then we can't do it
    leave 12, but take 15, then that works
    3 + 6 + _0_ + 15 = 24
    
    in every step we'll both take and leave the value
"""


def subset_sum(a_list, i, current):
    if i < len(a_list):
        print('\t' * i, i, current, a_list[i])
    if current == 0:
        return True
    elif i == len(a_list):
        return False

    take = subset_sum(a_list, i + 1, current - a_list[i])
    leave = subset_sum(a_list, i + 1, current)
    if take:
        print('\t' * i, 'take it', a_list[i])
    elif leave:
        print('\t' * i, 'leave it', a_list[i])
    return take or leave


print(subset_sum([1, 2, 4, 7], 0, 13))
print(subset_sum([1, 5, 10, 20], 0, 25))

"""
    
what is linear search?
    a for loop looking for an element, searches the entire list [kind of inefficient if you do a lot of searches]

binary search
    S = 2
    [1, 2, 8, 10, 20, 50, 80, 95, 102] L = 9 
    L//2 = 4
    to the left, why? sorted
    [1, 2, 8, 10] L = 4
    L // 2 = 2
    see 8 go left again
    [1, 2] L = 2, L//2 = 1
    list[L//2] == 2 found it
    
Basically it divides the list in half every time
List is of size "n" how many times might we have to look through the list?
    As many times as you can divide n by two before it's 1 or 0
    n = 100 took about 7 times
    n = 200 takes ~ 8
    n = 400 take about 9 times
    
    
    2^x, if you increase x by 1 then the number doubles
        this is the inverse of that, if you double your size you only increase the search by 1
    
    ln(x) = log_e, log = log_10
    lg(x) = log_2(x)
    
    Binary search is that it takes lg(n) steps to find or not find the element
    
"""


def search_for_x(a_list, x):
    for y in a_list:
        if x == y:
            return True

    return False


def binary_search(a_list, look_for_me):
    n = len(a_list)
    print(a_list)
    if n == 0:  # empty list, we didn't find it
        return False
    if a_list[n // 2] == look_for_me:
        return True

    if a_list[n // 2] < look_for_me:
        return binary_search(a_list[n // 2 + 1:], look_for_me)
    else:
        return binary_search(a_list[0: n // 2], look_for_me)


import random

while input('again? ') == 'yes':
    rando_list = [random.randint(0, 100) for _ in range(20)]
    rando_list.sort()

    print(rando_list)
    binary_search(rando_list, int(input('What do we look for? ')))
