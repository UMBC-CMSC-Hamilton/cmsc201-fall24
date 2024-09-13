"""
    Lecture for 9-4 : Print and Input

        How do we display things?
            We use the print function (built-in python function)

"""
print('Single quote string')
print("Double quote string")

print("CMSC 201 is the greatest class, until any other class...")

# single line comment, if you need a single line comment, use the hash-tag/pound sign
# What other kinds of things can we print?
# what we have done is print a string, but we can also print integers, floats, booleans, and more
print(4, -17, 25385, 987321321321987987987432)
# floats being printed
print(3.2, 2.7182818459, 1.618, -32.765)
# random types being printed
print("hi", 3.14, 2, -2, 7.89)

print(True, False)
print(True * True, False * False)
print(True + 1)

"""
    Variables
        A way to remember data in ram. 
        A variable needs a name - so that we can recall that variable when we need it
        
"""

x = 3
print(x)

pi = 3.14159265358979

print(pi)

welcome_message = "hello there, welcome to cmsc201 "
print(welcome_message)

print(welcome_message, pi, x)

print(4 * x + 7)
print(3 + x ** 2, (3 + x) ** 2)
print(16 ** 1/2, 16 ** (1/2))

"""
    How do you get data into your program from the user?
    
    There's an input function that allows us to get data from the user
        Takes an argument which is the prompt that it's going to tell you
        
        print(something) <-- something is the argument inside of the print function
        input(prompt string) <-- print the string first then ask the user for input
        
        what is returned from the print function is a string which is what 
            the user has typed
"""
# the_word <<--- whatever comes out of the input function is what we get
the_word = input("Tell me a word: ")

print('You have said', the_word)

# you can use casting to change the type of a variable, maybe if it works
fav_num = int(input("Tell me your favorite number: "))
print('Your favorite number plus one is: ', fav_num + 1)

# you do need to worry about the values, don't worry about the types
positive_number = int(input("Tell me a positive int: "))
print(positive_number)

floaty_mcfloatface = float(input('Tell me a floating point number: '))
print(floaty_mcfloatface)

really_an_int = int(input('Tell me a float (this is a lie): '))

number = 17.998
print(int(number))

print(type(17.0), type(17))

