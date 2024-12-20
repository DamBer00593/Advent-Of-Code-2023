fileContent = open("./sourceFiles/16-1.txt", "r")
puzzleInput = []
startingPoint = []
index = 0
for lineContent in fileContent:
    puzzle = [*lineContent.strip()]
    puzzleInput.append(puzzle)
    if "S" in puzzle:
        startingPoint = [index,puzzle.index("S")]
    
    index+=1
print(puzzleInput)
print(startingPoint)
def checkCoords(coords,direction):
    return puzzleInput[coords[0]+direction[0]][coords[1]+direction[1]]

def checkPuzzle(startingStraights, startingTurns, startingCoords, lastDirection, lastCoord):
    print(startingStraights,startingTurns,startingCoords,lastDirection)
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for dir in directions:
        char = checkCoords(startingCoords,dir)
        print(char)
        if(char == "."):
            print(lastDirection, dir, startingCoords)
            if lastDirection == [0,0] or lastDirection == dir:
                startingStraights+=1
                startingCoords[0] += dir[0]
                startingCoords[1] += dir[1]
                checkPuzzle(startingStraights,startingTurns,startingCoords,dir)
            elif lastDirection != dir:
                print("?")
                startingTurns+=1
                startingCoords[0] += dir[0]
                startingCoords[1] += dir[1]
                checkPuzzle(startingStraights,startingTurns,startingCoords,dir)
        elif(char == "E"):
            print(startingStraights,startingTurns,startingCoords,lastDirection)

checkPuzzle(0,0,startingPoint,[0,0])
        