"""
    Drawing with for loops?
        Draw an X?
            what does an X look like?
        0 1 2 3 4 5 6 7
    0    A 0 0 0 0 0 0 A regular diagonal case
    1    0 A 0 0 0 0 A 0
    2    0 0 A 0 0 A 0 0
    3    0 0 0 A A 0 0 0
    4    0 0 0 A A 0 0 0
    5    0 0 A 0 0 A 0 0
    6    0 A 0 0 0 0 A 0
    7    A 0 0 0 0 0 0 A

    On diagonal, the indices are the same, x == y then we draw the symbol
    what about 7 - x for the anti-diagonal? that works

    Want their x to be of size 8: need to consider size - 1 - x
"""

size = int(input('How big of an X do you want to draw? '))

for x in range(size):  # each row
    for y in range(size):  # each column within each row
        if x == y or y == size - 1 - x:
            print('*', end=' ')
        else:
            print(' ', end=" ")
    print()

"""
    Checkerboard "shape"
     0123456789
  0  # # # # # # # 
  1   # # # # # # 
  2  # # # # # # # 
  3   # # # # # # 
  4  # # # # # # # 
  5   # # # # # # 
  6  # # # # # # # 
  7   # # # # # # 
    evens & odds 
    evens => draw odds=> blank
"""

shape = input('Tell me a character: ')

for y in range(size):
    for x in range(size):
        if (x + y) % 2 == 0:
            print(shape, end=' ')
        else:
            print(' ', end=' ')
    print('\n', end='')

"""
Let's make a circle

    x^2 + y^2 = r^2
"""

error = 0.5

for y in range(-size, size + 1):
    for x in range(-size, size + 1):
        if size - error <= (x ** 2 + y ** 2) ** (1 / 2) <= size + error:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""
    While loops
        for loops are good, they allow us to cycle through strings, lists, ranges of various kinds
        but the one limitation of a for loop is that the for loop is restricted to operating
        as many times as the list is long, or string's length, or the size of the range.
        
        You can't loop indefinitely with a for loop.  
            user menu - you don't know how many options they will check
            server program - you don't know how many requests and you dont know how long 
                the server will be up
            gui programs - gets user messages, parses them responds
        want a while loop
        
        while loop is an if statement with repeat turned on 
"""

menu_options = """1) start
2) stop
3) save
4) whatever
5) quit
Select One >> """

option = int(input(menu_options))
while option != 5:
    # do all the things inside of this area here
    print('we are going to do ', option)
    # last line of the while loop
    option = int(input(menu_options))

"""
    input validation loops
    
    
"""
a_positive = int(input('Enter a positive integer: '))
while a_positive <= 0:
    a_positive = int(input('I don\'t think that was positive, try again. Enter a positive integer: '))

string_with_z = input('Enter a string starting with z: ')
while string_with_z[0].lower() != 'z':
    string_with_z = input('Enter a string starting with z: ')

i = 0  # start
while i < 10:  # stop
    print(i, end=" * ")
    i += 1  # step
# for i in range(10): print(i)
print()

"""
    All for loops can be rewritten as while loops
        "more general loop"
"""

my_list = [5, 3, 4, 5, 6, 5, 4, 6, 6, 4, 5, 6, 4, 3, 6, 7, 4, 6, 9]
index = 0
while index < len(my_list):
    # imagine instead of a print statement 20 or so lines
    print(my_list[index], end=" ")
    index += 1

print()

"""
    while loops can be infinite because you made the condition:
        while True:
            stuff
        
        while i < 10
            not remember i += 1
            
    infinite loops are generally not what you want
"""

"""
    On the opposite side, if the condition is false, the loop never runs the first time
    
    "skipped loop"
"""
num = int(input('Enter a number between 1 and 10: '))
while not(1 <= num <= 10):  # num < 1 or num > 10
    num = int(input('Enter a number between 1 and 10: '))



num = int(input('Enter a number (fibonacci): '))
"""
What are the fibonacci numbers? 
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
"""

prev_fib = 1
current_fib = 1
while current_fib < num:
    temp = current_fib
    current_fib += prev_fib
    prev_fib = temp
    print(current_fib)


new_list = []
thing = input('What do you want to add? ')
while thing != 'quit':
    new_list.append(thing)
    thing = input('What do you want to add? ')

my_string = 'abcd1234'
index = 4
print(my_string[index])