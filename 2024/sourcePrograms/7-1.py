fileContent = open("./sourceFiles/7-1.txt", "r")
puzzleInput = []
for lineContent in fileContent:
    firstSplit = lineContent.strip().split(": ")
    puzzleInput.append([firstSplit[0],firstSplit[1].split(" ")])

for puzzle in puzzleInput:
    inputString = str(puzzle[1][0])
    for variable in ["*","+"]:
        for input in puzzle[1][1:]:
            inputString += variable + str(input)
    print(inputString)