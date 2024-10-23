"""

    Slices - A way to get a substring or a sublist
        convenience notation

    notation uses brackets:
        [start: stop] = starts at start and goes up to but not including stop

"""

a_string = 'abcdefghij'
# start inclusive, stop exclusive [doesn't include it]
print(a_string[2:7])
print(a_string[0:5])
print(a_string[5: len(a_string)])

my_list = [2, 7, 4, 8, 4, 3, 5, 6, 7, 8, 6, 4, 3, 5, 7]
print(my_list[4:12])

date_string = "10/14/2024"
day = date_string[3:5]
month = date_string[0:2]
year = date_string[6:10]

print(day, month, year)
# be careful because if the data ever comes in a different format it won't align perfectly
new_date_string = "3/5/24"
day = new_date_string[3:5]
month = new_date_string[0:2]
year = new_date_string[6:10]
print(day, month, year)
print(new_date_string.split('/'))

random_string = 'kjfdskjfdsfdsfds'
print(random_string[5:800000000])

garbage = 'g'
# any invalid slice will give you an empty string, this can be a problem if you then say access an index
my_slice = garbage[200:2000]
# print(my_slice[3])
"""
Slice defaults
    string[start: stop: step (optional)]
    
    start defaults to zero, stop will default len(list) or len(string)  
"""
another_string = 'general kenobi i\'ve been expecting you'
print(another_string[:17], another_string[30:])
random_list = ['hi', 'bye', 'computer', 'turnip', 'truck']

r2 = random_list[:]  # makes a copy of the list
r2[3] = 'opossum'

print(random_list, r2)

# reverses a list, start stop reverse when they're not written and when there's a negative step
print(random_list[::-1])

ab_string = 'ababababababababababababababab'
print(ab_string[::2], ab_string[1:len(ab_string):2])

print(another_string[-5:])

"""
    File IO = File Input-Output
    
    Every program that you've written loses all data when the program ends
    File systems are useful for storing data across instances/usage of a program
    
    There are three modes in python to open files:
        read mode = 'r' reads the file only, cursor gets set to the beginning of the file
        write mode = 'w' opens the file, gives you write permission and then blanks the file
        append mode = 'a' opens the file gives write permissions, sets the cursor at the end of 
            the file. 
"""

my_file = open("the_file.txt", 'r')
print(my_file.read())
my_file.close()

my_file = open("the_file.txt", 'r')
for the_line in my_file.readlines():
    print(the_line.strip())  # end='' also might do it
my_file.close()

my_string = input('hi')
print(list(my_string))
"""
one primary difference between all file methods and print/input
    readlines or readline they do not remove the newlines from the end of the string.
"""

my_file = open("the_file.txt", 'r')
first_line = my_file.readline()
second_line = my_file.readline()
rest = my_file.readlines()  # difference is readlineSSSS
my_file.close()

print(first_line, second_line)
print(rest)

my_file = open("the_file.txt", 'r')
print(my_file.read())
print('Go again')
# if you dont seek then this read produces nothing because the cursor is at the end of the file
# if you do then it'll produce whatever is after the cursor
my_file.seek(52)
# you dont need seek in this class
print(list(my_file.read()))
my_file.close()


with open('the_file.txt') as read_file:
    # line will be a string and read_file must be a file object
    # secretly its calling readline()
    for line in read_file:
        print(line.strip())
    # i would use this in 95% of cases
    # i dont need to close the file, with keyword does it for me


with open('5pmtime.txt', 'w') as write_file:
    in_string = input('>>> [q] to quit >> ')
    while in_string.lower().strip() != 'q':
        write_file.write(in_string + '\n')
        in_string = input('>>> [q] to quit >> ')

    # write_file will be closed by the with block, you don't need to close it

# if you have a list of strings you can call writelines
# writelines is a bit of a lie, more like writestrings

with open('5pmtime.txt', 'a') as write_file:
    my_string_list = ['a', 'Turtle', 'Happy', 'Sandwich', 'Falconry', 'Starfish']

    for i in range(len(my_string_list)):
        my_string_list[i] += '\n'

    write_file.writelines(my_string_list)




