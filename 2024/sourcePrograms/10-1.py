fileContent = open("./sourceFiles/10-1.txt", "r")
puzzleInput = []
for lineContent in fileContent:
    puzzleInput.append([*lineContent.strip()])

print(puzzleInput)
startingPoints = []
for i in range(len(puzzleInput)):
    for y in range(len(puzzleInput[i])):
        if (i == 0 or i == len(puzzleInput)-1) and puzzleInput[i][y] == "0":
            startingPoints.append([i,y])
        elif (y == 0 or y == len(puzzleInput[int(i)])-1) and puzzleInput[i][y] == "0":
            startingPoints.append([i,y])
print(startingPoints)
            

for points in startingPoints:
    print(puzzleInput[points[0]][points[1]])
    currentPosition = int(puzzleInput[points[0]][points[1]])
    while True:
        if(puzzleInput[points[0]-1][points[1]] == currentPosition+1 and points[0] > 0):
            print("up")
        elif(puzzleInput[points[0]+1][points[1]] == currentPosition+1 and points[0] < len(puzzleInput)-1):
            print("Down")
        elif(puzzleInput[points[0]][points[1]-1] == currentPosition+1 and points[1] > 0):
            print("Left")
        elif(puzzleInput[points[0]][points[1]+1] == currentPosition+1 and points[1] < len(puzzleInput)-1):
            print("Right")
        else:
            print("no paths")
            break