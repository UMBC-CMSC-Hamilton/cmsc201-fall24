"""
    Nesting - if you have multiple levels of if statements
        in python you tab in one level inside of another.

    Star Wars = you know the characters vaguely

"""
if False:
    light_dark = input('Are you on the light side or dark side? ')
    if light_dark.lower() == 'light':
        moisture_farmer = input('Are you a moisture farmer? ')
        if moisture_farmer.lower() == 'yes':
            print('You are Luke')
        else:
            carpet = input('Are you a large walking carpet? ')
            if carpet.lower() == 'yes':
                print('You are Chewbacca')
            else:
                bounty = input('Are you being hunted by bounty hunters? ')
                if bounty == 'yes':
                    print('You are Han Solo')
                else:
                    print('You are Pricess Leia')
    else:
        lightning_fingers = input('Do you shoot lightning and scream about unlimited power? ')
        if lightning_fingers == 'yes':
            print('You are Emperor Palpatine')
        else:
            print('You are Darth Vader')

"""
    Can you nest loops? yes
    Can you nest if statements into loops? yes
    can you nest loops into if statements? yes
"""

"""
For loops and lists

More fundamental loop (while loop is the other one) 90-95% of all loops are for loops

1st way that we have to repeat code over and over

For loops can iterate over lists, strings, ranges

Starting with ranges
"""

for i in range(10):
    print(i)

the_limit = int(input('Tell me a number to add up to: '))
# Goal: add 1 + 2 + 3 + 4 + ... + 25
total = 0
for i in range(the_limit + 1):
    total += i

print(total)

"""
range(start, stop) = start (inc) up to stop (exc), by default start = 0
"""
new_total = 0
for i in range(1, the_limit + 1):
    new_total += i

"""
What is factorial?

    n! = n * (n - 1)! n > 0
         1 if n == 0
    n! = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * ... 3 * 2 * 1
    
"""
fact_total = 1
for i in range(the_limit + 1):
    if i != 0:
        fact_total *= i

print(fact_total)

fact_total = 1
for i in range(1, the_limit + 1):
    fact_total *= i

print(fact_total)

# n!! = n * (n - 2) * (n - 4) ... (2 or 1)
# similar
# multiplying just the even numbers
# 2 * 4 * 6 * 8 * ... (n or n - 1)
double_fact = 1
for i in range(1, the_limit + 1):
    if i % 2 == 0:
        double_fact *= i

"""
range(start, stop, step)

step can be negative (go backwards)
    can also be not 1
"""
print()
for num in range(5, 12, 2):
    print(num)

print()
for num in range(0, 21, 7):
    print(num)

for countdown in range(10, -1, -1):
    print(f'T - {countdown}')

"""
neither will run because they have invalid ranges
"""
print('starting j loops')
for j in range(5, 25, -3):
    print(j)
for j in range(25, 5, 3):
    print(j)
print('ending j loops')


"""
Lists - 

student_0
student_1
student_2
student_3

"""

students = ['eric', 'robert', 'samantha', 'jill']

horrific = [2, 3.5, 'hello there', False, 5, 2, 'jill']
for x in horrific:
    print(x)

"""
for x in horrific:
    print(x + 2)
"""

mixed = ['hi', 3, 'byte', 4, 'turnip', 17, 'cat', 81, 'word', 3]

total_word = ''
total = 0
for i in range(len(mixed)):
    if i % 2 == 0:
        total_word += mixed[i]
    else:
        total += mixed[i]

print(total_word, total)

# how do indices work?
#          0  1  2  3  4  5  6
my_list = [3, 9, 1, 5, 7, 4, 3]

for i in range(len(my_list)):
    print(i, my_list[i])

my_list[4] = 13
print(my_list)

# print(my_list[281])