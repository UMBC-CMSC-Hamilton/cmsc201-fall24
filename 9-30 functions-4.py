"""
    Our first exam will be on Wednesday Oct 9th. In Class.
        Monday we will go over that practice exam in class.
        MCQ - usually ~ 10-12
        Lists - indices, elements
        short answer - concept questions
        code output problems - read code and tell me what happens
        debugging - you read code and find errors in it
                    you fix them.
        coding problems you write code by hand.
            10-15 line solutions at most
            goal: you can write the answer in < 5 minutes + 5-10 thinking
            goal for me: compile 8-10 problems with solutions [practice]
            practice writing the answers on paper.
"""

# constants

# functions go here
def main():
    # python doesn't care about this function in particular
    # it sees main as the same as any other function
    # doesn't call it when the program starts...
    print('do something here this is the main')
    print('in most programming languages, main gets called automatically')
    print('but in python what happens? ')

# this is a 'secret' variable that gets created when you run the script or import a file
# the file that you run or that the user runs is named __main__ as a string.


import main_script

print(__name__)
if __name__ == '__main__':
    # non-function code that calls your functions.
    # main()
    pass
    # put all your code in here

"""
    What about functions?
        functions are a way to make code more modular so that you can have a piece of 
            functionality which gets called multiple times.
        reduces repetition
        helps with debugging
        a function should really do "one job"
        
        functions have input (parameters) and output (return)
            when I say output i don't mean output to a screen, i mean output back to the rest
            of your program.  
            
        Tic Tac Toe
        play_game = play the game
            fill_box = mark a box as X or O
            switch_players (don't need a function for this, I'll show you)
            check_victory = check the board for a win
                check_rows
                check_cols
                check_diags
"""

#            in_string is a parameter
def count_as(in_string):
    count = 0
    for x in in_string:
        if x.lower() == 'a':
            count += 1

    return count


s1 = input('Enter a string with as: ')
s1_count = count_as(s1)

another_string = input('Enter a string with as: ')
another_count = count_as(another_string)

print(s1_count, another_count)


def my_function(x):
    if x == 1:
        print('hi')
        return

    if x < 5:
        print('byte')

    if x < 10:
        print('nibble')
    else:
        print('big')

my_function(1)
print('-'*30)
my_function(4)
print('-'*30)
my_function(11)

def loop_bad(x):
    for i in range(10):
        print(i, end=" ")
        if x == i:
            print()
            return


loop_bad(3)


def is_prime(n):
    """
    this function tests n for primality
    :param n: the number are checking
    :return: boolean, true or false if it is prime
    """
    if n < 2:
        return False

    for x in range(2, n):
        if n % x == 0:
            return False

    # if you survive this for loop it means that you are prime
    return True


for i in range(200):
    print(i, is_prime(i), end='\t')
    if i > 9 and i % 10 == 0:
        print()

"""
    Code tictctoe to learn functions
"""
print('\n\n\n')

EMPTY = ''
SPACE = ' '
TX = "X"
TO = "O"


def display_board(the_board):
    for i in range(len(the_board)):
        print(' | '.join(the_board[i]))
        if i < 2:
            print('-' * 9)


def place_mark(the_board, symbol):
    """
        ask the user for input 2 0 for instance
        we split it into parts (2 0 1) three parts
        they have to cast into integers (oops)
        what if it's off the board (ask again)
        what if it is filled?

    :param the_board:
    :param symbol:
    :return:
    """
    pos = [-1, -1] # [row, col]
    while not(0 <= pos[0] < 3 and 0 <= pos[1] < 3) or the_board[pos[0]][pos[1]] != SPACE:
        in_string = input('Tell me a place to put the mark (space separated, row col): ')
        split_list = in_string.split()
        if len(split_list) == 2:
            try:
                pos = [int(split_list[0]), int(split_list[1])]
            except ValueError:
                print('You tried to enter a non-integer. ')
                pos = [-1, -1]
        else:
            print('You must enter two numbers separated by a space. ')
    # relies on lists being mutable
    the_board[pos[0]][pos[1]] = symbol


