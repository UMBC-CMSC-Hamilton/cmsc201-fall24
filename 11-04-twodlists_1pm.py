"""
Two dimensional [higher dimensional] lists

In python you can store a list inside of a list
"""

list_of_lists = [[1, 2, 3],  # 0 index
                 [2, 3, 4, 5, 6, 7],  # 1 index
                 [5, 6, 7, 8, 9],  # 2 index
                 [10, 11]]  # 3 index

print(list_of_lists[2])
# to access a specific element we'd need two indices:
print(list_of_lists[2][4])
"""
Note:
    number of lists can vary
    
    Using the two index brackets, the first index accesses the outer list and the second
        accesses the inner list.
        
    [important and tricky] Notice that the size of the outer list is not always the size of the
        inner list.
    
    Number of elements in each inner list can also vary.
    
    Often when you have a game board or something uniform, you'll fix the number of rows and 
        columns.
"""
list_of_lists.append([1, 4, 9, 2, 3, 4])
print(list_of_lists)

# i want to make a 8 x 8 empty board to start
chess_board = []
for i in range(8):  # creates the 8 rows of the chessboard
    # forces a new list every time, rather than using the same one
    new_row = []  # new row, very important I'll show you why
    for j in range(8):  # adds 8 empty spaces into the row
        new_row.append(' ')
    chess_board.append(new_row)  # adds the new row into the list

# this hides a lot of the details that you kind of need to understand
# most programming languages dont have this notation...
#  FORBIDDEN:
chess_board2 = [[' ' for _ in range(8)] for _ in range(8)]

checker_board = []
new_row = []
for j in range(8):  # adds 8 empty spaces into the row
    new_row.append(' ')

for i in range(8):  # creates the 8 rows of the chessboard
    # new_row = []  # new row, very important I'll show you why
    # the list constructor will copy a list and make a new copy of it.
    checker_board.append(list(new_row))  # adds the new row into the list

checker_board[2][4] = 'x'

for row in checker_board:
    print(row)

"""
How do we output this list?
"""
new_list = [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [2, 3, 4], [1, 5, 10, 20, 50, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [76, 54, 32, 21]]

print(new_list)

# what if we want to print each individual sublist?
for row in new_list:
    print(row)

# nested for each loop...
for row in new_list:
    for element in row:
        if element % 2 == 0:
            print(element, end=', ')
    print()

"""
If the element is even we print, if it's odd we square the element, store it back in the list 
    before we print it...
"""
print('\n\n')

# gives us the outer index...
for i in range(len(new_list)):
    for j in range(len(new_list[i])): # this little [i] is very important i hope i have convinced you of that
        if new_list[i][j] % 2 == 1:
            new_list[i][j] **= 2
        print(new_list[i][j], end=', ')
    print()

"""
When you're testing any program, if the lists don't have to be of the same size, make
    sure to test lists of not-same-size
"""

"""
    How to copy a 2d list?
    
    (20 + 1)(20 + 1) = 400 + 2(20) + 1
"""
new_list_copy = list(new_list)
print(new_list_copy)
new_list_copy[4][3] = 1001

print(new_list)

"""
    list copy constructor is a deep copy but it doesnt copy sublists
        it's only 1 level deep (that's probably the best way to say it)
    it doesn't go 
"""

# this is making a deep copy of each ROW then it makes a deep copy [true copy] of the entire list
new_list_copy = []
for row in new_list:
    new_list_copy.append(list(row))  # makes a copy of the inner lists


"""
    Deep copy = a copy of an object where the data is actually copied to new memory
        not just a link [reference/pointer] to the previous data.  
        
    Shallow copy = reference = it actually isnt a copy, it's just the same object with 
        two different names. 
        
        That's what the new_list_copy = list(new_list) was doing to the INNER lists...
"""


# total deep copy of a list:
def true_deep_copy(a_list):
    """
        assume what we have is a list of either lists or numbers
        a_list[0] is an integer then the rest will be integers
        otherwise it's a list and needs to be copied
        a_list[0] is also a list then we need to copy it so we need to go down into the list
    """
    # base case is hidden because the for loop wont run...
    copy_list = []
    for x in a_list:
        if isinstance(x, list):
            copy_list.append(true_deep_copy(x))
        else:
            copy_list.append(x)  # this thing may not be a list but may be mutable [assume its int, string, float, whatever]
    return copy_list


sample = [[1, 2, 3, [4, 5, 6]], [2, 2, 2], [[123, 234, 234], [234, 5, 5, 5], [890, [123123]]]]

is_it_a_copy = true_deep_copy(sample)

print(is_it_a_copy)


"""
See if we can implement checkers... to some degree?
"""

"""
Set up a checkers board
"""

def set_up_checkers():

    checkers = []

    row = []
    for i in range(8):
        row.append(' ')

    for i in range(8):
        checkers.append(list(row)) # copy of the empty row, so that we don't that duplication bug.

    for i in range(len(checkers)):
        for j in range(len(checkers[i])):
            if i < 3 and (i + j) % 2 == 0: # put a red piece in the correct places
                checkers[i][j] = '\u25EF'
            elif i > 4 and (i + j) % 2 == 0:
                checkers[i][j] = '\u2B24'
            elif (i + j) % 2 == 0:
                checkers[i][j] = '\u2B1C'

    return checkers


def display_checkers(board):
    print(' ',  ' '.join([str(i + 1) for i in range(8)]))
    index = 1
    for row in board:
        print(index, ' '.join(row))
        index += 1

def play_game():
    my_board = set_up_checkers()
    display_checkers(my_board)
    player_pieces = ['\u25EF', '\u2B24']

    current_turn = 0

    while True:  # because i cant check for victory yet
        # not victory(my_board)
        """
            Add a ton of safety checks
            is it a valid position, is a valid destination?
                hint: make helper functions
                
            Add capturing
            Add king making and movement
        """
        position_str = input('Tell me the index (space sep) of the position [eg 1 4]: ')
        position = position_str.split()
        position = [int(position[0]) - 1, int(position[1]) - 1]
        if my_board[position[0]][position[1]] == player_pieces[current_turn % 2]:
            dest_str = input('Tell me the index (space sep) of the position [eg 1 4] to move to: ')
            destination = dest_str.split()
            destination = [int(destination[0]) - 1, int(destination[1]) - 1]

            my_board[destination[0]][destination[1]] = player_pieces[current_turn % 2]
            my_board[position[0]][position[1]] = '\u2B1C'

        display_checkers(my_board)

        current_turn += 1


play_game()