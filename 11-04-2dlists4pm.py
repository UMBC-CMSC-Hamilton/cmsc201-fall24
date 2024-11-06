"""
    Midterm next wednesday.

    Let's talk about 2d lists.



"""

my_2d_list = [[1, 2, 3, 4, 5, 6],  # index 0
              [1, 2, 3, 4],  # index 1
              [9, 8, 7, 6, 5, 4, 3, 2, 1],
              [5, 4, 6, 4, 3, 5, 5, 6, 5],
              [4, 3, 3, 4, 4, 3, 3, 4, 4, 3, 34, 3],
              [1, 2, 3]]  # index 2

print(my_2d_list[2])
print(len(my_2d_list))
"""
    Notice that the length of the outer list doesnt match with the length of the inner lists.
        It can if you have a chessboard or checkers board or something like that.
    Notice that the lengths of the inner lists also don't match.  
"""

for row in my_2d_list:
    for element in row:
        print(element, end=' :: ')
    print()

"""
What I want to do is modify all the odd elements, I want to square them.
"""
for i in range(len(my_2d_list)):
    for j in range(len(my_2d_list[
                           i])):  # without this[i] index we are using the length of the outer list instead of the inner lists
        if my_2d_list[i][j] % 2 == 1:
            my_2d_list[i][j] **= 2
        print(my_2d_list[i][j], end=' ')

    print()

""""
if you want to create an empty list with a certain number of rows and columns... then
"""

ROWS = 7
COLS = 12

grid_list = []
for i in range(ROWS):
    new_row = []
    for j in range(COLS):
        new_row.append('.')
    grid_list.append(new_row)

new_row[5] = 'T'
grid_list[3][11] = 'R'

for row in grid_list:
    print(' '.join(row))
"""
Alternative to the first way.
"""

new_grid = []
new_column = []
for i in range(COLS):
    new_column.append('+')

for i in range(ROWS):
    new_grid.append(list(new_column))  # this is the list copy constructor, makes a duplicate list
    # if you dont use the list constructor we run into the duplicate problem

new_grid[0][5] = 'x'
new_grid[2][3] = 'v'
new_grid[5][10] = 'q'

for row in new_grid:
    print(' '.join(row))

# list comprehensions are unfortunately banned
comp_grid = [['+' for _ in range(COLS)] for _ in range(ROWS)]
# it exists in python but not really in other languages, you need to know how to do things in general
# notice that actually it is 2 for loops just collapsed into one line of code, not different from what we're doing


"""
    
"""

my_favorite_list = [[1, 2, 5, 10], [2, 3, 3, 3, 3, 3], [9, 5, 8, 3, 6, 1], [1, 1]]
new_favs = list(my_favorite_list)
print(new_favs)
new_favs[2][3] = 1001
new_favs.append([5, 5, 5, 5, 5])
print(my_favorite_list)  # notice that the favorites are actually changed, but the 5, 5, 5, list is not there
# new_favs is actually a new list, so the 555s only went into that list, but most of the sublists are shared
print(new_favs)

"""
list copy is only 1 deep
    it makes a copy of the outer list, but if the list contains lists, it just copies the references
    it doesn't work recursively
"""

copy_favs = []
for row in my_favorite_list:
    copy_favs.append(list(row))

copy_favs[2][2] = 20000
print(my_favorite_list)


def recursive_copy(a_list):
    the_copy = []

    for x in a_list:
        if isinstance(x, list):
            the_copy.append(recursive_copy(x))  # will only happen if its a list
        else:
            the_copy.append(x)  # if it is immutable

    return the_copy


"""
Deep Copy - a copy where the underlying data is copied into new memory. [If you modify the copy, 
    the original is unchanged]
    A copy that is true.
    
Shallow Copy - "a copy" where the underlying data is a reference to the original data
    if you modify the shallow copy, the original data is also modified.
    
    Shallow copies are not copies, they are references/renamings of the original data/variable
"""

"""
    I want to do a bit of 2d list nonsense in an example, ... checkers
"""


def create_board(size):
    new_row = []
    for i in range(size):
        new_row.append(' ')

    the_board = []
    for i in range(size):
        the_board.append(list(new_row))
    # at this point we have an empty board, wow...

    for i in range(len(the_board)):
        for j in range(len(the_board[i])):
            if (i + j) % 2 == 0:
                if i < 3:
                    the_board[i][j] = '\u25ef'  # extended unicode use \U
                elif i == 3 or i == 4:
                    the_board[i][j] = '\u25a1'
                else:
                    the_board[i][j] = '\u2b24'

    print('\U0001f4a9')

    return the_board


def display_board(the_board):
    print(' ', ' '.join([str(i + 1) for i in range(8)]))
    index = 1
    for row in the_board:
        print(index, ' '.join(row))
        index += 1


def play_game():
    game = create_board(8)
    display_board(game)

    turn_count = 0
    player_pieces = ['\u25ef', '\u2b24']

    while True: # changed to while not victory(game):
        pos_str = input('Enter a position row col sep. by spaces: ')
        position = pos_str.split()
        position = [int(position[0]) - 1, int(position[1]) - 1]

        if game[position[0]][position[1]] == player_pieces[turn_count % 2]:
            dest_str = input('Enter a position row col sep. by spaces: ')
            destination = dest_str.split()
            destination = [int(destination[0]) - 1, int(destination[1]) - 1]
            # is that a legal move?
            # would that be a capture?
            game[destination[0]][destination[1]] = player_pieces[turn_count % 2]
            game[position[0]][position[1]] = '\u25a1'

        display_board(game)

        turn_count += 1


play_game()
