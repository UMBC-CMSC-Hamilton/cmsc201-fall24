"""
Write an expression that is True if and only if chance_rain is greater than 0.01 and umbrella
is True and rain coat is also True.
"""
# not part of the answer
chance_rain = 0.05
umbrella = True
rain_coat = False
# all you have to write
chance_rain > 0.01 and umbrella and rain_coat

"""
17. Write an expression that is True if and only if either x is 
greater than 20 or y is greater than 12 but not both.

a xor b = (a and not b) or (b and not a)
"""
x = 21
y = 13
# answer
(x > 20 and not (y > 12)) or (y > 12 and x <= 20)
(x > 20 and y <= 12) or (y > 12 and x <= 20)
# not writing if... just the expression inside of it
# if [boolean expression]:
(x > 20 or y > 12) and not (x > 20 and y > 12)

"""
What kind of loop can result in an infinite loop? Give an example consisting of 5 or less lines
of code demonstrating an infinite loop.

A while loop because the condition can always be true. 

x = 12
while x > 0:
    x += 1
    
while True:
    pass

x = 5
y = 2
while x > y:
    x += 1
    print(x, y)
"""

"""
Explain what happens when we replace an elif with an if statement instead. For instance
consider the code below:
"""
num = int(input(' >> '))
if num > 10:
    print(' num is larger than 10 ')
elif num > 20:
    print(' num is larger than 20 ')

"""
In the original statement, if you have a number like 25 then only num larger than 10 will print.

If you make the replacement, then if the number is bigger than 20, both will print.
"""
"""
20)
start stop step
start stop
stop

21) True
22) True
23) False
"""

doubles = 1
while doubles < 50:
    print(doubles)
    doubles *= 2

"""
1
2
4
8
16
32
"""

for i in range(5, 27, 3):
    print(i)
"""
5
8
11
14
17
20
23
26
"""

s = 'hello'
n = 15
if n == 20 and s == 'hello'
    print(" Both are true . ")
elif n == 15:
    print(" 15 is equal to 3 times 5 ")
elif s == 'hello'
    print(" Well Hello There ")
else:
    print(" Obi Wan Kenobi , You ’ re my only hope ")

"""
Line 7 - needs a colon
Line 8 - range(len(has_list))
Line 11 - if need_counts [ i ] <= has_counts [ j ]: needs to be >= 
Line 14 - print ( ’ ... ’ , needs[i]) 
Line 17 - for x in needs_counts : to for x in has_counts:
Line 18 - total += x
"""


def get_two_max_values(L):
    if not L:  # L == [] or len(L) == 0
        print(-1, -1)
        return [-1, -1]
    elif len(L) == 1:
        print(L[0], -1)
        return L[0], -1

    first_max = 0
    second_max = 0
    """
    what if you have first_max = 20
    second_max = 10
    x = 15 ?
    """

    for x in L:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x

    print(first_max, second_max)
    return [first_max, second_max]


"""
distance three match(’abca’, ’a’) should return True
distance three match(’adabdc’, ’a’) should return False
distance three match(’adabdc’, ’d’) should return True
"""


def distance_three_match(s, c):

    for i in range(len(s) - 3):
        if s[i] == s[i + 3] == c:
            return True

    return False

[1, 2,3, 4] in [[1, 2, 3, 4], 2, 3, 4, 5]