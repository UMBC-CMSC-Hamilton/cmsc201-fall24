"""
    while loops are if statements with repeat turned on

        while [condition]:
            code
            code
            code

        if the condition is false the first time you enter you get a skipped loop
        if the condition is always true => infinite loop
            and there's no logical way to change that to false

"""

while input('Enter x') != 'x': pass

"""
    how do we remove things out of lists?
    
        my_list.remove(x) => removes by element
            finds the first instance of the element and removes it from the list
            
        del my_list[index] => removes by index
        
        
"""
if False:
    letters = ['a', 't', 't', 'q', 'q', 'v', 'q', 'a', 'r', 's', 'q', 'b', 'f', 'r', 'e', 'q']
    letters.remove('t')
    print(letters)

    rem_letter = input('Tell me the letter to remove: ')
    if rem_letter in letters:
        letters.remove(rem_letter)
        print(letters)
    else:
        print('That wasn\'t in the list.')


    rem_all = input('What letter do you want to remove all of them? ')
    while rem_all in letters:
        letters.remove(rem_all)
        print(letters)

    """ future python """
    rem_third = input('What letter do you want to remove [try except]? ')
    try:
        letters.remove(rem_third)
        print(letters)
        x = 0
    except ValueError:
        print('That letter was not in the list. ')
        x = 0
    except IndexError:
        pass
    """
    x = 0
    try:
        x = y + 3
    except NameError:
        print('Y was not defined')
    """

    """
    other remove method: 
        
    del my_list[index]
    """
    my_list = ['blue', 'sentinel', 'magic', 'unset', 'premade']
    print(my_list)
    del my_list[2]

    the_index = int(input('What index should we remove? '))
    print(my_list)
    if 0 <= the_index < len(my_list):
        del my_list[the_index]
        print(my_list)
    else:
        print('That was out of bounds, I saved you from an IndexError. ')

    big_list = []
    for i in range(100):
        big_list.append(i + 1)
    """
    print(big_list)
    for i in range(len(big_list)):
        if big_list[i] % 5 == 0:
            del big_list[i]
            print(big_list)
    """

    i = 0
    while i < len(big_list):
        if big_list[i] % 5 == 0:
            del big_list[i]
            print(big_list)
        i += 1


    letter_list = ['a', 'b', 'b', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'b', 'a']
    for i in range(len(letter_list)):
        if i < len(letter_list) and letter_list[i] == 'a':
            letter_list.remove('a')
            print(letter_list)

    print('final')
    print(letter_list)

    new_list = []
    for i in range(len(letter_list)):
        if letter_list[i] != 'a':
            new_list.append(letter_list[i])
    print(new_list)

"""
    string immutability
        strings cannot be modified
"""
my_string = 'sandwiches'
# my_string[5] = 'q' so then what?
my_str_letters = list(my_string)
print(my_str_letters)
my_str_letters[5] = 'q'
print(my_str_letters)

print(''.join(my_str_letters))  # join takes an argument which is a list of strings
# starting string is called the separator
print(', '.join(['happy', 'turtles', 'together', 'life']))
sep = " :: "
print(sep.join(['penny', 'lane', 'dove', 'wordle']))

"""
    strip()
        string.strip() => removes whitespace from the beginning and end of the string
        string.strip('a') => removes all of the 'a' from the start and the end
        string.strip('%^&*') removes all %^&* from the string's front and back
        lstrip
        rstrip
    split()
        string.split() => splits the string on whitespace creates a list
    
        
"""
print("\n\n\t\thello there\tmaybe something else                           \t         ".strip())

print('a                         b'.strip())
print('========================================Section Header================================'.strip('='))

print('=*=*=*=*=*=*=*=*=*=*=*=======***** Section Header *****====*=*=*=*=*=*=*=*=*=*=*=*='.strip('=* '))

print('Once upon a time there was a baby processor, it could add but not multiply.'.split())
print('Hello                                           There'.split())

print('abaabbaabbabababababa'.split('a'))

save_command = 'System.out.println("something")'.split('.')
print('->'.join(save_command))
"""
split and join are inverse functions, they do the opposite things
"""