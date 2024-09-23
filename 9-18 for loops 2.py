"""
How do we write a for loop?
"""
if False:
    for x in range(3, 20):
        if x % 5 == 3:
            print(x)

    """
        remember that range has three arguments:
        
        range(start = 0, stop, step = 1)
        range(start, stop)
        range(stop)
        
        inclusive of the start, exclusive of the stop
    """

    """
    how do lists work?
    
    """

    another_list = ['string', 'thing', 'sing', 'ring']
    mixed_lists = [True, 'random', 'hi', 3, 5.7, -2, 'something else', False]

    for thing in mixed_lists:  # for each loop because we're looking at elements
        print(thing * 2)

    # for thing in mixed_lists:
    #    print(thing + 2)

    """
        for each - use elements
        
        for i - use indices
    """
    my_list = [3, 4, 2, 19, 3, 34, 21]

    for i in range(len(my_list)):
        print(i, my_list[i])

    print(my_list[2], my_list[5], my_list[6])
    # print(my_list[224]) produces an index error

    my_var = int(input('What index do I access? '))
    if 0 <= my_var < len(my_list):
        print(my_list[my_var])
    else:
        print(f'That is out of bounds you selected index {my_var}')

    # negative indices count from the back of the list -1 = last element, -5 5th from last
    print(my_list[-1], my_list[-2], my_list[-5])

    """"
     How do you modify a list?
     
     You use the index and then assign
    """

    my_fav_nums = [0, 0, 0, 0, 0]

    for i in range(len(my_fav_nums)):
        my_fav_nums[i] = int(input('Tell me a number: '))

    print(my_fav_nums)

    new_list = []
    new_length = int(input('How long do you want the list to be? '))

    print('boring length: ', len(new_list))
    for i in range(new_length):
        num_str = input('Tell me a new number: ')
        num = int(num_str)
        new_list.append(num)

    print(new_list)

    x = 3
    x += 5
    print(x)
    x = 'silly string'

    # for each way to scan through a string
    for char in "my random string":
        print(char)

    mrs = 'my random string match magnificient me'
    for index in range(len(mrs)):
        if mrs[index] == 'm':
            print(mrs[index], index)

    """
        What is a palindrome?
        
            word or set of letters that is the same forwards and backwards
            
            racecar
            tacocat
            mom 
            dad
            a man a plan a canal panama
    
            ask the question:
                is the ith thing in the string the same as the ith thing from the end?
                my_string[i] gets the ith thing. nice.
                
                my_string[len(my_string) - 1 - i]
                 01234
                'hello'
    """

test_pal = input('Enter a string to check as a palindrome: ')

is_pal = True

for i in range(len(test_pal) // 2):
    # print(i, test_pal[i], test_pal[len(test_pal) - 1 - i])
    if test_pal[i] != test_pal[len(test_pal) - 1 - i]:
        is_pal = False

print(test_pal, is_pal)

"""
What is a prime number?
    n is prime if its only [positive] factors are n and 1, not 1

"""
test_prime = int(input('Tell me a prime number: '))

is_a_prime = True

if test_prime != 1:
    for i in range(2, test_prime):
        if test_prime % i == 0:
            is_a_prime = False
    if is_a_prime:
        print(f'{test_prime} is prime')
    else:
        print(f'{test_prime} wasn\'t a prime')
else:
    print('1 is defined as a non-prime')

sample_list = [3, 5, 4, 3, 2, 4, 5, 6, 5]
found = False
check_for = int(input("What should we search for? "))
for x in sample_list:
    if x == check_for:
        found = True

print(found)

print(check_for in sample_list)

"""
count vowels in a string
"""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
my_string = input('Tell me a string: ')

vowel_count = 0
for char in my_string:
    # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
    if char.lower() in vowels:
        vowel_count += 1

# if char == 'a' or 'e' or 'i'...  is the char == 'a or is 'e' True or is 'i' True (yes)
print(vowel_count)

big_list = [3, 2, 3, 4, 5, 3, 3, 4, 5, 4]
print(len(big_list))
