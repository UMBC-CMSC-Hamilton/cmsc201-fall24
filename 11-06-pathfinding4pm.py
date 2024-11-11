"""
Pathfinding on a grid...

1 | |u| | |*| |*| | |
2 |l|x|r| | | |*| | |
3 | |d| | |*| | |g| |

Let's imagine you have a grid of some kind, 2d grid
    you're allowed to move up down left right


Sometimes the answer is left, right, up, down
    What we're going to do is actually do all of those options
    See if one of them (or more) leads to the answer


1 | |u| | |*| |*| | |
2 |l|x|r| | | |*| | |
3 | |d| | |*| |*|*|*|
4 | | | | |*| |*|g| |

Sometimes there's no answer so we want to know that too.

x -> r -> x -> r -> x [problem] it will die after 1000 recursions
One idea [doesnt work]: keep track of the previous position

1 | | | | |*| |*| | |
2 | |x = next|x|x| | |*| | |
3 | |x = curr|*|x|*| |*|*|*|
4 | |x = prev|x|x|*| |*|g| |

 We have to track ALL of our previous visited positions.

 we're going to have a recursive function

    check to see we're at the goal:
        return True
    check to see if we've been here before:
        return False
    set the position we're currently at as visited

    try to go up  [recursive call]
    try to go right [recursive call]
    try to go down [recursive call]
    try to go left [recursive call]

    was there an answer? return True if there was, otherwise False
"""

# inside the random library [the first thing] there is a function also  called random
# you've used randint(a, b) integers in the interval [a, b]
from random import random
# this one gives us a value between 0 and 1, uniform distribution
EMPTY = ' '
WALL = '*'
GOAL = 'G'


def make_grid(rows, cols, p):
    """
    :param p: a number between 0 and 1 [float] determine the probability of a wall
    :return:
    """
    new_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            if random() <= p:
                new_row.append(WALL)
            else:
                new_row.append(EMPTY)
        new_grid.append(new_row)

    return new_grid

def display_grid(the_grid):
    rows = len(the_grid)
    cols = len(the_grid[0])

    # column indices first
    col_indices = list(range(cols))
    for i in range(len(col_indices)):
        col_indices[i] = str(col_indices[i])

    print('\t', '     '.join(col_indices))
    for i in range(len(the_grid)):
        print(i, '\t', end='')
        for x in the_grid[i]:
            print('|', str(x).rjust(4), end='')
        print()

"""
    check to see we're at the goal:
        return True
    check to see if we've been here before:
        return False
    set the position we're currently at as visited

    try to go up  [recursive call]
    try to go right [recursive call]
    try to go down [recursive call]
    try to go left [recursive call]
"""
def pathfinding(the_grid, posy, posx, visited):
    if the_grid[posy][posx] == GOAL:
        return True

    if [posy, posx] in visited:
        return False

    visited.append([posy, posx])

    go_up = go_right = go_down = go_left = False
    if posy > 0 and the_grid[posy - 1][posx] != WALL:
        go_up = pathfinding(the_grid, posy - 1, posx, visited)  # going up (decreasing y coord)
    if posx + 1 < len(the_grid[posy]) and the_grid[posy][posx + 1] != WALL:
        go_right = pathfinding(the_grid, posy, posx + 1, visited)  # going right
    if posy + 1 < len(the_grid) and the_grid[posy + 1][posx] != WALL:
        go_down = pathfinding(the_grid, posy + 1, posx, visited)  # going down
    if posx > 0 and the_grid[posy][posx - 1] != WALL:
        go_left = pathfinding(the_grid, posy, posx - 1, visited)  # going left

    return go_up or go_down or go_left or go_right



def pathfinding_with_steps(the_grid, posy, posx, visited, step):
    if the_grid[posy][posx] == GOAL:
        return True

    if [posy, posx] in visited:
        return False

    visited.append([posy, posx])

    go_up = go_right = go_down = go_left = False
    if posy > 0 and the_grid[posy - 1][posx] != WALL:
        go_up = pathfinding_with_steps(the_grid, posy - 1, posx, visited, step + 1)  # going up (decreasing y coord)
        if go_up:
            the_grid[posy][posx] = str(step)
    if posx + 1 < len(the_grid[posy]) and the_grid[posy][posx + 1] != WALL:
        go_right = pathfinding_with_steps(the_grid, posy, posx + 1, visited, step + 1)  # going right
        if go_right:
            the_grid[posy][posx] = str(step)

    if posy + 1 < len(the_grid) and the_grid[posy + 1][posx] != WALL:
        go_down = pathfinding_with_steps(the_grid, posy + 1, posx, visited, step  + 1)  # going down
        if go_down:
            the_grid[posy][posx] = str(step)
    if posx > 0 and the_grid[posy][posx - 1] != WALL:
        go_left = pathfinding_with_steps(the_grid, posy, posx - 1, visited, step + 1)  # going left
        if go_left:
            the_grid[posy][posx] = str(step)
    return go_up or go_down or go_left or go_right


while input('Again? ') == 'yes':
    my_grid = make_grid(10, 10, .24)
    display_grid(my_grid)
    goal_str = input('Enter a goal position: ')
    goal_pos = goal_str.split()
    goal_pos = [int(goal_pos[0]), int(goal_pos[1])]
    my_grid[goal_pos[0]][goal_pos[1]] = GOAL
    display_grid(my_grid)
    print(pathfinding_with_steps(my_grid, 0, 0, [], 0))
    display_grid(my_grid)





"""
x = 2
if x == 3:
    def increment(x):
        return x + 1
    
increment(5)
"""