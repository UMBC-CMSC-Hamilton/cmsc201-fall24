"""
Binary Hexadecimal

Decimal first:
    write numbers in base 10

    52 = 5 * 10 + 2
    7921 = 7 * 1000 + 9 * 100 + 2 * 10 + 1
    328 = 3 * 10^2 + 2 * 10^1 + 8 * 10^0
    89251 = 8 * 10^4 + 9 * 10^3 + 2 * 10 ^2 + 5 * 10^1 + 1 * 10^0

Instead of using powers of 10 we use powers of 2, we get binary.
    8 * 2^3 + 7 * 2^2 + 3 * 2 + 1
    restrict the digits ==> bits
        0, 1 = bit values

    1010b
    1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 10d

    32 16 8  4  2  1
    1  1  0  0  1  1 b = 32 + 16 + 2 + 1 = 51d

    8 bits = 1 byte
         <====
    1100 0011 b = 1 + 2 + 64 + 128 = 195 d

    0111 0101 b = 1 + 4 + 16 + 32 + 64 = 117d

    traditionally you write binary numbers separated by each 4 bits
        each 4 bits is called a nibble.

    1111 b = 1 + 2 + 4 + 8 = 15 (this is the biggest number you can represent with 4 bits)
    1111 1111 b = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 = 255

    Unicode uses 2 bytes per character instead of 1, you get 65,536 possible values
    binary  decimal     binary      decimal
    0000    0           1000        8
    0001    1           1001        9
    0010    2           1010        10
    0011    3           1011        11
    0100    4           1100        12
    0101    5           1101        13
    0110    6           1110        14
    0111    7           1111        15


Let's talk now about converting decimal into binary.

Take for example 21

    First thing you do is mod by 2
    Divide by 2

    21 % 2 == 1
    21 // 2 = 10

    10 % 2 = 0
    10 // 2 = 5

    5 % 2 = 1
    5 // 2 = 2

    2 % 2 = 0
    2 // 2 = 1

    1 % 2 = 1
    1 // 2 = 0
    <=====
    10101 is this right?
    16 + 4 + 1 = 21 (you dont have to check but it's always good)

    183 (harder)
    183 % 2 = 1
    183 // 2 = 91

    91 % 2 = 1
    91 // 2 = 45

    45 % 2 = 1
    45 // 2 = 22

    22 % 2 = 0
    22 // 2 = 11

    11 % 2 = 1
    11 // 2 = 5

    5 % 2 = 1
    5 // 2 = 2

    2 % 2 = 0
    2//2 = 1

    1 % 2 = 1
    1 // 2 = 0 (stop)


    <===
    1011 0111
    Check our work:
    128 + 32 + 16 + 4 + 2 + 1 = 183 (yep)
"""

def dec_to_bin(x):
    binary_num = ''
    if x == 0:
        return '0b0'

    while x > 0:
        if x % 2 == 0:
            binary_num = '0' + binary_num
        else:
            binary_num = '1' + binary_num
        x //= 2

    return '0b' + binary_num


n = int(input('Tell me a number: '))
while n != -1:
    print(dec_to_bin(n), bin(n))
    n = int(input('Tell me a number: '))


"""
Let's talk about hexadecimal.

    Computers don't work in base 16, so why bother with this?
    
    hex = base 16
    
    16 possible digits
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a = 10d, b = 11d, c = 12, d = 13, e = 14, f = 15
    10 hex = 1 * 16 + 0 * 1
    
    
    25 hex = 2 * 16 + 5 = 32 + 5 = 37 dec
    
    c7 hex = 12 * 16 + 7 = 12 * 12 + 12 * 4 + 7 = 199
    
    127 hex = 1 * 16^2 + 2 * 16 + 7 = 256 + 32 + 7 = 295 
    
    a3b2 hex into decimal
        hard
        a * 16^3 + 3 * 256 + b * 16 + 2
        10 * 4096 + 3 * 256 + 11 * 16 + 2
        40960 + 768 + 176 + 2 = 946 + 40960 = 41906
        
    Why Hex?
    bin     dec hex     bin     dec hex
    0000    0   0       1000    8   8
    0001    1   1       1001    9   9
    0010    2   2       1010    10  a
    0011    3   3       1011    11  b
    0100    4   4       1100    12  c
    0101    5   5       1101    13  d
    0110    6   6       1110    14  e
    0111    7   7       1111    15  f
    (Rule: 1 + 1 = 0, carry)
    0000 1111 1111 0000 = 0ff0
    
    0000 1111 1111 0000 0000 1111 1111 0000 0000 1111 1111 0000 0000 1111 1111 0000    
    
    (because 16 = 2^4 exactly 4 bits is one hex digit, not an accident, why hex was picked)
    
    5ac4bff2 into binary
    0101 1010 1100 0100 1011 1111 1111 0010
    abcd1234
    1010 1011 1100 1101 0001 0010 0011 0100
    4acef7
    0100 1010 1100 1110 1111 0111
    
    
    Equally easy: converting from binary into hex
    
    0010 0011 1110 1111 0101 1010 1110 1010 0011
    23ef5aea3
    
    110101 => 0011 0101 or NOT(1101 0100) (this one multiplies the number by 4)
    0x35
    
    1101 1100 1001 => 0xdc9
    
    
    what have we done?
    dec <-> binary
    binary <-> hex
    
    what's left?
    dec <-> hex [hard not nice]


    hex => dec [these we've done]
    
    a34 => a * 16^2 + 3 * 16 + 4 = 10 * 256 + 48 + 4 = 2560 + 52 = 2612
    ff => 15 * 16 + 15 = 160 + 80 + 15 = 255 correct 2^8 = 256
    
    hardest one (most annoying)
    
    how do you convert a decimal number into hex?
    
    281 into hex
    while the number > 0
        mod by 16
        divide by 16
    
    281 % 16 = 9
    281 // 16 = 17
    
    17 % 16 = 1
    17 // 16 = 1
    
    1% 16 = 1
    1 // 16 = 0
    <==== 
    0x119
    
    
    52938 into decimal
    52938 % 16 = 10 (a)
    52938 // 16 = 3308
    
    3308 % 16 = 12 (c)
    3308 // 16 = 206
    
    206 % 16 = 14 (e)
    12 
    
    12 % 16 = 12 (c)
    12 // 16 = 0 done
    <====
       0xceca
    
"""

x = 0xdc9 # actually hex

print(hex(x))

