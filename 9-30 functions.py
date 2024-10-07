"""
First exam next week:
    Wednesday
    Review monday - previous exam that I will send out
    Put together 8-10 sample problems [very hopefully]
"""

"""
    if __name__ == '__main__':
"""

print('hi')  # this runs even though its not in a function called main
print(__name__)
import main_script

# this function here is not considered any different by python than any other function name
def main():
    print('I am the main function i will be called because that\'s what main functions do')
    # oh right that's not true


if __name__ == '__main__':
    print('i am in main')
    # put your code in here
    # concept: there is no main function in python
    #  you know this actually: just have code out in the aether
    # python runs everything outside of this if statement
    # runs everything inside the if statement if this is the actual script that the user
    #       executed, or that we ran python 9-30\ functions.py
    #       ban def main()


"""
    Let's talk about functions:
    
    functions are a way to modularize code 
        a function should have "one job"
        in python they should be focused on that ask, 10-100 
    helper function also has one job, which is to do a part of the job of the big function
    
    tic tac toe
    
    goal = play the game
    
    play_game = play the game
        take_turn = players take turns
        place_mark = detects if its filled
        check_victory = check rows, cols, diags
            check_row
            check_col
            check_diag
"""

def count_as(my_string):
    """
        In mathematics, you have y = f(x) think of y as the output and x as input
        Use parameters, f(x, y, z, w, k) in order to run f you need to input all of these variables
        :param my_string: short for parameter, thats the data that we need to run the function
        :return: output of the function
    """
    count = 0
    for i in range(len(my_string)):
        if my_string[i].lower() == 'a':
            count += 1

    return count


test_string = input('Give me a string: ')
first_count = count_as(test_string)  # outside of the function (global scope) the variable is called test_string
other_string = input('Do it again: ')
second_count = count_as(other_string)

# return is not print
print(first_count, second_count)


def is_prime(n):
    """
        when you have a function that has an "is" or "has" the response (the return type) should be
            a boolean meaning True or False
    :param n: the number we check for primality
    :return: True/False depending on if it is prime
    """
    if n < 2:
        return False

    for x in range(2, n):
        if n % x == 0:
            # if you put a return inside of a loop, the function ends as soon as it hits this
            return False
            # no code after this will execute
    # if you survive the for loop that means the if statement never executed, so it is prime
    return True


for i in range(200):
    print(i, is_prime(i), end='\t')
    if i % 10 == 0:
        print()

print('\n\n')

"""
Lets write it up
"""

EMPTY = ''
SPACE = ' '
TIC_TAC_X = 'X'
TIC_TAC_O = 'O'


def display_board(the_board):
    for i in range(len(the_board)):
        print(' | '.join(the_board[i]))
        if i < 2:
            print('-' * 9)


def check_rows(the_board):
    """
        [ (0,0), (0, 1), (0, 2) ]
        [ (1,0), (1, 1), (1, 2) ]
        [ (2,0), (2, 1), (2, 2) ]

         X X X or O O O

    :param the_board:
    :return:
    """
    for row in the_board:
        row_mark = row[0]
        b_victory = True
        for i in range(len(row)):
            if row[i] != row_mark:
                b_victory = False
        if b_victory and row[0] != SPACE:
            return row_mark

    return EMPTY


def check_cols(the_board):
    """
        [ (0,0), (0, 1), (0, 2) ]
        [ (1,0), (1, 1), (1, 2) ]
        [ (2,0), (2, 1), (2, 2) ]
            (i, 3 - 1 - i), len(the_board) - 1 - i
         X 0
         X 0
         X 0

    :param the_board:
    :return:
    """
    for i in range(3):
        b_victory = True
        for j in range(3):
            if the_board[j][i] != the_board[0][i]:
                b_victory = False
                #  why cant we just return False? we're only checking one column at a time,
                #  its possible that the first one isn't a victory but the second is
        if b_victory and the_board[0][i] != SPACE:
            return the_board[0][i]

    return EMPTY


def check_diags(the_board):
    """

    :param the_board:
    :return:
    """
    diag_victory = True
    for i in range(len(the_board)):
        if the_board[i][i] != the_board[0][0]:
            diag_victory = False
    if diag_victory and the_board[0][0] != SPACE:
        return the_board[0][0]

    anti_diag_victory = False
    if the_board[2][0] == the_board[1][1] == the_board[0][2]:
        anti_diag_victory = True

    if anti_diag_victory and the_board[2][0] != SPACE:
        return the_board[2][0]

    return EMPTY


