"""
Conditionals
if statements

    if [condition]:
        [anything you need]
        [goes in here]
        [all tabbed in by one]

    if you have a set of if statements where you only ever want one of them to run
    you can use else if

    else if is written elif
"""
if False:
    x = int(input('Enter an option 1 - 5: '))
    if x == 1:
        print('Starting Game')
    elif x == 2:
        print('Loading Game')
        x = 4
    elif x == 3:
        print('Saving Game')
    elif x == 4:
        print('Settings')
    elif x == 5:
        print('Exiting')
    else:
        print('Invalid Choice')

    print('all ifs')
    x = int(input('Enter an option 1 - 5: '))
    if x == 1:
        print('Starting Game')
    if x == 2:
        print('Loading Game')
        x = 4
    if x == 3:
        print('Saving Game')
    if x == 4:
        print('Settings')
    if x == 5:
        print('Exiting')

    """
        Standard practice to write the if statements from the most specific to the most general
    """
    x = int(input('Tell me another number: '))
    if x > 0:
        print('x is positive')
    elif x == 32:
        print('interesting')

    if x == 32:
        print('interesting')
    elif x > 0:
        print('x is positive')

    """
    Let's talk about else
    
    else is another way to end an if statement
        can put else at the end
        else will execute when ALL of the conditions are false
    
    """

    a = int(input('Tell me the numerator: '))
    b = int(input('Tell me the denominator: '))

    if b != 0:
        print(a / b)
    else:
        print('You can\'t catch me.')

    my_money = 500
    value = int(input('How much do you want to spend? '))
    if value >= 0:
        my_money -= value  # my_money = my_money - value
    else:
        print('The value must be non-negative.')
    # also -=, *=, **=, //=, /=, %=
    # no ++, --

    print(my_money)

num_months = int(input('Tell me how many months into the future we are: '))

current = num_months % 12
if current == 0:
    print('Meet me in September')
elif current == 1:
    print('Halloween Month (october)')
elif current == 2:
    print('Thanksgiving yes!')
elif current == 3:
    print('Christmas Time')
elif current == 4:
    print('New Years')
elif current == 5:
    print('Does anyone actually do Valentines?')
elif current == 6:
    print('Springtime in March')
elif current == 7:
    print('Tax time :(')
elif current == 8:
    print('End of School Year')
elif current == 9:
    print('June Summertime')
elif current == 10:
    print('July named after Julius Caesar')
elif current == 11:
    print('Prep for semester, sad times')
else:
    print('current is getting reset to something not mod 12')

x = 0
y = 15

if x and y > 5:
    print('yes you are right')

"""
    Arithmetic goes first [highest precedence]
        PEMDAS
    comparisons
        ==, <=, <, >, >=, !=, 
    then logic last [lowest precedence]
        not = happens before the others
        and/or = same precedence.  

    So what the heck does it mean to say if x:?
"""

if x:
    print('x is True, ???')
"""
integers/floats/numbers 
    0 = False
    anything else = True
For strings:
    '' = False
    anything else = True

"""

if '      ':
    print('Yep this is true')

if not '':
    print('The empty string is actually false')

if x != 7:
    print('7 is a lucky number but we don\'t want it')

"""
How many elif statements can you write in a single if block?
    as many as you want
    infinity <-- somewhat scary

How many elif statements will execute in a single if block?
    1 or 0
    at most 1
"""

"""
DeMorgan's Laws

not A and not B = not(A or B)
not A or not B = not(A and B)

Sometimes it's useful for dealing with complex expressions
"""

if x < 0 and y < 0 and z < 0:
    pass

if not (x >= 0 or y >= 0 or z >= 0):
    pass  # placeholder that basically is a no-op no-operation, do nothing
"""
What is pass?
    
if (blah) {}
"""

"""
Nesting:
    You can have multiple levels of if statements
"""

username = input('Enter the username: ')

if username == 'eric8' or username == 'jdixon' or username == 'abc123':
    password = input('Enter your secret password: ')
    if password == 'admin':
        print('You are logged in.')
    else:
        print('incorrect password')
else:
    print('You are not a valid user.')