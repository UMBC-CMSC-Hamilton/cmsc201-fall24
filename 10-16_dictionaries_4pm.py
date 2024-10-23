"""
    Dictionaries == hash tables or hash maps

        With a list for instance, you get
        [a, b, c, d, e]
         0  1  2  3  4
        Problem with lists:
            if its not sorted or not arranged in any way you have to search the entire list
            potentially to find an element.  Even if you use the in keyword it still has to scan
            each element in the list up to the element that you're looking for.
        Question: Is there a better way to create a collection of data where you don't always
            have to search for each individual element?
        Yes.

        Create key: value pairs, key is usually a string or integer that you can look up very
            quickly without scanning all the other keys.
"""

empty_dictionary = {}
another_way_empty = dict()

sample = {'a': 7, 'b': 14, 'r': 31, 'z': 27, 'y': 81, 61: 32}
print(sample)
"""
How do you access a value out of a dictionary?
    You need to know its key
    
Dictionaries can have mixed types for both keys and values, but generally avoid that
    because you might want the keys to all be operated on by the same code
    if you mix types you might cause TypeErrors
"""
print(sample['a'], sample['r'], sample['z'], sample[61])

sample['a'] = 77  # this overwrites the previous 'a'
sample['t'] = 90  # this is how you add a key to a dictionary
print(sample)

tricky = {'a': 5, 'b': 3, 'c': 281, 'a': 53}
print(tricky)

"""
Keys have to be unique and immutable
    string, int, bool, float, NoneType... more interestingly datetime
    
    floats [to be avoided, roundoff error]
    
"""
# roundoff error
print(10 / 3, 2 + 4 / 3)
floaty = {}
floaty[10 / 3] = 'hello'
floaty[2 + 4 / 3] = 'robot'
print(floaty)

floaty[True] = 5
floaty[False] = 17
print(floaty)

"""
    use ints and strings, avoid bools and floating points for these reasons
"""

"""
    how can we scan through a dictionary?
"""
scan_dict = {'forthwith': 88, 'crazy': 4, 'sushi': 97, 'really': 200, 'fight': 8, 'silly': 8}
for word in scan_dict:
    if word[0] == 's':
        print(word, scan_dict[word])
    else:
        print(word, 'does not need to be looked up')

"""
    How do you remove from a dictionary?
        Use the del keyword
"""
"""
Be careful of this accident:
x = 5
print(x)
del x
print(x)
"""

# need the brackets or else the dictionary will be removed
del scan_dict['sushi']
print(scan_dict)
the_word = input('What key should I access? ')

# when we use the in keyword it's specifically only looking at keys, not values
if the_word in scan_dict:
    print(scan_dict[the_word])

if 200 in scan_dict:
    print('200 is in there')
else:
    print('200 is not? in there??')

# if you actually want to search for it, you use a loop:
for word in scan_dict:
    if scan_dict[word] == 200:
        print(word)


def count_words(a_string):
    list_of_words = a_string.split()
    word_counts = {}
    for word in list_of_words:
        word = word.strip('<>?!@#$%^&(),.{}[]\\|/`~\"\'').lower()
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    return word_counts


with open('tales_of_egypt.tex', 'rb') as tales_file:
    text = tales_file.read()
    my_string = text.decode('latin-1')
    print(count_words(my_string))

"""
    Dictionaries keys have to be immutable but values can be anything, including
        lists and dictionaries
"""

grades = {'eric8': [31, 99, 21, 77],
          'henry5': [21, 56, 99, 23],
          'jill77': [55, 66, 77, 88],
          'ke9843': [12, 23, 45, 56]}

grades['jill77'][3] = 97
for username in grades:  # username is the key
    total = 0
    for grade in grades[username]:  # grades[username] is the list
        total += grade
    print(f'user {username} has a total of {total} and average {total / len(grades[username])}')

students = {'eric8': {'name': "Eric", 'gpa': 3.6, 'classes': ['cmsc201', 'cmsc441']},
            'robert7': {'name': 'Robert', 'gpa': 3.9, 'classes': ['art101', 'cmsc431']}
            }

for username in students:
    print(students[username]['name'])

"""
    Why cant you use a list or a dictionary as a key?
        1) it produces a TypeError
        2) But really? WHY!? because if the list can change then you dont know where the key is
        

d = {}
test = [1, 2, 3]
d[test] = 4
test.append(8)
print(d[test])
"""
