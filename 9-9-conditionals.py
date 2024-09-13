"""
SFTP = secure file transfer protocol (port 22)
SSH = secure shell
telnet = earlier version of ssh
"""

"""
Conditions - if statements
    
    Last time we discussed print and input
    
    We need the ability to "branch" do different things based on the state of the program
    
    How do we write an if statement in Python?
    
    Use : 
        if [condition]:
            [all the code that runs in the if statement gets tabbed once]
"""
if False:
    # assignment operator (single equal sign)
    x = int(input('Tell me an integer: '))

    if x > 0:
        print(f"{x} is positive")

    # conditional equality operator (double equal sign)
    if x == 0:
        print('x is zero')

    if x < 0:
        print(f'{x} is negative')

    """
        |x| = x if x >= 0
              -x if x < 0
    """

    value = int(input('Tell me a value: '))
    if value < 0:
        value = (-1) * value

    print(f'The current value is {value}')

    word = input('Enter a word: ')
    if word.lower() == 'hello' or word.lower() == 'goodbye':
        print('That is a greeting/farewell of some kind. ')

    y = float(input('Tell me a float: '))

    if y / 3 == 1/3:
        print('it is')

    while word != 'quit':
        if word < "hi":
            print('word is less than hi whatever that means')
        word = input(">> ")

    """
        We can test if a number is even or odd
        
        We need to use "mod" modulus division
        
        n / d  25 / 5 or 17 / 3 or 179 / 13
        25 // 5 = 5 R 0
        17 // 3 = 5 R 2
        179 // 13 = 13 R 10
        
        If you do a division you can use floating point division : /
         or you can use integer division                         : //
         One more thing, modulus division                        : %
            It returns the remainder from integer division
            
        179 % 13 = 10
        17 % 3 = 2
        5 % 2 = 1
        8 % 2 = 0
        
        Is 0 even, odd, neither?
            0 is even, not positive or negative
        Even n % 2 == 0
        Odd  n % 2 == 1
    """

    parity = int(input('Enter a number: '))
    while parity != -1:
        if parity % 2 == 0:
            print('The number is even.')
        else:
            print('The number is odd')

        parity = int(input('Enter a number: '))


"""
Escape Sequences in Strings
    \n = newline
    \r = carriage return
    \t = tab
    \\ = single backslash

    \", \'
"""
print('Caesar said \'Et Tu Brute\'')
print("Someone said \"hi\"")
print('this is the worst, isn\'t it?')

print('hi\nsomething\t\t12345')

print('hello-there', end='')
print('\rrobot')

"""
    Carriage returns vs newlines [windows vs everyone else (mac/linux))]
    
    In windows, they actually encode a newline as \r\n
    In macOS and Linux it's just \n no \r 
"""

"""
    Logical Operators
    
        and, or, not
        
        not X
        X       not X
        True    False
        False   True/
        
        and = both symbols must be true
        X \ Y   True     False
        True    True     False
        False   False    False
        
        or = inclusive or = one the other or both can be true
        X \ Y   True     False
        True    True     True
        False   True    False
        
        ^ = caret [bitwise exclusive or]
"""