"""
Exams "should be back" release the grades as soon as possible

Recursion
    Idea that a function calls itself.

    Russian Nesting Dolls

    In programming recursion is the process where a function calls itself.

    Why do we need it?
        Some problems need us to try to go down multiple paths.
        Path finding algorithms like depth first / breadth first search
        Branching is the real issue that needs recursion
"""


def infinite(x):
    print(x)
    infinite(x - 1)


def infinite_while():
    x = 100
    while True:
        print(x)
        x -= 1


# infinite(100)
"""
Python by default will give a RecursionError at a depth of 1000 recursions
995, 1002, 1005 
"""


def countdown(n):
    if n == 0:  # this is called a base case
        print('Blastoff!! ')
        return  # this return statement happens and then the function exits, no recursive calls
    # every recursive algorithm needs a base case

    print(f'T - {n}')
    countdown(n - 1)
    n += 1


countdown(10)

"""
    Factorial
        
        n! = n * (n - 1)!
        factorial(n) = n * factorial(n - 1)
        Need a base case:
            0! = 1
"""


def factorial(n):
    print(f'Calling factorial({n})')
    if n <= 0:
        return 1
    temp = n * factorial(n - 1)
    print(f'Leaving factorial({n}) = {temp}')
    return temp


def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


x = int(input('>> factorial >> '))
while x != -1:
    print(factorial(x))
    x = int(input('>> factorial >> '))

"""
Fibonacci sequence:

    fib(n) = fib(n - 1) + fib(n - 2)
    fib(0) = fib(1) = 1
"""


def fib(n):
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_visual(n, level=0):
    print('\t' * level + f'Calling fib({n})')

    if n <= 1:
        return 1

    return fib_visual(n - 1, level + 1) + fib_visual(n - 2, level + 1)


x = int(input('>> fibonacci >> '))
while x != -1:
    print(fib_visual(x))
    x = int(input('>> fibonacci >> '))


"""
A's and B's

make all possible permutations of a's and b's of a certain length

length = 0
    [nothing is here]
length = 1
    a   b
length = 2
    aa  ab  ba  bb
length = 3
    aaa  aab  aba  abb
    baa  bab  bba  bbb
length = 4
    aaaa  aaab  aaba  aabb
    abaa  abab  abba  abbb
    baaa  baab  baba  babb
    bbaa  bbab  bbba  bbbb


Thinking process:
    Take the answer on length L - 1
    copy it
    add an ''a' to the start of the first copy
    add a 'b' to the start of the second copy
    go until L = 0 (base case)
"""


def as_and_bs(length, current=''):
    if length == 0:
        print(current)
    else:
        as_and_bs(length - 1, current + 'a')
        as_and_bs(length - 1, current + 'b')


def as_and_bs_visual(length, current='', level=0):
    print('\t' * level + current)
    if length == 0:
        pass
    else:
        as_and_bs_visual(length - 1, current + 'a', level + 1)
        as_and_bs_visual(length - 1, current + 'b', level + 1)


x = int(input('>> abperm >> '))
while x != -1:
    as_and_bs_visual(x)
    x = int(input('>> abperm >> '))



def as_and_bs_and_cs(length, current=''):
    if length == 0:
        print(current)
    else:
        as_and_bs_and_cs(length - 1, current + 'a')
        as_and_bs_and_cs(length - 1, current + 'b')
        as_and_bs_and_cs(length - 1, current + 'c')


x = int(input('>> abc >> '))
while x != -1:
    as_and_bs_and_cs(x)
    x = int(input('>> abc >> '))

