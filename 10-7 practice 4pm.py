print([1, 2, 3, 4] in [[[1, 2, 3, 4], 5], 6, 7, 8])
print([1, 2, 3, 4] in [1, 2, 3, 4, 5])

print(6 / 2)

my_list = [1, 2, 3, 4, 5, 5, 6]
my_list[6 // 2]

"""
Write an expression that is True if and only if chance_rain is greater than 0.01 and umbrella
is True and rain coat is also True.
"""
# this is not the answer
chance_rain = 0.05
umbrella = False
rain_coat = True

# this is the answer
chance_rain > 0.01 and umbrella and rain_coat
chance_rain > 0.01 and umbrella == True and rain_coat == True

"""
    What is a boolean expression?
        if [boolean expression]:
        dont need to write the if part, or the colon
"""

"""
Write an expression that is True if and only if 
either x is greater than 20 or y is greater than 12 but not both.

a xor b = (a and not b) or (b and not a)
"""
x = 1
y = 20

# this is the actual answer
(x > 20 and y <= 12) or (y > 12 and x <= 20)
(x > 20 or y > 12) and not (y > 12 and x > 20)

# python weirdness
print(5 and 3)

"""
What kind of loop can result in an infinite loop? Give an example consisting of 5 or less lines
of code demonstrating an infinite loop.

While loops, they can have a condition that is never false, so will go forever.
"""


def inf_while():
    x = 5
    while x > 0:
        x += 1

    while True: pass


"""
Explain what happens when we replace an elif with an if statement instead. For instance
consider the code below:

If the number is larger than 20, then the original statement will only ever say 
"num is larger than 10", conversely if both are if statements, then if the number is 
greater than 20, both things will print.  
"""
num = int(input(' >> '))
if num > 10:
    print('num is larger than 10')
elif num > 20:
    print('num is larger than 20')

"""
21) True
22) True
23) False
"""

doubles = 1
while doubles < 50:
    print(doubles)  # think about what happens when print and *= are reversed
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

"""
Line 7 : add a colon to the end
Line 8 : ... range(len(has_list)):
Line 11: if need_counts [ i ] > has_counts [ j ]: You can say replace <= with >. 
Line 14: replace i with needs[i]
Line 17: for x in has_counts
Line 18: replace = with +=
"""


def get_two_max_values(L):
    if not L:
        print(-1, -1)
        return [-1, -1]
    elif len(L) == 1:
        print(L[0], -1)
        return [L[0], -1]

    first_max = 0  # fm = 0
    second_max = 0  # sm = 0

    for x in L:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x

    print(first_max, second_max)
    return [first_max, second_max]


def distance_three_match(s, c):

    for i in range(len(s) - 3):
        if s[i] == s[i + 3] == c:
            return True

    return False
