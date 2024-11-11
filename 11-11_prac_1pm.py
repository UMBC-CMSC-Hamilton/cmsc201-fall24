"""
1) C
2) C => int string float and bool are immutable, the rest is mutable [mostly]
3) B => mutable things are passed by reference, immutable things are passed by value [copied]
4) A
5) C => KeyError remember that .get(x, 0) it'll return None by default if you don't put in a parameter
6) B
7) C lines 8, 9
8) B => to stop a recursion you need a base case
9) A

Recursive case vs base case
mutable vs immutable
pass by value vs pass by reference
file modes

10) 9 (6 + 3)
11) KeyError
12)
{ ’ falafel ’: 3 , ’ quiche ’: 6 , ’ babka ’: 6, ’ danish ’: 5}
13) 8 [length once you add two elements]

14) Write an expression that evaluates to True if and only if all three of the diagonal elements in
a 2d-list of dimension 3x3 called grid are the character “X”. A diagonal element is one where
the row and column index match.
"""
grid = [['x', 'o', 'x'], ['x', 'o', 'x'], ['x', 'o', 'x']]

grid[0][0] == grid[1][1] == grid[2][2] == 'X'
grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X'

"""
15. Write an expression that evaluates to True if and only if a dictionary named robots has a
key ‘Data’ and a key ‘HAL’ but not the key ‘Marvin’
"""
robots = {}
# answer
'Data' in robots and 'HAL' in robots and 'Marvin' not in robots

"""
16. Describe what happens when you have a recursive function with no base case, both in theory
and specifically in Python.

In theory, a recursive function with no base case will recurse forever, like an infinite loop.
    Also in theory, a little deeper eventually the computer will run out of memory and the program
    will crash.  
In python, a RecursionError is thrown after 1000 recursion depth.  

17. Explain what checks must be performed to ensure that accessing the 2d-list grid at 
grid[row][col] does not result in an IndexError.

You check these things:
    1) 0 <= row < len(grid)
    2) 0 <= col < len(grid[row])

Anatomy of the function:
    Name, prototype
    parameters, arguments
    function declaration
    function call
    function body
    
    Starting from top left going around clockwise
"""


def inner(x, y):
    return 4 * y - x


def outer(a, b):
    return 2 * b + a


a = 4
b = 3
c = inner(a, b)
d = outer(inner(a, c), b)
print(a, b, c, d)

"""
18 real one) 
    work:
    c = inner(4, 3) = 4 * 3 - 4 = 8
    4 * 8 - 4 = 28
    d = outer(inner(4, 8), 3) = outer(28, 3)
    d = 2 * 3 + 28 = 34
    done
    
    output, box this:
    4 3 8 34
"""


def diabolical(n, k):
    print(n, k)
    if n < 1:
        return 1
    return 1 + diabolical(n - k, k + 1)


print(diabolical(25, 0))

"""
25 0                                            9
25 1                d(25 - 0, 0 + 1) = d(25, 1) 8
24 2                d(25 - 1, 1 + 1) = d(24, 2) 7
22 3                d(24 - 2, 2 + 1) = d(22, 3) 6
19 4                d(22 - 3, 3 + 1) = d(19, 4)  5
15 5                d(19 - 4, 4 + 1) = d(15, 5) 1 + 3 = 4
10 6                d(15 - 5, 5 + 1) = d(10, 6) 1  + 2 = 3
4 7                d(10 - 6, 6 + 1) = d(4, 7)   1 + 1 = 2
-3 8                d(4 - 7, 7 + 1) = d(-3, 8)  1
9
"""

print('hellojelloyellow'.split('ll'))
# be careful if the thing you're splitting is the first element
print('abbcbcabcaabcbbccb'.split('a'))

matrix = [[5, 4, 3], [7, 8, 9], [2, 1, 0]]
for i in range(3):
    print(matrix[(2 * i + 1) % 3][(5 * i + 2) % 3])
"""
matrix[1][2] = 9
matrix[0][1] = 4
matrix[2][0] = 2
Answers:
9
4
2
"""

"""
128 64 32 16 8421 
 0  0  1  1  0111 to decimal
 32 + 16 + 4 + 2 + 1 = 55
 
 1010 0011
 1 + 2 + 32 + 128 = 163
 
 53 into binary
 odd (1) => 26 (even) => 13 (odd) => 6 (even) => 3 (odd) => 1 (odd)
 0011 0101
  check = 32 + 16 + 4 + 1 = 53
  
220 to binary
220 (even) => 110 (even) => 55 (odd) => 27 (odd) => 13 (odd) => 6 => 3 (odd) => 1(odd)

1101 1100

12 for row in range( len ( lines ) ):
14 if row in lines_to_switch: <- colon
16 if c in switches [ row ]: ???
    if c in switches
19 new_line = c => new_line += c
20 new_lines.append ( new_line )
22 new_lines . append ( lines[row] <-- )
"""

"""
Write a recursive function sum ascending that calculates the sum of a list but only those
elements which are ascending, for instance the list:
L = [1, 2, 1, 4, 2, 3, 5, 8, 7]
should produce 1 + 2 + 4 + 5 + 8 = 20. Do not use any loops. You are permitted to use
list slices, recall that L[1 :] will make a copy of everything except for the first element. I leave
the parameters up to you, there are multiple ways to solve the problem.
def sum_ascending ( ):
"""


def sum_ascending(the_list, current):
    if not the_list:
        return 0
    if the_list[0] > current:
        return the_list[0] + sum_ascending(the_list[1:], the_list[0])
    else:
        return sum_ascending(the_list[1:], current)


"""
Write a function called max of lists where you take a 2d list and generate a list of the max-
imums of each list. Assume the lists will have only positive integers, so if the list is empty,
then zero is the maximum.
For example if you have the list L = [[1, 2, 3, 4], [10, 50, 100, 1000, 2], [], [3]] then the list that
should be returned is [4, 1000, 0, 3].
def max_of_lists ( L )

Hint: always consider empty lists first
"""


def max_of_lists(L):
    m = []
    for i in range(len(L)):
        the_max = 0
        for j in range(len(L[i])):
            if L[i][j] > the_max:
                the_max = L[i][j]
        m.append(the_max)
    return m
