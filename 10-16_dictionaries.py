"""
    Dictionaries = Hash Tables/Hash Maps something like that

        When you have lists, a list is a collection of elements indexed from 0 ... (len - 1)
        One issue with a list is that if you want to know if an element is inside of a list
            you have to use either a loop or the in keyword or something like that.
            If the list is large then there's a lot of things to scan over and this can slow
            down your programs.
        Is there a better way?
            Yes we can use dictionaries

        Keys are used to store values, things are stored as key: value pairs

    Keys can be anything that is immutable in python:
        bool, int, strings, floats [recommend against]
"""

my_empty = {}
another_empty = dict()

my_dict = {'ab': 17, 'cd': 3, 'ar': 13, 'df': 0, 'dx': 223}
print(my_dict['ab'], my_dict['dx'], my_dict['ar'])

my_dict[53] = 24
my_dict[72] = 'happy'
print(my_dict)
my_dict[True] = 'it is very true'
my_dict[False] = 'Yep false too'
print(my_dict[False])

"""
    The in keyword only checks keys not values
"""

wordle_words = {'gamut': 100, 'happy': 2, 'hello': 4, 'robot': 17, 'welsh': 53}
if 'happy' in wordle_words:
    print('Happy was used in wordle')
if 'poset' in wordle_words:
    print('Is that even a word? yes technically it means partially ordered set')
else:
    print('You are a liar')

if 100 in wordle_words:
    print('Yep that is')
else:
    print('It is not because it is a value not a key. ')

"""
    How does it perform with for loops?
        It works like a for each loop but it outputs keys not values
"""
for word in wordle_words:
    print(word, wordle_words[word])

"""
keys have to be unique
"""
wordle_words['verily'] = 42
wordle_words['verily'] = 65
print(wordle_words)

try_dict = {'a': 4, 'b': 7, 'c': 25, 'a': 9}
print(try_dict)

"""
    Keys are unique, pick a system where the keys should be unique
        if there's repetitions you want to figure out what to do about that.
"""


def count_words(a_string):
    split_string = a_string.split()
    counts = {}

    for word in split_string:
        word = word.lower().strip(':,.\'\"!@#$%^&*()?<>')
        if word in counts:
            counts[word] += 1  # for all the counts after the first
        else:
            counts[word] = 1  # we found the first one

    return counts


my_string = input('Tell me a string to count')
print(count_words(my_string))


with open('hunting_ballads.txt', 'rb') as ballad_file:
    char_read = ballad_file.read().decode('latin-1')
    print(count_words(char_read))


"""
let's get back to dictionaries, stop trying to clean files

What if you want to remove a key from a dictionary?

del keyword, make sure you get the format right
"""

happy_map = {'h': 5, 'a': 29, 'p': 81, 'y': 2, 'z': 15}
del happy_map['z']
print(happy_map)

"""
KeyErrors happen when the key is not in the dictionary.  
    Remember that you have the in keyword to test
"""
key = input('What key should we get? ').strip().lower()
if key in happy_map:
    print(happy_map[key])
else:
    print('That was not a letter in our thing. ')

"""
    I want to mention the .keys() and .values() functions
    
"""

# this is unnecessary because the keys are already the thing accessed
# when you do for letter in happy_map, no reason to type this extra function
for letter in happy_map.keys():
    print(letter)

students = {'ab2345': 'Eric', 'cd123123': 'Robin', 'ur984398': 'Greg', 'tf9843': 'Henry'}
print(students.keys())
print(list(students.keys()))
student_id_list = list(students.keys())  # the one valid use that i can think of.

"""
Slightly more useful is .values():

    
"""
print(students.values())

students = {'eric8': {'name': 'Eric', 'gpa': 3.7, 'classes': []},
            'robert7': {'name': 'Robert', 'gpa': 2.9, 'classes': ['ART101']}}

print(students)

print(students['eric8']['name'])

"""
Why keys have to be immutable but values dont care:
    note: datetime object    
    if you modify a key, then the value gets to move around the dictionary
        it makes it impossible to know whether using a key will find the thing you're looking for
        or if its been moved
        
Values can and often do change, but we dont use them to look anything up, so it's ok
"""
"""
not allowed:

my_list = [1, 2, 3]
cant_do_this = {my_list: 'hello there'}
my_list.append(4)
cant_do_this[[1, 2, 3]] or [1, 2, 3, 4]?
"""

# this is immutable
from datetime import datetime

"""
What else can we do with dictionaries?
"""
my_nesting = {'a': [1, 2, 3], 'b': [2, 3, 4, 5, 6], 'c': [6, 7, 8, 9, 9]}

# remember that letter is always the key, if you want the value you must access my_nesting[letter]
for letter in my_nesting:
    print(letter)
    total = 0
    for x in my_nesting[letter]:
        total += x
    print(f'The total for {letter} is {total}')

print(my_nesting['b'][4])

test_dict = {'g': 2, 'd': 4, 'e': 8, 'c': 7, 'a': 7}

value = int(input('What value should we look for? '))
for x in test_dict:
    if test_dict[x] == value:
        print(x)
