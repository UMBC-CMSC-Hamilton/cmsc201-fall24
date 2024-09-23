"""
    Nesting - What is nesting?
        we have if statements / elif / else
        can you put an if statement inside of an if statement?
            yes

    input a number
        if the number is even
            is it also divisible by 4?
        if the number is odd
            is it divisible by 3?
"""
if False:
    x = int(input('Enter a number: '))

    if x % 2 == 0:
        if x % 4 == 0:
            print('x is actually divisible by 4')
        else:
            print('It is even but not divisible by 4')
    else:
        if x % 3 == 0:
            print('x is divisible by 3')
        else:
            print('who knows...')


    """
    
    """
    human = input('Are you human? ')
    if human == 'yes' or human == 'y':
        fight_gorn = input('Did you fight the Gorn? ')
        if fight_gorn == 'yes' or fight_gorn == 'y':
            print('You are James T. Kirk')
        else:
            doctor = input('Are you a doctor but not a bricklayer? ')
            if doctor == 'y' or doctor == 'yes':
                print('You are Bones.')
            else:
                can_you = input('Can you do it? ')
                if can_you == 'no' or can_you == 'n':
                    print('You are Scotty.')
                else:
                    fence_or_borsch = input('Would you rather fence? Or talk about Borsch? ')
                    if fence_or_borsch == 'fence':
                        print('You are Sulu')
                    elif fence_or_borsch == 'borsch':
                        print('You are Checkov')
                    else:
                        print('You are KHAAAANNNNNNN!!!!!')
    else:
        is_it_logical = input('How do you feel about logic? (great/not great)')
        if is_it_logical.lower() == 'great':
            print('You are Spock.')
        else:
            print('You are Uhura')

    """
    Let's talk about my favorite concept of the semester: for loops
    
    notice here that until now we haven't really had a way to repeat code. 
    
    Looping is a fundamental part of the ability to make a computer. 
    
    How do you actually write such a thing?
    
    for loops can scan through lists, strings, and range objects (sorta lists not really)
    
    What is a range object?
    range(n)
        start at zero, go up to but not including n.
    
    """

    for i in range(10):
        print(i)

limit = int(input('What number do you want to add to? '))
# goal: 1 + 2 + 3 + 4 + ... + n.
total = 0
for i in range(limit + 1):
    total = total + i  # total += i

print(total)

"""
    let's compute factorial
    
    n! = 1 if n == 0
         n * (n - 1)! if n > 0

    n! = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * ... * 3 * 2 * 1
            <------------------------------------------------------
"""
fact_limit = int(input('What factorial do we want to compute? '))
fact = 1  # easy mistake to set it to zero
for num in range(fact_limit + 1):
    if num != 0:
        fact *= num

print(f'The result is {fact}')
# (20 + 4) * 5 = 100 + 20
# (25 - 1) * 5 = 125 - 5

"""
I dont want to have to check, can't we just not have 0 happen?
    Yes
range(start, end) = starts at start goes up to end (not included), by 1s
"""

fact2 = 1
for num in range(1, fact_limit + 1):
    fact2 *= num
print(f'The number {fact2} should be the same')


for x in range(5, 12):
    print(x)

# note that python wont run a loop where the range is invalid
# when you use range, it checks for you.
print('Starting y loop')
for y in range(123, 5):
    print(y)

# for y in range(start_val, end_val)

print('Ending y loop')

# for(int y = 123; y != 5; y++)

"""
    What if you want to go backwards?
        there's yet another secret argument inside of range, step argument
    range(stop)
    range(start, stop)
    range(start = 0, stop, step = 1)
"""

for i in range(2, 200, 4):
    print(i, end=' ')

print() # if you put a print without anything in it, end= '\n' hit return

for i in range(10, -1, -1):
    print(i, end=' ')

print()

for j in range(3, 178, 19):
    print(j, end=' ')

print()

for j in range(100, 0, -7):
    print(j, end=' ')

print()

"""
    What are lists?
    
"""

list_of_nums = [2, 5, 9, 3, 1, 8, 7, 6, 5, 5]
total = 0
for num in list_of_nums:
    total += num
    print(num, total)

#                   0       1            2         3      4       5            6
list_of_strings = ['hi', 'sandwich', 'borsch', 'spock', 'data', 'rhyme', 'grapenuts']

for word in list_of_strings:
    print(word)

# It's an IndexError
# print(list_of_strings[25])

for i in range(len(list_of_strings)):
    print(i, list_of_strings[i])
