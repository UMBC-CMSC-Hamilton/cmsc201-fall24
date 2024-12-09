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

composers = {"Beethoven": 9, "Chopin": 24, "Vivaldi": 4}

print(composers["Scarlatti"])  # KeyError, Error

print(composers.get("Scriabin", "Who?!"))  # Who?!

print(composers.get("Vivaldi", "Who?!"))  # 4

print(composers["Chopin"], composers["Beethoven"], composers["Vivaldi"])
# 24 9 4
composers['Scarlatti'] = 17
print(composers)

# {"Beethoven": 9, "Chopin": 24, "Vivaldi": 4, 'Scarlatti': 17}

"""
64 into binary and hex
    bin     dec/hex     bin     dec hex
    0000    0           1000    8   8
    0001    1           1001    9   9
    0010    2           1010    10  a
    0011    3           1011    11  b
    0100    4           1100    12  c   
    0101    5           1101    13  d
    0110    6           1110    14  e
    0111    7           1111    15  f

    binary:
        64(even) => 32 (even) => 16 (even) => 8 (even)
        => 4(even) => 2 (even) => 1 (odd) 
        0100 0000
        
    hex:
        0x40 [remember that 0x symbol that means "hex will follow"]
        
    183
        183 (odd) => 91 (odd) => 45 (odd) => 22 (even) => 11 (odd) => 5 (odd) => 2 (even) => 1 (odd)
        1011 0111
        
        Hex: 0xb7
        
    1101 1011 to dec and hex
    
    1 + 2 + 8 + 16 + 64 + 128 = 192 + 3 + 8 + 16 = 219
    
    0xdb or 0xDB
    
    1010 0000
    
    To decimal 128 + 32 or a * 16 = 10 * 16 = 160
        128 + 32 = 160  (decimal)
        hex 0xa0
    
    Hex to binary FD30A15E use the table 
    1111 1101 0011 0000 1010 0001 0101 1110
"""

print("\\\\\nMerry\nChristmas!\\")
"""
    \\
    Merry
    Christmas!\
    
    [be aware of \t]
"""


def list_add(my_list):
    my_list.append('3')


if __name__ == '__main__':
    the_list = ['1', '7']
    list_add(the_list)
    list_add(the_list)
    print(the_list)

# ['1', '7', '3', '3']
# reason: lists are mutable, pass by reference, modified in the function.

a_list = ['Python', 'is', 'a', 'fun', 'time']

print(a_list[2:4])
print(a_list[4:10])
print(a_list[:3])


# ['a', 'fun']
# ['time']  because python will ignore indices 5-9
# ['Python', 'is', 'a']

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
    hello(15)  ---> "hello"
    hello(7)   ---> "hello"
    hello(10)  ---> "hello" (5x)
    hello(2)   ---> "hello"
    hello(5)   ---> "hello"
    hello(-3) 
"""

the_matrix = [[4, 2, 7], [8, 5, 6], [9, 1, 3]]
print(the_matrix[0][1])
print(the_matrix[2][1])
print(the_matrix[1][2])


# 2
# 1
# 6

def three_plus_one(x):
    return 3 * x + 1


if __name__ == '__main__':
    y = 1
    for i in range(4):
        y = three_plus_one(y)
    print(y)

"""
    y = 1
    y = 3(1) + 1 = 4 iteration i = 0
    y = 3(4) + 1 = 13 iteration i = 1
    y = 3(13) + 1 = 40 iteration i = 2
    y = 3(40) + 1 = 121 iteration i = 3
    
    answer:
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

# 101 => bab
"""
rec_fun(5) = 'b' + rec_fun(5//2) = 'b' + 'ab' = 'bab'
rec_fun(2) = 'a' + rec_fun(2//2) = 'a' + 'b' = 'ab'
rec_fun(1) = 'b' + rec_fun(1//2) = 'b' + '' = 'b'
rec_fun(0) = ''

Answer:
bab
"""

if __name__ == '__main__':
    a = [1, 2]
    b = list(a)  # true copy into new memory of this data
    b[0] += 3  # b  = [4, 2]
    print(a)

"""
[1, 2]


Other version of the question
"""

if __name__ == '__main__':
    a = [1, 2]
    b = a  # true copy into new memory of this data
    b[0] += 3  # b  = [4, 2]
    print(a)

# [4, 2] because the lists are set equal as references

""""
Debugging 1:

Line 6: if word_string to if not word_string: if len(word_string) > 0: [fine]
Line 9:
    if word_string[0].lower() in ['a', 'e', 'i', 'o', 'u']:
Line 12:
    return count_vowels(word_string[1:]) don't skip two letters
Line 16:
    missing colon
Line 17:
    result = count_vowels(my_words)
Line 18:
    print('The number of vowels is', result)
    print('The number of vowels is' + str(result))
    print(f'The number of vowels is {result}')
Line 19:
    my_words = input('Enter some words here') + 1 indent    
"""

"""
Debugging 2:
    Line 1: Missing Colon
    Line 6:
        total = 0
    Line 7:
        for i in range(len(the_list)):
    Line 8:
        if the_list[i] > 0:
    Line 9:
        total += the_list[i]
    
    Line 11:
        Missing Colon
    Line 12;
        ctn = 'Yes' or ctn = input("wanna go again?")
    Line 15: extra )
    Line 16:
        the_list = []
    Line 17:
            while temp_val != 'quit':
    Line 19:
        +1 indent
    

"""


def count_binary_ones(num):
    if num == 0:
        return 0
    if num % 2 == 0:
        return count_binary_ones(num // 2)
    else:
        return 1 + count_binary_ones(num // 2)


def min_of_max(twod):
    if not twod: # not 100% necessary because i tell you the list is not empty
        return 0
    max_list = []
    for i in range(len(twod)):
        current_max = twod[i][0]
        for j in range(len(twod[i])):
            if twod[i][j] > current_max:
                current_max = twod[i][j]
        max_list.append(current_max)

    current_min = max_list[0]
    for x in max_list:
        if x < current_min:
            current_min = x
    return current_min
