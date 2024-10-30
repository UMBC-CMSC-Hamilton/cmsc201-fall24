"""
    Recursion

        A recursive function is a function that calls itself.
        There has to be a branch of logic that doesn't call itself.
            Base Case [multiple bases cases can be done]
                you have to prevent an infinite recursion.
            Recursive case [you can have multiple of these too]
                any branch of logic [if statement/elif] where the function calls itself
        In python there is a 1000 recursion depth limit.
            Recursion Error if you do.
"""

"""
    Think about the problem recursively:
        Is there one simple step that I can take that can help/determine the answer?
    Palindrome is a word or sequence of letters that is the same forwards and backwards.
        abcddcba is a palindrome. 
        abcdefg
    If we look at the first letter and the last letter, if they're the same, then it could be
        if not then definitely not. 
    Cut the first and last letter off and then ask if the middle part is also a palindrome.
    
    Base case? 
        '' or 'x' these are palindromes.
        
        abccba
        bccb
        cc
        ''
        abcdcba 
        bcdcb
        cdc
        d => also d if reversed so its a palindrome i guess
"""


def rec_pal(a_string):
    print(a_string)
    if len(a_string) <= 1:
        return True

    if a_string[0] == a_string[-1]:  # len(a_string) - 1
        rest_of_string = a_string[1:-1]
        result = rec_pal(rest_of_string)
        print(a_string, result)
        return result
    else:
        return False


s = input("recpal>> ")
while s != 'quit':
    print(rec_pal(s))
    s = input("recpal>> ")

"""
    SubsetSum
    
    Get a list:
    [3, 8, 3, 25, 9, 15]
    Get a target S = 18 = 3 + 15 => True
    
    S = 19 no, so you'd return False
    
    a_list = [5, 5, 5, 5, 5, 5, 5]
    S = 20
    
    maybe we just take or leave each number.
    but wait, that needs to be recursive
    
"""


def subset_sum(a_list, index, target):
    print('\t' * index, index, target)
    if target == 0:
        return True
    elif target < 0:
        return False
    elif index == len(a_list):
        return False

    take = subset_sum(a_list, index + 1, target - a_list[index])
    leave = subset_sum(a_list, index + 1, target)
    print('\t' * index, index, take, leave)
    return take or leave


a_list = [1, 2, 4, 8, 16]
print(subset_sum(a_list, 0, 17))
print(subset_sum(a_list, 0, 100))
b_list = [2, 3, 8, 9, 15, 32]

print(subset_sum(b_list, 0, 21))
print(subset_sum(b_list, 0, 19))

"""
binary_search 
distinguish it from linear search... well whats that?
    what the in keyword does
"""

def linear_search(a_list, element):
    for x in a_list:
        if x == element:
            return True
    return False

"""
use a trick:
    [1, 2, 5, 7, 12, 19, 21, 35, 47] target = 5, length = 9
    9 // 2 = 4
    [1, 2, 5, 7] target = 5, length = 4
    4//2 = 2
    
    [1, 2, 5, 7, 12, 19, 21, 35, 47] target = 4, length = 9
    [1, 2, 5, 7] target = 4, length = 4
           ^
    [1, 2]
        ^ --> 
        [] False
        
"""

def binary_search(the_list, target):
    print(the_list, target)

    if not the_list:
        return False

    n = len(the_list)
    if the_list[n // 2] == target:
        return True
    elif target < the_list[n // 2]:
        return binary_search(the_list[0: n//2], target)
    else:
        return binary_search(the_list[n//2 + 1:], target)


import random
test_list = [random.randint(0, 100) for _ in range(20)]
test_list.sort()

print(test_list)

print(binary_search(test_list, int(input('What to look for ? '))))
