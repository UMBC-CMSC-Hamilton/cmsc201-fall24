"""
    Slices:
        Slices are a way to get a substring using a specific python notation
        list slices
        string slices
        works a bit like the range object but you can extract a substring or sublist using
            start, stop step
        Difficulty is really the syntax
    File IO = File Input - Output
"""

my_string = 'asdfjkqweruioxasfdjklsafdlkj'
print(my_string[3:7])
# inclusive start and exclusive stop [doesnt include it]
another_string = 'abababababababababababab'
print(another_string[0:len(another_string):2])
# what if you want the b's?
print(another_string[1:len(another_string):2])

weird_thing = 'hello i am a string'
# doesnt produce an index error... huh? ok
print(weird_thing[0:200000])

print(weird_thing[len(weird_thing) - 1: 0: -1])
"""
with slices:
    start = 0 or len(string or list) - 1 if you're going forward or backward
    stop = len(string or list) or 0 if you're going forward or backward
    step = 1
"""
# this is equivalent to reversing the string
print(weird_thing[::-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# if you see this [:] == [0: len(my_list)] = copy of the list
print(my_list[:])


def my_split(a_string):
    WHITESPACE = [' ', '\t', '\r', '\n']
    # index is "invalid currently"
    split_list = []
    first_index = -1
    for i in range(len(a_string)):
        if first_index == -1 and a_string[i] not in WHITESPACE:
            first_index = i
        elif first_index != -1 and a_string[i] in WHITESPACE:
            split_list.append(a_string[first_index: i])
            first_index = -1

    if first_index != -1:
        split_list.append(a_string[first_index:]) # [first_index:] == [first_index: len(a_string)]

    return split_list


print(my_split('hello i am a set of words please split me'))

print("XXXX4321YYYYZZZZ"[4: 8])


"""
File IO - Need to be able to read and write to files
    Up to this point, nothing you have done can persist past the time your program exits
"""


# the second argument is the mode, and it's a string, it can be either r, w, a,
#           rb, wb, ab - reading writing appending as pure bytes
# read =
# write =
# append =
the_file = open('the_file.txt', 'r')
print(the_file.read())
the_file.close()


print('Time to readlines: \n')
the_file = open('the_file.txt', 'r')
print(the_file.readlines())

print('Now I am going to read again')
# seek will take you to position i in the file
# the_file.seek(0)
# this shouldn't get anymore data because the cursor is at the end of the file.
print(the_file.read())
the_file.close()
"""
    When reading data in from the file you should be aware that the data does not have the
        newlines taken out.
"""

the_file = open('the_file.txt', 'r')
my_string = the_file.readline()
print(my_string, end='')
my_string = the_file.readline()
print(my_string, end='')  # or you could strip the newline
the_file.close()

with open('the_file.txt') as the_file:
    for line in the_file:  # call to readline every time
        print(line.strip())
    # with construction will auto-close the file

# it's a different file name, it creates the first time you open with write mode
with open('new_file.txt', 'w') as nf:
    my_string = input('What do you want to type into the file? ')
    while my_string.strip().lower() != 'quit':
        # write command doesn't add the newline into the string
        nf.write(my_string + '\n')  # you have to put the newline into the string so that it will do what you want
        my_string = input('What do you want to type into the file? ')

"""

WARNING:
    write mode will erase the file - don't open any file you care about in write mode
    
How do I open a file and write more stuff in it?
    there's an append mode (opens the file with write PERMISSIONS but doesn't blank the file)
    
"""

with open('new_file.txt', 'a') as append_file:
    list_of_strings = []
    my_string = input('What do you want to type into the file? ')
    while my_string.strip().lower() != 'quit':
        # write command doesn't add the newline into the string
        list_of_strings.append(my_string + '\n')
        my_string = input('What do you want to type into the file? ')

    # the reason i added the newlines is because this function won't
    append_file.writelines(list_of_strings)


