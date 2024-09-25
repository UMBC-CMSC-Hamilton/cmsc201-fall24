"""
    Last time we were discussing while loops
        while loops are if statements on repeat

        they will continue until the condition is false
            if the condition is false the first time they skip the loop
            if the condition never gets changed (is always true) infinite loop
                infinite loops are usually to be avoided

    make a list
"""
if input('Run whiles? ') == 'y':
    new_list = []
    my_object = input('Enter something here: ')
    while my_object != 'quit':
        new_list.append(my_object)
        # often best to get the next input right before we jump back to the while
        # because the first thing that it will do is to check the condition
        my_object = input('Enter something here: ')

    print(new_list)

    new_list = []
    my_object = ''
    while my_object != 'quit':
        my_object = input('Enter something here: ')
        new_list.append(my_object)

    print(new_list)


    x = 2
    while x != 0:  # only checks here, doesnt know about anything else
        x = int(input("Tell me an int "))
        print(x)  # x is 0!
        # this block of code here can be as long as you want
        # the while condition never gets checked until you jump back to the start
        x = int(input("Tell me an int again "))


    """
        How do we remove objects from lists?
            2 ways
                list.remove(x)
                    removes by element
                del list[index]
                    removes by index
    """

    my_list = ['a', 'r', 't', 'q', 'o', 'k', 'v', 'a', 'b', 'r', 'r', 'a', 'q']
    my_list.remove('a')   # only removes the first a that it finds, leaves all the others
    print(my_list)

    # danger: the element must be in the list
    letter = input('Enter a letter: ')
    # this will only execute if the letter is in the list, otherwise it skips
    # totally legal, totally safe and good
    if letter in my_list:
        my_list.remove(letter)
        print(my_list)
    else:
        print('That was not in there. ')

    # future python
    try:
        my_list.remove(letter)
        # if there's more code here
        # it gets skipped
    except ValueError:
        print('oops')

    """
        remove all of the elements with a particular value
    """

    letter = input('Tell me a letter and we will remove all of it: ')
    while letter in my_list:
        my_list.remove(letter)
        # probably not going to print while its working, just print at the end
        print(my_list)

    """
        del list[index]
            this just removes whatever is at that index
            worry about index errors
    """

    random_list = ['garage', 'picture', 'quest', 'house', 'word', 'byte', 'bit', 'data']

    # priming the pump
    index = int(input('What index do you want to remove? '))
    """
        We need to check the indices that the user enters
        
        -1 is called a sentinel value
    """
    while index != -1:
        if 0 <= index < len(random_list):
            del random_list[index]

        print(random_list)
        index = int(input('What index do you want to remove? '))


    """
        Avoid remove or delete by creating a new list - a different way of thinking about 
            removing things
    
        
    """

    my_string = 'hello there'
    print(my_string)
    # probably what you meant was delete some_list[index] not just delete some_list
    del my_string  # deletes the variable name my_string from the rest of the program
    # print(my_string)  # generates a name error

"""
    strings, immutability and slices

        you can access strings by their index but you can't edit a string by its index
"""

new_string = 'symphony'
print(new_string[4], new_string[7])
#  new_string[4] = 'quest'
#  this is called immutability strings in python are immutable = cannot be changed

# what do i do?
my_string_list = list(new_string)
print(my_string_list)  # takes a string and it outputs a list of characters
# but lists are mutable
my_string_list[4] = 'q'
print(my_string_list)

# empty string.join(my_string_list)
print('**'.join(my_string_list))

list_of_strings = ['erstwhile', 'therefore', 'thence', 'wherefore', 'however']
print('$'.join(list_of_strings))
print(', '.join(list_of_strings))
print('\t'.join(list_of_strings))

"""
strip() - removes whitespace from the input
    '  word'
    'word '
    ' word '
    whitepace is basically tabs, newlines, carriage returns
        \t, \n, \r, [space]

split() - 

"""


tell_me = input('Tell me something:')
print(tell_me.strip())

random_star_string = '*************what are we doing?*****************************'
# do test this
print(random_star_string.strip('*'))

# testable but 'rare'
random_other_string = '*=**=*=*=*=*=**=========*=*=*==*=what are we doing?*=*=*=*==*=*=*=*=*=*=*=*=*=*=*=**************'
print(random_other_string.strip('*='))

"""
.split() works very similarly to strip, except that it splits the string into a list of strings
    it splits by whitepsace.  
"""

my_string = 'let\'s make a \n\n\t\t string'
print(my_string.split())

"""
split also works on things that are not whitespace
"""
my_string = "what:would:you:ever:do:this:for?"
print(my_string.split(":"))

