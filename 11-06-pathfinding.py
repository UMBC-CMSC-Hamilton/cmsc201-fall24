"""

    Project 3: who knows
        Answer: use DFS = Depth First Search
        What is that?
            Its a way to recursively search a 'map' or a grid or some kind of network


    | |u| | | | |
    -------------
    |l|x|r|B| | |
    -------------
    | |d| |B| |g|
    -------------
    g = goal
    x = where you are
    B = blocked


    Idea: we dont know which is the right move
        Make every move go up down left and right from wherever we are

        It's going to be recursive

        We want to be able to mark a place as visited if it has been visited, we dont go back.
            Avoids infinite loops / recursions.
            We cant just remember the last / previous node we visited because of the more
                complex loops that we can accidently get into.

    | | |x|x|x| |
    -------------
    | | |x|B|x|g|
    -------------
    | | |x|x|x| |
    -------------

    each recursive function will make 4 recursive calls, go up, down, left and right
    check if its the goal, and we check if its visited => base cases

"""

import random

WALL = '*'
EMPTY = ' '
GOLD = 'G'


def make_grid(rows, cols, p):
    the_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            #  library.function it generates a random float between 0 and 1 [uniformly]
            if random.random() <= p:
                new_row.append(WALL)
            else:
                new_row.append(EMPTY)
        the_grid.append(new_row)
    return the_grid


def display_grid(the_grid):
    rows = len(the_grid)
    cols = len(the_grid[0])

    col_indices = list(range(cols))
    for i in range(len(col_indices)):
        col_indices[i] = str(col_indices[i])

    print('\t', '   '.join(col_indices))
    for i in range(rows):
        print(i, '\t', '|  '.join(the_grid[i]))



def pathfinding(the_grid, posy, posx, visited):
    # print([posy, posx])
    if the_grid[posy][posx] == GOLD:
        return True # we found it

    # we will not move onto walls so dont worry [worry a little]
    if [posy, posx] in visited:
        return False  # we've been here before, dont go into a big loop

    visited.append([posy, posx])

    go_up = go_right = go_down = go_left = False
    if posy > 0 and the_grid[posy - 1][posx] != WALL:
        go_up = pathfinding(the_grid, posy - 1, posx, visited)  # go up
        if go_up:
            the_grid[posy][posx] = 'v'
            print(posy, posx)
    # if the first statement is false, it never checks the second one, saves you from the IndexError
    if posx + 1 < len(the_grid[posy]) and the_grid[posy][posx + 1] != WALL:
        go_right = pathfinding(the_grid, posy, posx + 1, visited)  # right
        if go_right:
            the_grid[posy][posx] = 'v'
            print(posy, posx)
    if posy + 1 < len(the_grid) and the_grid[posy + 1][posx] != WALL:
        go_down = pathfinding(the_grid, posy + 1, posx, visited)  # down
        if go_down:
            the_grid[posy][posx] = 'v'
            print(posy, posx)
    if posx > 0 and the_grid[posy][posx - 1] != WALL:
        go_left = pathfinding(the_grid, posy, posx - 1, visited)  # left
        if go_left:
            the_grid[posy][posx] = 'v'
            print(posy, posx)
    return go_up or go_right or go_left or go_down


def pathfinding_with_step(the_grid, posy, posx, visited, step):
    if the_grid[posy][posx] == GOLD:
        return True # we found it

    # we will not move onto walls so dont worry [worry a little]
    if [posy, posx] in visited:
        return False  # we've been here before, dont go into a big loop

    visited.append([posy, posx])

    go_up = go_right = go_down = go_left = False
    if posy > 0 and the_grid[posy - 1][posx] != WALL:
        go_up = pathfinding_with_step(the_grid, posy - 1, posx, visited, step + 1)  # go up
        if go_up:
            the_grid[posy][posx] = str(step)
            print(posy, posx)
    # if the first statement is false, it never checks the second one, saves you from the IndexError
    if posx + 1 < len(the_grid[posy]) and the_grid[posy][posx + 1] != WALL:
        go_right = pathfinding_with_step(the_grid, posy, posx + 1, visited, step + 1)  # right
        if go_right:
            the_grid[posy][posx] = str(step)
            print(posy, posx)
    if posy + 1 < len(the_grid) and the_grid[posy + 1][posx] != WALL:
        go_down = pathfinding_with_step(the_grid, posy + 1, posx, visited, step + 1)  # down
        if go_down:
            the_grid[posy][posx] = str(step)
            print(posy, posx)
    if posx > 0 and the_grid[posy][posx - 1] != WALL:
        go_left = pathfinding_with_step(the_grid, posy, posx - 1, visited, step + 1)  # left
        if go_left:
            the_grid[posy][posx] = str(step)
            print(posy, posx)
    return go_up or go_right or go_left or go_down


while input('Again? ') == 'y':
    grid = make_grid(10, 10, 0.25)
    display_grid(grid)
    goal_pos = input('Where should we put the goal? ')
    position = goal_pos.split()
    grid[int(position[0])][int(position[1])] = GOLD
    display_grid(grid)
    print(pathfinding_with_step(grid, 0, 0, [], 1))
    display_grid(grid)


"""
    breadTH first search
"""