def victory(the_board):
    """
        check the rows
        check the columns
        check diag/anti-diag
        [check for a filled board]
    :param the_board:
    :return: either 'X', 'O', 'T' or empty string '' or False
    """
    row_victory = check_rows(the_board)
    if row_victory:
        print('row victory')
        return row_victory

    col_victory = check_cols(the_board)
    if col_victory:
        print('col victory')
        return col_victory

    diag_victory = check_diags(the_board)
    if diag_victory:
        print('diag victory')
        return diag_victory

    # not so hard to check if the board is filled
    filled = True
    for i in range(len(the_board)):
        for j in range(len(the_board[i])):
            if the_board[i][j] == SPACE:
                filled = False

    if filled:
        return 'T'

    return EMPTY


def place_mark(the_board, symbol):
    """
        is the position entered 2 numbers? does it split into two parts
        is the position on the board? 1 <= sp[0] <= 3
        is the position filled already?
            the_board[sp[0]][sp[1]] == SPACE, if not then try again
    :param the_board:
    :param symbol:
    :return:
    """
    pos = [-1, -1]
    # short circuiting = if the first or is true it doesnt check the second one
    while not(0 <= pos[0] < 3 and 0 <= pos[1] < 3) or the_board[pos[0]][pos[1]] != SPACE:
        string_pos = input('Tell me the position to play on the board (eg 2 1): ')
        split_pos = string_pos.split()
        if len(split_pos) == 2:
            pos = [int(split_pos[0]), int(split_pos[1])]
        else:
            print('That is not two numbers separated by spaces. ')

    the_board[pos[0]][pos[1]] = symbol
    return pos


def play_game():
    # build the board
    the_board = [[SPACE, SPACE, SPACE],  # the_board[0], the_board[0][1] = the middle one
                 [SPACE, SPACE, SPACE],  # the_board[1], the_board[1][0] = the first in this row
                 [SPACE, SPACE, SPACE]   # the_board[2], the_board[2][2] = the last in this row
                 ]
    display_board(the_board)
    turn_count = 0
    # keep the game going until someone wins
    while not victory(the_board):

        if turn_count % 2 == 0:
            place_mark(the_board, TIC_TAC_X)
        else:
            place_mark(the_board, TIC_TAC_O)
        display_board(the_board)

        turn_count += 1


if __name__ == '__main__':
    # play_game()
    pass


"""
What do we take from this?
    a space is true, not empty
    
    functions need parameters which are the data that they need to run
        return should be whatever the function needs to tell the outside world
        
    functions do essentially one job functions are between 10 - 30 lines, not a rule
        but a guideline
    
    if a function gets too complex, think about breaking it up with helpers
    helper function is a function that does a bit of the job of the big function
        break down the functionality of a complex thing and allow you to focus on one task
        or one sub-task
    
"""

"""
Let's talk about parameters:
    theres two different ways parameters can be passed: pass-by-value and pass-by-reference
    
    pass-by-value parameter [argument] = the parameter is actually a copy of the value of the 
        global/other local variable, if you change it in the function, it does not change the 
        global variable
        
    pass-by-reference parameter [argument] = the parameter is actually a renaming of the original
        variable and you can modify it inside the function
    
    immutable in python:
        int bool string float passed by value
        datetime, NoneType (None)
    mutables or anything else:
        lists, dictionaries, classes, etc pass by reference
"""


def pass_int_example(x, y, z):
    x = 3 * x + y
    z = 2 * x + 4 * z
    y = x - y
    print(x, y, z)



def pass_str_example(s, t):
    s = s + 'happy'
    t = t + 'robots'
    print(s, t)


def pass_list_example(my_list):
    my_list.append('something')
    print(my_list)

def pass_dict_example(my_dict):
    my_dict['c'] = 17
    print(my_dict)

x = 4
y = 5
z = 3
pass_int_example(x, y, z)
print(x, y, z)

s = 'foremost'
t = 'visceral'
pass_str_example(s, t)
print(s, t)


the_list = ['another', 'apart', 'apt']
pass_list_example(the_list)
print(the_list)

my_example = {'a': 3, 'b': 7}
print(my_example['a'])

pass_dict_example(my_example)
print(my_example)


"""
    Local Scope vs Global Scope:
    
    When you enter a function a new scope is created
        variables that are declared inside of that scope only exist there
        when you leave that scope those variables [names/values] are lost
        the only way to save a local variable's value is to return it
        
    Local Scope (each function has its own)
        Lifetime: length of time that the function runs
        Accessibility: these variables are not accessible from outside of the function

    Global Scope:
        Lifetime: the runtime of the program
        Accessibility: everywhere including inside of functions
"""


def bad_function(a, b):
    global x  #  we have banned this keyword, if you need it, pass it
    print(a + x + b)

"""
    why are break and continue banned at least in 201?
        break  = will exit whatever loop you're in
        continue = bypasses the rest of the loop code and starts the next iteration
"""
x = 5
while x > 0:
    if x == 20:
        break

    x += 1

"""
  234 56
hello he
01234


(l + k) % len(temp_string)
"""