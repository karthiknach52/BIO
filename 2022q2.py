from copy import deepcopy

# Directions are 0-5 instead of 1-6
# Cells are 0-24 instead of 1-25
# 1 is used to represent red colony
# -1 is used to represent blue colony

# INPUTS
r = 1
b = 14
s = 31
f = 19

# VARIABLES
hive = [[0 for x in range(6)] for y in range(25)]
red_drone = [0, 0]
blue_drone = [24, 5]

def print_hive():
    for i in range(len(hive)):
        print(i, hive[i])

def sum_hive(hive):
    red_cells = 0
    blue_cells = 0
    for cell in hive:
        if sum(cell) > 0:
            red_cells += 1
        elif sum(cell) < 0:
            blue_cells += 1
    return red_cells, blue_cells

def take_edge(input_hive, edge, colony):
    hive = deepcopy(input_hive)
    hive[edge[0]][edge[1]] = colony
    opposite_edge = get_opposite_edge(edge)
    if opposite_edge:
        hive[opposite_edge[0]][opposite_edge[1]] = colony
    return hive

def get_opposite_edge(edge):
    reverse_cell_odd = {0:-5, 1:1, 2:5, 3:4, 4:-1, 5:-6}
    reverse_cell_even = {0:-4, 1:1, 2:6, 3:5, 4:-1, 5:-5}
    reverse_direction = {0:3, 1:4, 2:5, 3:0, 4:1, 5:2}

    if (edge[0] // 5) % 2 == 0:
        opposite_cell = edge[0] + reverse_cell_odd[edge[1]]
    else:
        opposite_cell = edge[0] + reverse_cell_even[edge[1]]
    
    if (
        opposite_cell < 0 or
        opposite_cell > 24 or
        (edge[0] % 5 == 0 and edge[1] == 4) or
        (edge[0] % 5 == 4 and edge[1] == 1) or
        ((edge[0] // 5) % 2 == 0 and edge[0] % 5 == 0 and (edge[1] == 5 or edge[1] == 3)) or
        ((edge[0] // 5) % 2 != 0 and edge[0] % 5 == 4 and (edge[1] == 0 or edge[1] == 2))
    ):
        opposite_edge = None
    else:
        opposite_edge = [opposite_cell, reverse_direction[edge[1]]]

    return opposite_edge



for skirmish in range(s):
    hive = take_edge(hive, red_drone, 1)
    red_drone[0] = (red_drone[0] + r) % 25
    red_drone[1] = (red_drone[1] + 1) % 6

    hive = take_edge(hive, blue_drone, -1)
    blue_drone[0] = (blue_drone[0] + b) % 25
    blue_drone[1] = (blue_drone[1] - 1) % 6


for feud in range(f):

    ### RED ###
    moves = []
    highest_red, lowest_blue = sum_hive(hive)
    for i in range(25):
        for j in range(6):
            if hive[i][j] == 0:
                test_hive = take_edge(hive, [i,j], 1)
                red, blue = sum_hive(test_hive)
                if red > highest_red: highest_red = red
                moves.append([[i,j], red, blue])

    i = 0
    while i < len(moves):
        if moves[i][1] < highest_red:
            moves.pop(i)
        else:
            if moves[i][2] < lowest_blue:
                lowest_blue = moves[i][2]
            i += 1

    i = 0
    while i < len(moves):
        if moves[i][2] > lowest_blue:
            moves.pop(i)
        else:
            i += 1

    hive = take_edge(hive, moves[0][0], 1)

    ### BLUE ###
    moves = []
    lowest_red, highest_blue = sum_hive(hive)
    for i in range(25):
        for j in range(6):
            if hive[i][j] == 0:
                test_hive = take_edge(hive, [i,j], -1)
                red, blue = sum_hive(test_hive)
                if blue > highest_blue: highest_blue = blue
                moves.append([[i,j], red, blue])

    i = 0
    while i < len(moves):
        if moves[i][2] < highest_blue:
            moves.pop(i)
        else:
            if moves[i][1] < lowest_red:
                lowest_red = moves[i][1]
            i += 1

    i = 0
    while i < len(moves):
        if moves[i][1] > lowest_red:
            moves.pop(i)
        else:
            i += 1

    hive = take_edge(hive, moves[-1][0], -1)

print(sum_hive(hive))