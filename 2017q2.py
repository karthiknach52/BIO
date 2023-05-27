def printGrid(grid):
    for row in grid:
        for element in row:
            print(element, end = ' ')
        print()

def validEdge(edge):
    if (edge % 12 == 1) or (edge % 2 == 0 and (edge < 8 or edge > 66)):
        return False
    return True

def playEdge(edges, curPlayer, pos):
    edge = 0
    allDiffs = {1: [-6, 1, +6, -1], 2: [-6, -1, 6, 1]}
    diffs = allDiffs[curPlayer]

    for diff in diffs:
        testEdge = pos + (pos + diff)
        if testEdge not in edges and validEdge(testEdge):
            edge = testEdge
            return edge, pos

    # if no edges found, go to next dot and try again
    pos += 1
    if pos > 36:
        pos += -36
    return playEdge(edges, curPlayer, pos)

def checkBox(edges, playedEdge, toCheck):
    allDiffs = {"L":[5, -2, -7], "R":[-5, 2, 7], "U":[-7, -5, -12], "D":[7, 5, 12]}
    diffs = allDiffs[toCheck]

    for diff in diffs:
        if playedEdge + diff not in edges:
            return False
    return True

def updateGrid(topEdge, grid, curPlayer):
    y = int(topEdge // 12)
    x = int((topEdge - ((12 * y) + 3)) / 2)
    marking = {1:"X", 2:"O"}
    grid[y][x] = marking[curPlayer]
    score[curPlayer-1] += 1

def main(positions, modifiers, turns):
    grid = [["*" for x in range(5)] for y in range(5)] 
    edges = set()
    curPlayer = 1

    while turns > 0:
        
        pos = positions[curPlayer - 1]
        mod = modifiers[curPlayer - 1]

        pos += mod
        if pos > 36:
            pos += -36

        edgePlayed, pos = playEdge(edges, curPlayer, pos)
        edges.add(edgePlayed)

        positions[curPlayer - 1] = pos


        # Check if box has been made, if so player gets next turn
        samePlayer = False
        if edgePlayed % 2 == 0:
            if checkBox(edges, edgePlayed, "L"):
                updateGrid(edgePlayed-7, grid, curPlayer)
                samePlayer=True
            if checkBox(edges, edgePlayed, "R"):
                updateGrid(edgePlayed-5, grid, curPlayer)
                samePlayer=True
        else:
            if checkBox(edges, edgePlayed, "U"):
                updateGrid(edgePlayed-12, grid, curPlayer)
                samePlayer=True
            if checkBox(edges, edgePlayed, "D"):
                updateGrid(edgePlayed, grid, curPlayer)
                samePlayer=True

        if not samePlayer:
            invertPlayer = {1:2, 2:1}
            curPlayer = invertPlayer[curPlayer]

        turns -= 1

    printGrid(grid)
    print()
    print(score[0], score[1])


input = input("Enter 5 numbers with spaces: \n")
print()
input = input.split()

pos = [int(input[0]), int(input[2])]
mod = [int(input[1]), int(input[3])]
turns = int(input[4])
score = [0, 0]

main(pos, mod, turns)