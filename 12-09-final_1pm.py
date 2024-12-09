"""
Final is 6-8 pm on Friday 13th.

    put out tentative room assignments today.  Hopefully more room its going to be tight.

    I extended the project until wednesday.

"""
"""
MCQ answers:

    1 c
    2 c
    3 b
    4 b
    5 d
    6 c
    7 c
    8 b
    9 a
    10 b
"""

try:
    composers = {"Beethoven": 9, "Chopin": 24, "Vivaldi": 4}

    print(composers["Scarlatti"])

    """
        KeyError = Error
    """

    print(composers.get("Scriabin", "Who?!"))

    """
        Who!?
    """

    print(composers.get("Vivaldi", "Who?!"))

    """
    4
    """

    print(composers["Chopin"], composers["Beethoven"], composers["Vivaldi"])

    """
    24 9 4
    """

    composers['Scarlatti'] = 17
    print(composers)

    new_dictionary = {"Beethoven": 9, "Chopin": 24, "Vivaldi": 4, 'Scarlatti': 17}

except KeyError:
    print('nope')
"""
dec bin     hex     
0   0000    0       4   0100    4   8   1000    8       12  1100    c 
1   0001    1       5   0101    5   9   1001    9       13  1101    d
2   0010    2       6   0110    6   10  1010    a       14  1110    e
3   0011    3       7   0111    7   11  1011    b       15  1111    f

64
Binary:
    64 (even) => 32 (even) => 16 (even) => 8 (even) => 4(even) => 2(even) => 1 (odd) => 0 (done)
    
    0100 0000
Hex:
    0x40
    
183 => Binary
    183 (odd) => 91 (odd) => 45 (odd) => 22 (even) => 11 (odd) => 5 (odd) => 2 (even) => 1 (odd)

    1011 0111
    
        0b10110111
    128 + 32 + 16 + 7 = 176 + 7 = 183 yes
    
    Hex:
        0xb7
        b(16) + 7
        11(16) = 176 + 7 = 183
        
        0xa32 = 10 * 256 + 3 * 16 + 2

1101 1011 
hex and to decimal
hex: 0xdb

128 + 64 + 16 + 8 + 2  + 1 = 219

1010 0000
hex
    0xa0
decimal
    128 + 32 = 160
    
    0xFD30A15E into binary
    [please do not calculate, i dont even know exactly what you would calculate but please dont]
    1111 1101 0011 0000 1010 0001 0101 1110
"""

print("\\\\\nMerry\nChristmas!\\")
"""
24) 
\\
Merry
Christmas!\

[remember \t is tab]
"""


def list_add(my_list):
    my_list.append('3')


if __name__ == '__main__':
    the_list = ['1', '7']
    list_add(the_list)
    list_add(the_list)
    print(the_list)

"""
25) Append will change the original list, so when you print it out

['1', '7', '3', '3']

Other version of this question involves an immutable thing, int or string


"""
a_list = ['Python', 'is', 'a', 'fun', 'time']

print(a_list[2:4])
print(a_list[4:10])
print(a_list[:3])
"""
['a', 'fun']
['time'] - python doesnt generate index errors on slices
['Python', 'is', 'a']
"""


def hello(count):
    if count < 0:
        return
    print("hello")
    if count % 5 == 0:
        hello(count - 8)
    else:
        hello(count + 3)


if __name__ == '__main__':
    hello(15)

"""
hello(15) ---> "hello"
hello(7) ---> "hello"
hello(10) ---> "hello"
hello(2) --> "hello"
hello(5) --> "hello"
hello(-3)
"""

the_matrix = [[4, 2, 7], [8, 5, 6], [9, 1, 3]]
print(the_matrix[0][1])
print(the_matrix[2][1])
print(the_matrix[1][2])

"""
    2
    1
    6
"""


def three_plus_one(x):
    return 3 * x + 1


if __name__ == '__main__':
    y = 1
    for i in range(4):
        y = three_plus_one(y)
    print(y)

"""
Work:
    y = 1
    y = 3(1) + 1 = 4 iteration i = 0
    y = 3(4) + 1 = 13 iteration i = 1
    y = 3(13) + 1 = 40 iteration i = 2
    y = 3(40) + 1 = 121 iteration i = 3
Prints:
121
"""


def rec_fun(a):
    if a == 0:
        return ''
    if a % 2 == 0:
        return 'a' + rec_fun(a // 2)
    else:
        return 'b' + rec_fun(a // 2)


if __name__ == '__main__':
    print(rec_fun(5))

"""
    rec_fun(5) -> 'b' + returned = 'b' + 'ab' = 'bab'
    rec_fun(2) -> 'a' + returned = 'a' + 'b' = 'ab
    rec_fun(1) -> 'b' + returned = 'b'
    rec_fun(0) = ''
    
    101b = 5
"""

if __name__ == '__main__':
    a = [1, 2]
    b = list(a) # what does this do? it makes a copy, not the original list
    b[0] += 3 # b = [4, 2]
    print(a)  #not asking to print out b, i want a

"""
[1, 2]

other version of the question would be if i replace b = list(a) with b = a
then we get [4, 2]
"""

"""
Debugging:
Line 6: add a not to the expression

Line 9:
    if word_string.lower() == ['a', 'e', 'i', 'o', 'u']:
    word_string[0] only want the first character
    == needs to be in
    
Line 12:
    return count_vowels(word_string[2:])
    return count_vowels(word_string[1:]) fix the index
    
Line 16:
    missing colon
Line 17:
    count_vowels(my_words)
Line 18:
    print('The number of vowels is' + str(result))
    print('The number of vowels is', result)
    print(f'The number of vowels is {result}')
Line 19:
    infinite loop
    my_words = input('Enter some words here')  needs to be here too


Debugging 2:
Line 1: 
    def sum_positives(the_list): [needs colon]
Line 6:
    total = 0
Line 7:
    for i in range(len(the_list)):
Line 8:
    if the_list[i] > 0: [or >=]
Line 11:
    if __name__ == '__main__': [yet another colon]
Line 12:
    ctn = 'Yes' Undefined variable
Line 16:
    the_list = []
Line 17:
    while temp_val != quit:
Line 19: 
    indent one more place, or else infinite loop
"""

def rec_fun(a):
   if a == 0:
       return ''
   if a % 2 == 0:
       return 'a' + rec_fun(a // 2)
   else:
       return 'b' + rec_fun(a // 2)


def count_binary_ones(a_number):
    if a_number == 0:
        return 0

    if a_number % 2 == 0:
        return count_binary_ones(a_number // 2)
    else:
        return 1 + count_binary_ones(a_number // 2)



def min_of_max(twod):
    list_of_maxes = []
    for sublist in twod:
        current_max = sublist[0]  # if you know that the list isnt empty
        for x in sublist:
            if x > current_max:
                current_max = x
        list_of_maxes.append(current_max)

    the_min = list_of_maxes[0]
    for x in list_of_maxes:
        if x < the_min:
            the_min = x
    return the_min


