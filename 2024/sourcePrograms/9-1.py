fileContent = open("./sourceFiles/9-1.txt", "r")
puzzleInput = []
for lineContent in fileContent:
    puzzleInput = [*lineContent]
print(puzzleInput)
visualOutput = []
index = 0
index2 = 0
for puzz in puzzleInput:
    if(index%2 == 0):
        # print("usedSpace",int(puzz))
        for i in range(int(puzz)):
            visualOutput.append(index2)
        index2+=1
    else:
        # print("freeSpace",puzz)
        for i in range(int(puzz)):
            visualOutput.append(".")
    index += 1
    

print(visualOutput)
index = 0
try:
    for item in visualOutput:
        if item ==".":
            if(visualOutput[-1] != "."):
                visualOutput[index] = visualOutput[-1]
                del visualOutput[-1]
            else:
                while visualOutput[-1] == ".":
                    del visualOutput[-1]
                visualOutput[index] = visualOutput[-1]
                del visualOutput[-1]

        index +=1   
except:
    print(visualOutput)
index = 0
total = 0
for item in visualOutput:
    total += index * int(item)
    index +=1
print(total)

#is the right answser