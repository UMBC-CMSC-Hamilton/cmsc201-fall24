"""
Get bitvise if you're on windows
Get cyberduck if you're on mac

sftp/ssh into gl.umbc.edu -> password -> dual auth

Drag drop files

Right click on the project and open the directory, drag drop from there
"""

"""
Currently we have input and print, every program we write is entirely linear.
    We need a way to branch depending on what the user does or maybe some program state.
    
    
if [condition]:
    [all code to be tabbed in by one place]
    [if its not then ... it's outside of the if statement]

"""
# print(5/0) ZeroDivisionError
if False:
    x = int(input('Tell me a number: '))

    if x > 0:
        print(f'{x} is positive')

    if x == 0:
        print('x is zero')

    if x < 0:
        print(f'{x} is negative')


    word = input('Tell me a word: ')

    """
    String checking is case sensitive because the encoding scheme is case sensitive
    
    You can use .upper() or .lower()
    """
    if word.lower() == 'robot':
        print('robots attack')

    print('hello 13245 HELLO !@#%'.lower())

    y = int(input('Tell me another number: '))

    """
        In python, the logical operators are actually the words and, or, & not
        
        and
        X \ Y   True    False
        True    True    False
        False   False   False
        
        or [inclusive or]
        X \ Y   True    False
        True    True    True
        False   True    False
    
        ^ (bitwise exclusive or, generally not used, but who knows)
        
        not [unary operator]
        
        X       True    False
        not X   False   True
        Anything is either true or false [law of the excluded middle]
        
    """
    if x > 20 and y > 5:
        print('yep the condition works')

    if x or y > 0:
        print('conditional 1 executed')

    if x > 0 or y > 0:
        print('conditional 2 executed')


    """
        integers and floats:
            0 = False, anything else => True
        strings:
            '' = empty string = False
            anything else = True
            Silly note:
                '   ' = not empty
        None = special variable in python => False
    """

    """
    else if => elif
    you can chain conditionals together, start out with an if statement
        after that if the first if statement is false you check the next elif
    else / elif
    
        rule: you can have as many elif statements as you want, but only one will ever execute
    """
    menu = int(input('Enter 1 to 5: '))

    while menu != 5:
        if menu == 1:
            print('Starting Game...')
        elif menu == 2:
            print('Saving Game...')
        elif menu == 3:
            print('Loading Game...')
        elif menu == 4:
            print('Settings')
        elif menu == 5:
            print('Exiting...')
        menu = int(input('Enter 1 to 5: '))


    x = int(input('Tell me a number: '))

    if x > 0:
        print('x was positive')
    elif x == 5:
        print('x is 5')
    """
        Remember that you generally want to put the most specific cases first
        the more general cases later [you dont want to catch the specific case
        in a big block of general cases and lose it]
    """
    if x == 5:
        print('x is 5')
    elif x > 0:
        print('x was positive')

x = int(input('Tell me a number: '))
y = int(input('Tell me a number: '))

if x == 0:
    print('x is zero we are not going to divide')
else:
    print(y/x)
"""
else means that all of the if/elif block is false
    it will execute in that condition.
you don't always need an else, many times you don't
but if you need to do something
"""

"""
/ = floating point division
17 / 3 = 5.66666666
// = integer division
17 // 3 = 5

mod = modulus division is the remainder after an integer division

17 // 3 = 5 R 2

17 % 3 = 2 [mod gives us the remainder of the number when we divide.]
7 % 2 = 1
16 % 4 = 0

n // d

n = d * q + r
    Rule: 0 <= r < |d|
    
-5 = (-1) * 4 - 1
-5 = (-2) * 4 + 3 
"""

print(-5 % 4)
