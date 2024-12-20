fileContent = open("./sourceFiles/4-1.txt", "r")
wordGrid = []
for lineContent in fileContent:
    rowGrid = []
    for item in lineContent.strip():
        rowGrid.append(item.strip())
    wordGrid.append(rowGrid)
total = 0
instructions = [
[[-1,1],[0,0],[1,-1]],
[[-1,-1],[0,0],[1,1]]
]
globalXmasList = []
for i in range(len(wordGrid)):
    for y in range(len(wordGrid[i])):
        if(wordGrid[i][y] == "A"):
            xmasList = []
            xmas = ""
            for dir in instructions:
                xmas = ""
                for pairs in dir:
                    # print(pairs)
                    # print(pairs[0]+i,pairs[1]+y)
                    
                    # print(len(wordGrid),len(wordGrid[0]))
                    # print(pairs[0]+i >= 0 and pairs[0]+i < len(wordGrid))
                    # print(pairs[1]+y <= len(wordGrid[i])-1,pairs[1]+y , "<",len(wordGrid[i])-1 )
                    # print(pairs[1]+y >= 0)
                    if pairs[0]+i >= 0 and pairs[0]+i < len(wordGrid):
                        if(pairs[1]+y >= 0 and pairs[1]+y <= len(wordGrid[i])-1):
                            print(i,y,pairs[0],pairs[1], wordGrid[pairs[0]+i][pairs[1]+y])
                            xmas += wordGrid[pairs[0]+i][pairs[1]+y]
                #             print()
                print(xmas)
                xmasList.append(xmas)
            subTot = 0
            # print(xmasList)
            for lis in xmasList:
                if(lis in ["SAM","MAS"]):
                    subTot += 1
                    
            if subTot == 2:
                total += 1
                print(xmasList)
            globalXmasList.append(xmasList)

                
print(total)
# print(globalXmasList)
#2549 was answer of part 1
#2003 is answer of part 2