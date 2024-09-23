"""
 For loops:

    for var_name in [list, string, range]:

        range(stop)
        range(start, stop)
        range(start = 0, stop, step = 1)

"""

for i in range(4, 25, 3):
    print(i)

for j in range(0, 100, 5):
    print(j)

"""
How do lists work?

    lists are collections of data
        lists can contain integers, floats, bools, strings, other things
        lists have indices and length 
"""

my_list = ['a', 'c', 'r', 'p', 'q', 's', 'w']

print(len(my_list))

"""
What is the purpose of a list?
    customer_1
    customer_2
    customer_3
    customer_jim

    We can have multiple variables and access them by an integer index
"""

my_index = 3

print(my_list[1], my_list[4], my_list[6])
# you can use variables as indices, you can do algebra inside of them.
print(my_list[my_index], my_list[my_index + 1])
# if you have my_index + 1 think "this is the next thing"

# IndexError, so let's comment it out
# print(my_list[77])

"""
two ways to scan through a list:

    for each loop - getting elements
        for some_element in the_list:
    for i[ndex] loop - getting indices
        for some_index in range(len(some_list)):
"""
#               0    1   2   3    4    5    6
numbers_list = [12, 15, 72, 113, 184, 273, 441]
for x in numbers_list:  # x is actually an element inside of the list, not an index
    if x % 3 == 0:
        print(x)

# i is an index not an element in the list, to access we must use the array brackets / list brackets
for i in range(len(numbers_list)):
    if numbers_list[i] % 3 == 0:
        print(numbers_list[i])

"""
    Tricky: variable name doesn't matter, whether you use the indices or elements,
        if you have range(len(a_list)) -> for i
"""

my_words = ['rest', 'api', 'aviary', 'apiary']
for index in my_words:
    print(index)

"""
    .append
"""
if False:
    new_list = []  # array/list brackets, probably more common
    another_list = list()  # create an empty list - constructor notation / less common

    for i in range(5):
        word = input('Tell me a word: ')
        new_list.append(word)  # you see that the list starts empty and grows as you append
        print(new_list)

    """
    Search a list for an element:
    """

    my_numbers = [2, 17, 31, 15, 15, 15, 63, 1927, 1778, 15, 17, 15, 2, 31]

    check_num = int(input('Enter a number: '))

    found_it = False
    for x in my_numbers:
        if check_num == x:
            found_it = True

    if found_it:
        print('Found it')
    else:
        print('It wasn\'t there')

    check_num = int(input('Enter a number: '))

    count_it = 0
    for x in my_numbers:
        if check_num == x:
            count_it += 1  # count_it = count_it + 1

    print(f'Found it {count_it} times')

    """
    Python has a built-in keyword that checks if something is a member of a list.
    """

    check_num = int(input('Enter a number: '))
    print(check_num in my_numbers)
    # in keyword returns True if the value is in the list, else it will return False
    # use in if statements mostly
    if check_num in my_numbers:
        print('It is there!')

    check_num = int(input('Enter a number (not example): '))
    if check_num not in my_numbers:  # do NOT use is
        print('it is NOT there! good')

    """
    palindromes
         - you can use for loops to step through strings character by character
         
         What is a palindrome? the word is the same 'forwards and backwards' 
            The word is its own reverse
            
            racecar
            tacocat
            mom
            dad
            a man a plan a canal panama
            
        check if the letter / char at index i is the same as the thing at index i from the end
        
        What is the last index in any list/ string?
         01234
        'hello'
        i starts at 0
            len(the_string) - i ==> Right idea but when i = 0 it's going to be out of bounds
        fix it by subtracting 1
            len(the_string) - 1 - i
    """

    word = input('Tell me a word: ')
    for letter in word:
        print(letter)

    for k in range(len(word)):
        print(word[k])

    is_pal = True
    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:
            is_pal = False

    if is_pal:
        print(f"{word} is a palindrome")
    else:
        print('Try again.')

"""
is prime - what is a prime number?
    a prime number is a positive integer > 0 
    a number n whose factors are 1 and n (that's it)
    
    7 % 1 = 0 ??? (even in the definition its saying skip 1)
    7 % 2 = 1 != 0
    7 % 3 = 1 != 0
    7 % 4 = 3 != 0
    7 % 5 = 2 != 0
    7 % 6 = 1 != 0

    15 % 1 == 0 ???
    15 % 2 == 1
    15 % 3 == 0 <--
    15 % 4 == 3
    15 % 5 == 0 <--
"""
the_prime = int(input('Enter a prime: '))

is_prime = True
for factor in range(2, the_prime):
    if the_prime % factor == 0:
        is_prime = False

if is_prime:
    print('Good it was.')
else:
    print('Sorry it isn\'t')

"""
    Assignment in list
"""

array = [0, 0, 0, 0, 0, 0]

for i in range(len(array)):
    array[i] = 2 ** i + 1

print(array)

array2 = [0, 0, 0, 0, 0, 0]
count = 0
for x in array2:
    x = 2 ** count + 1
    count += 1
    print(count, x)

print(array2)
