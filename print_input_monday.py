"""
    Download python from python.org
    Download pycharm from https://www.jetbrains.com/pycharm/download/

    To create a new file, you right click on the project and select new python file.

    Right click on the file and run it for the first time. After that you can use the play
        buttons.
"""

"""
    Print and Input
    
    What about print?
        Outputs strings to the console.
            A string is a sequence of characters [letters, numbers, punctuation, other symbols]
"""
print('Hello #$%^&*')
print('Anything you want, as long as it is in tic marks/apostrophes/single quotes')
print("You can use double quotes for strings too.")
print("what if you want to use a \"quotation mark\" inside of this? ")
# when you use the slash it is an escape sequence
"""
Escape Sequences that you need:
    \n = newline
    \t = tab
    \r = carriage return
    \" = quotation mark
    \' = single quote
    \\ = single backslash
    
    in linux, mac, \n is all you need
    in windows every time you see a newline it's actually two characters \r\n
    
"""
print('\\the python is a snake')
"""
You can also print numbers, integers or floats

integers are whole numbers 1, 2, 3, 4, 5, 291238321, also 0, -27

float = floating point (point is the decimal point)
3.1, 9.23123, -0.0021, 5.0 [python interprets this as a float not an integer]

    there's no double type, dont have to worry about the difference in precision.  
"""

print(5, -2, 17, 5.3, 27.1234)
print("5", 5)
# we have an encoding called ASCII which gives numbers to each character
# "5" has a value of 53
print(ord("5"), "5" + str(7), int("5") + 7, "abc" + "def")

"""
    Variables
        A variable is a location in memory where data is stored.  A variable has a name, 
            the reason is because remembering these numbers would get extremely complex.
"""

x = 17
# int x = 17; not necessary
my_name = "Eric"
welcome_string = "Hello and welcome to the program."
print(x, my_name, welcome_string)
pi = 3.14159265358979
print(pi)

"""
Use variables to get use input

input("prompt string goes here")

the returned value from input is ALWAYS a string
"""

movie = input('Tell me a movie name: ')
the_number = int(input("tell me a number: "))

print(movie)
print(the_number + 5)
"""
We dont require you to make all of your code type safe, if you ask for an int
    you will get an int, if you ask for a float, you get a float, etc.
    If you ask for a positive integer, we can give you -17
"""

radius = float(input("What is the radius? "))

print(f"The best movie ever is {movie}")
print(f"The area of the circle is {pi * radius ** 2}")

# the C-style printf weirdness
x = 25
print("The number is %d" % x)
print("{}".format(x))

"""
    remember order of operations

    parentheses
    ** exp
    * / // % at the same "precedence"
    + -
    
    25 / 5 * 2 = 10 
"""
print(5 ** (1/2))

"""
    Variable naming conventions
    
        Python Legal:
            good_var
            my_int_3
            MyInteger
            
            letters, numbers, underscores
            case sensitive (X != x)
            cant start with a number
            
        
        python Illegal:
            special characters
            avoid mixing case
            3_blind_mice
            super!

    Python Coding Standard (PEP8)
        snake case = lower case letters with underscores between words
            
"""

# 3_blind_mice = 5
# really_super! = 7
# $perl = 52

_my_variable = 'hi'
__two_underscores = 4
___three = 3
_3 = 4


