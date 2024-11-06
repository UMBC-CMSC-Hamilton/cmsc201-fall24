"""
    Number Systems:
        456 = 4 * 100 + 50 * 10 + 6
        1052 = 1 * 10^3 + 0 * 10^2 + 5 * 10^1 + 2 * 10^0
                   ^           ^         ^          ^
        decimal chooses this base to be 10

            digits go from 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 = 10 of these digits
            10 is not a digit, 10 is actually a combination of digits 1 * 10 + 0 * 10^0
            we can write numbers uniquely like this

            123 = 11[13] this doesnt really happen.
            .9999999999999999 (forever) = 1
            1 - .9(forever) = 0.0(forever)(after forever/after infinity)1

        base = 2

        What does that change?
            we can't use the digits 0-9 anymore because

        3 * 2 + 1 (uniqueness is broken)
        4 + 2 + 1
        we can only use the digits 0 and 1 for binary (base 2 arithmetic)

        16  8   4   2   1
        1   0   1   1   0
        16 + 4 + 2 = 22 thats it
        places 8421
        value  0110 = 4 + 2 = 6

        separate bits into packs of 4 as it turns out they have a name, 4 bits is a nibble
        128 64  32  16  8 4 2 1
        1   1   1   0   0 1 0 1

        1110 0101 = 1 + 4 + 32 + 64 + 128 = 229
        8 bits make a byte

        2048 1024 512 256   128
        1    1    0    1    0011 1001
        2048 + 1024 + 256 + 32 + 16 + 8 + 1 = 3072 + 256 + 57 = 3072 + 313 = 3385

        binary => decimal

        decimal => binary

        while num > 0
            add num % 2 to the front of the number
            num = num // 2

        43 into binary
        43 % 2 = 1 (first digit is 1)
        43 // 2 = 21

        21 % 2 == 1
        21 // 2 = 10

        10 % 2 == 0
        10 // 2 == 5

        5 % 2 == 1
        5 // 2 == 2

        2 % 2 = 0
        2 // 2 = 1

        1 % 2 == 1
        1 // 2 == 0
        <======
        101011
        a = answer * 4  b = 43
        1010 1100 or    0010 1011
        1 + 2 + 8 + 32 = 43 yes we did it
        0010 1011
        Think about it like this:
            $007 <- leading zeros are ok, putting them on the end is multiplication instead

        241 into binary
        120 (even) => 60 (even) => 30 (even) => 15 (odd) => 7 (odd) => 3 (odd) => 1(odd)=> 0 (done)
        1111 0001
        128 + 64 + 32 + 16 + 1 = 128 + 32 + 64 + 16 + 1 = 160 + 80 + 1 = 241

        594 into binary
        594 (even) => 297 (odd) => 148 (even) => 74 (even) => 37 (odd) => 18 (even) => 9 (odd) => 4(even)
        4(even) => 2(even) => 1(odd) => 0 (done)
        0010 0101 0010

       512 + 64 + 16 + 2 = 594 we got it.


    binary <-> decimal
    Let's talk about hex.

        hexadecimal is base 16 = 2^4 (thats why)

        numbers can be written

        ___ ___ ___ ___
        4096 256 16  16^0
        Probem: with binary we stole 0 and 1 and reused them
        how many digits {hex digits} do we need?
        X * 16^3 + Y * 16^2 + Z * 16 + W
        steal again 0, 1, 2, 3, 4, 5 ,6, 7, 8, 9, a = 10, b = 11, c = 12, d = 13, e = 14, f = 15
            you'll see both ABCDEF and abcdef case doesn't matter

        Big Chart:
        binary  dec     hex     binary  dec hex
        0000    0       0       1000    8   8
        0001    1       1       1001    9   9
        0010    2       2       1010    10  a
        0011    3       3       1011    11  b
        0100    4       4       1100    12  c
        0101    5       5       1101    13  d
        0110    6       6       1110    14  e
        0111    7       7       1111    15  f
          111
          0111
        + 0001
          1000 [1 + 0 = 1, but 1 + 1 = 0 and then carry]
        0110 1110 0011 1010 1111 0001 0000
        6e3af10

        1101 0010 1001 0011 0100 0000 1100 1010
        d29340ca

        5aef89c we can convert this into binary the same way
        [remember the leading 0s]
        0101 1010 1110 1111 1000 1001 1100

        24aef8
        0010 0100 1010 1110 1111 1000

        decimal <-> binary
        binary <-> hexadecimal
        decimal <-> hexadecimal

        hex => dec

        a33 (hex)

        10 * 256 + 3 * 16 + 3 = 2560 + 48 + 3 = 2611

        4c5a into dec
        4 * 16^3 + 12 * 16^2 + 5 * 16 + 10
        4 * 4096 + 12 * 256 + 5 * 16 + 10
        16384 + 2560 + 512 + 80 + 10 = 16384 + 3162 = 19546

        f3 = testable nicely = 15 * 16 + 3 = 240 + 3 = 243

        Converting directly from decimal into hex

        while num > 0
            add num % 16 to the front
            divide by 16 [int divide]


        5381 into hex
        5381 % 16 = 5
        5381 // 16 = 336

        336 % 16 = 0
        336 // 16 = 21

        21 % 16 = 5
        21 // 16 = 1

        1 % 16 = 1
        1 // 16 = 0 (done)

        <===
        0x1505 [hex number]

        0b1010 binary
        1010 [dec]
        0x1010 hexadecimal



"""

x = 0o123
print(x)

"""
in python there are two built in function that do this
"""

x = int(input('Num: '))
while x != -1:
    print(x, bin(x), hex(x), oct(x))
    x = int(input('Num: '))