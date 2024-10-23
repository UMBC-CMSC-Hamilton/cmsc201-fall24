"""
Exams will come back in discussion
    come see me in my office - i'll have them if you didn't get them

Today's topic is recursion

Recusion is a process which calls itself

    russian nesting dolls

    in programming recursion is when a function calls itself

        ensure that what happens is not an infinite process

        around 1000 recursions python throws a RecursionError
        if it didn't then eventually the program would actually crash anyway

    You get a stack overflow [the website is named after this]
"""


def infinite_rec(x):
    print(x)
    infinite_rec(x - 1)


"""
    countdown(10) [bottom of the stack]
        countdown(9)
            countdown(8)
                countdown(7)
                    countdown(6)
                        countdown(5)
                            countdown(4)
                                countdown(3)
                                    countdown(2)
                                        countdown(1)
                                            countdown(0) -> prints and returns
                                            top of the stack
"""


def countdown(x):
    if x == 0:
        print('Blastoff!')  # you need some branch of logic that is not recursive
        # we call this the base case
        # the reason we need this is to stop the recursion eventually
    else:
        # this is a recursive case it calls itself
        print(x)
        countdown(x - 1)


"""
    Factorial first
        n! = n * (n - 1)! ==> recursive case
        factorial(n) = n * factorial(n - 1)
        
        0! = 1 ==> base case
"""

"""
    factorial(5) = 5 * factorial(4) = 5 * 24 = 120
    factorial(4) = 4 * factorial(3) = 4 * 6 = 24
    factorial(3) = 3 * factorial(2) = 3 * 2 = 6
    factorial(2) = 2 * factorial(1) = 2 * 1 = 2
    factorial(1) = 1 * factorial(0) = 1 * 1 = 1
    factorial(0) = 1
"""


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def iterative_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


x = int(input('>> factorial>> '))
while x != -1:
    print(factorial(x))
    x = int(input('>> factorial>> '))

"""
A branching recursion makes more than one recursive call per instance, can end up making
    quite a lot of recursive calls.
    
Fibonacci

Fib(n) = Fib(n - 1) + Fib(n - 2)
Two base cases: Fib(0) = Fib(1) = 1
"""


def fib(n, level=0):
    print('\t' * level + f'Called fib({n})')

    if 0 <= n <= 1:
        return 1

    return fib(n - 1, level + 1) + fib(n - 2, level + 1)


x = int(input('>> fib >> '))
while x != -1:
    print(fib(x))
    x = int(input('>> fib >> '))

"""
    Want to do: Output every possible combination of a's and b's
    
        length = 3
        
        aaa
        aab
        aba
        abb
        baa
        bab
        bba
        bbb
        
        length 4, maybe 16?
        aaaa
        aaab
        aaba
        aabb
        abaa
        abab
        abba
        abbb
        
        baaa
        baab
        baba
        babb
        bbaa
        bbab
        bbba
        bbbb

    Need a recursion that adds and 'a' + as_and_bs(length -1)
    Another recursion that adds    'b' + as_and_bs(length - 1)
    
    You have to trust.
"""


def as_and_bs(length, current='', level=0):
    if length == 0:
        print('\t' * level + current)
        return
    else:
        print('\t' * level + current)

    as_and_bs(length - 1, current + 'a', level + 1)
    as_and_bs(length - 1, current + 'b', level + 1)


as_and_bs(2)
print('\n\n')
as_and_bs(3)

print('\n\n')
as_and_bs(4)

print('\n\n')
as_and_bs(5)

print('\n\n')
# as_and_bs(12)


"""
What other kinds of recursions can we do?
    what if you want the combinations of a, b, c, not just a and b?
"""

def as_and_bs_and_cs(length, current='', level=0):
    if length == 0:
        print('\t' * level + current)
        return
    else:
        print('\t' * level + current)

    as_and_bs_and_cs(length - 1, current + 'a', level + 1)
    as_and_bs_and_cs(length - 1, current + 'b', level + 1)
    as_and_bs_and_cs(length - 1, current + 'c', level + 1)


as_and_bs_and_cs(5)

"""
go back to just a's and b's but now i want only the same number of a's and b's

8
    abababab ok
    abbbbbbb not
    aaaabbbb ok
    aabbbbba not ok
"""

# delta = numas - numbs

def as_and_bs_exact(length, delta, current='', level=0):
    if length == 0:
        if delta == 0:
            print('\t' * level + current)
        return
    else:
        print('\t' * level + current)

    as_and_bs_exact(length - 1, delta + 1, current + 'a', level + 1)
    as_and_bs_exact(length - 1, delta - 1, current + 'b', level + 1)

x = int(input('>> ab exact >> '))
while x != -1:
    print(as_and_bs_exact(x, 0))
    x = int(input('>> ab exact >> '))