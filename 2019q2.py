import sys
from queue import Queue

def addPos(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]

def getDir(dir, turn):

    if turn == "R":
        dir += 1
    elif turn == "L":
        dir += -1

    dir = dir % 4

    return dir

# def addTrail(pos):
#     global trail
#     trail.put(pos)
#     if len(trail.queue) > maxAge:
#         trail.get()

def addTrail(pos):
    global trail
    trail.append(pos)
    if len(trail) > maxAge:
        trail.pop(0)


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
pos = [0, 0]
moveNo = 0
dir = 0
# trail = Queue()
trail = []

# INPUTS
maxAge = int(sys.argv[1])
inputStr = sys.argv[2]
moves = int(sys.argv[3])


while moveNo < moves:
    addTrail(pos.copy())

    turn = inputStr[moveNo % len(inputStr)]
    dir = getDir(dir, turn)
    nextPos = addPos(pos, dirs[dir])

    i = 0
    while i < 4 and nextPos in list(trail.queue):
        dir = getDir(dir, "R")
        nextPos = addPos(pos, dirs[dir])
        i += 1

    if i == 4:
        break

    pos = nextPos
    moveNo += 1

print(pos)