def check_rows(the_board):
    """
        X X X
        O O O
    """
    for row in the_board:
        if row[0] == row[1] == row[2] != SPACE:
            return row[0]

    return EMPTY


def check_cols(the_board):
    """
        (0, 0) (0, 1) (0, 2)
        (1, 0) (1, 1) (1, 2)
        (2, 0) (2, 1) (2, 2)
    """
    for i in range(len(the_board)):
        if the_board[0][i] == the_board[1][i] == the_board[2][i] != SPACE:
            return the_board[0][i]

    return EMPTY


def check_diags(the_board):
    if the_board[0][0] == the_board[1][1] == the_board[2][2] != SPACE:
        return the_board[0][0]

    # if you use a loop, think the_board[i][len(the_board) - 1 - i]
    if the_board[2][0] == the_board[1][1] == the_board[0][2] != SPACE:
        return the_board[2][0]

    return EMPTY

def check_victory(the_board):
    """
        write 3 helper functions
        check_rows
        check_cols
        check_diags

        check filled
    """
    row_check = check_rows(the_board)
    col_check = check_cols(the_board)
    diag_check = check_diags(the_board)

    if row_check:
        return row_check
    if col_check:
        return col_check
    if diag_check:
        return diag_check

    filled = True
    for i in range(len(the_board)):
        for j in range(len(the_board[i])):
            if the_board[i][j] == SPACE:
                filled = False

    if filled:
        return 'T'  # T means tie

    return EMPTY


def play_game():
    # set up the board
    the_board = [[SPACE, SPACE, SPACE],  # the_board[0][0] = first element in this row
                 [SPACE, SPACE, SPACE],  # the_board[1][1] = middle element in the board
                 [SPACE, SPACE, SPACE]]  # the_board[2][0] = first element of this row, the_board[2][2] = the last element of this row
    # print(the_board)
    display_board(the_board)
    turn_count = 0
    while not check_victory(the_board):
        if turn_count % 2 == 0:
            place_mark(the_board, TX)
            # place an X on the board
        else:
            place_mark(the_board, TO)
            # place an O on the board
        turn_count += 1
        display_board(the_board)
    print(f'The winner was {check_victory(the_board)}')


if __name__ == '__main__':
    # play_game()
    pass


"""
    pass-by-value
        a copy is made of the variable that gets passed, in local scope if you change the local
        variable, then the global variable stays the same.  
        
    pass-by-reference
        the variable in local scope is a renamed version of the global variable, so if you change
        it, then the global variable is also changed.  
"""

def pass_int_function(x, y, z):
    x = 15 * y - z
    y = 7 * x + 4
    z = 3 * y - x + z
    print(x, y, z)


def pass_str_function(s1, s2):
    s1 = s1 + ' her fleece was white as snow'
    s2 = s2 + ' M&C was a great movie'
    print(s1, s2)


def pass_list_function(list1):
    list1.append('hi')
    list1.append('bye')
    print(list1)
    list1 = [1, 2, 3, 4, 5]
    print(list1)


x = 2
y = 3
z = 5
pass_int_function(x, y, z)
print(x, y, z)

str1 = 'Mary had a little lamb'
str2 = 'Choose the lesser of two weevils'
pass_str_function(str1, str2)
print(str1, str2)

my_list = ['ball', 'soccer', 'field', 'goal']
pass_list_function(my_list)
print(my_list)


"""

    Evidence says:
        ints, strings pass by value
        lists pass by reference
    
    immutable:
        int, bool, string, float, None,[you don't need to know: datetime]
    mutable:
        lists, dictionaries, classes, sets, ...

    immutable things pass by value
    mutable things pass by reference
    
    int something(int & this_ref, int other_thing);
"""

def random_stuff(x):
    return 2 * x + 1

x = 4
x = random_stuff(x)

# trick: if you want to modify say 3-4 integers

def other_random(list_of_ints):
    list_of_ints[0] = 2 * list_of_ints[0] + 5

change_list = [5]
other_random(change_list)
print(change_list)
