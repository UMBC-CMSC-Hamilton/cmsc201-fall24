"""
    For loops and While Loops

    Draw a square

    Draw an X on the screen
        two for loops
        one for the rows (y)
        one for the columns (x)
     01234
  0  x   x
  1   x x
  2    x
  3   x x
  4  x   x
  for the diagonal we're looking for where y = x
  size = 5
  size - 1 - y = x
"""

size = int(input('What is the size of the X? '))

for y in range(size):
    for x in range(size):
        if x == y or y == size - 1 - x:
            print('*', end=' ')  # prevents the newline
        else:
            print(' ', end=" ")
    print()  # hits newline after every row

"""
    Draw a checkerboard
     0123456789    
   0 * * * * * * * * *
   1  * * * * * * * * 
   2 * * * * * * * * *
   3  * * * * * * * * 
   4 * * * * * * * * *
   5  * * * * * * * * 
   6 * * * * * * * * *
   7  * * * * * * * * 
   8 * * * * * * * * *
   9  * * * * * * * * 
"""

for y in range(size):
    for x in range(size):
        if (x + y) % 2 == 0:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()

"""
    Draw a "circle"
    
    x^2 + y^2 = r^2
"""

error = 0.33
for y in range(-size, size + 1):
    for x in range(-1 * size, size + 1):
        if size - error <= (x ** 2 + y ** 2) ** (1 / 2) <= size + error:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
    while loops
    
        with a for loop you "know" the number of times that the loop will run
            range(1, 10, 2) -> 1, 3, 5, 7, 9 run 5 times
            range(len(some_list)) -> # of times it runs is the length of that list
            range(len('my string')) -> also you know the length of the string so that's the number of times
        while loop you dont know the number of times it's going to run
            input validation from the user... 
            tic tac toe, chess, or whatever game... you dont know how many turns it will take
"""

a_positive = int(input('Enter a positive number: '))
while a_positive <= 0:
    a_positive = int(input('Enter a positive number: '))

print(a_positive ** (1 / 2))

q_string = input('Enter a string that starts with the letter q')
while q_string[0].lower() != 'q':
    q_string = input('Enter a string that starts with the letter q')

"""
All for loops can be recoded into while loops
but not all while loops can be made into for loops
for i in range(10):
"""
i = 0
while i < 10:
    print(i, end=" * ")
    i += 1
print()

my_list = ['a', 'b', 'z', 'r', 'q', 't', 'v', 'l', 'p', 'z', 'a']
index = 0
while index < len(my_list):
    print(my_list[index], end=" :: ")
    index += 1

print()

"""
Fibonacci numbers

loop until the number you enter is less than the fibonacci number we calculate

1, 1 starting ones
fib(n) = fib(n - 1) + fib(n - 2)
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
"""

exceed_me = int(input('What number do you want to exceed with Fibonacci numbers: '))
prev = 1
prev_prev = 1
current = 0
while current < exceed_me:
    current = prev + prev_prev
    prev_prev = prev
    prev = current
    print(current)

print(f'The number that exceeds {exceed_me} is {current}')


fibs = [1, 1]
while fibs[-1] < exceed_me:
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)
print(f'The number that exceeds {exceed_me} is {fibs[-1]}')


"""
Want the user to enter a list of things:
"""

"""
avoid: 
new_list = []
thing = ''
while thing != 'quit':
    thing = input('Tell me a thing: ')
    new_list.append(thing)

priming the pump
"""

new_list = []
thing = input('Tell me a thing: ')
while thing != 'quit':
    new_list.append(thing)
    thing = input('Tell me a thing: ')

print(new_list)
