fileContent = open("./sourceFiles/4-1.txt", "r")
wordGrid = []
for lineContent in fileContent:
    rowGrid = []
    for item in lineContent.strip():
        rowGrid.append(item.strip())
    wordGrid.append(rowGrid)
total = 0
instructions = [
[[0,0],[-1,1],[-2,2],[-3,3]],
[[0,0],[1,-1],[2,-2],[3,-3]],
[[0,0],[1,1],[2,2],[3,3]],
[[0,0],[-1,-1],[-2,-2],[-3,-3]],
[[0,0],[1,0],[2,0],[3,0]],
[[0,0],[-1,0],[-2,0],[-3,0]],
[[0,0],[0,1],[0,2],[0,3]],
[[0,0],[0,-1],[0,-2],[0,-3]]
]

for i in range(len(wordGrid)):
    for y in range(len(wordGrid[i])):
        if(wordGrid[i][y] == "X"):
            for dir in instructions:
                xmas = ""
                for pairs in dir:
                    # print(pairs)
                    # print(pairs[0]+i,pairs[1]+y)
                    # print(i,y,pairs[0],pairs[1])

                    # print(len(wordGrid),len(wordGrid[0]))
                    # print(pairs[0]+i >= 0 and pairs[0]+i < len(wordGrid))
                    # print(pairs[1]+y <= len(wordGrid[i])-1,pairs[1]+y , "<",len(wordGrid[i])-1 )
                    # print(pairs[1]+y >= 0)
                    if pairs[0]+i >= 0 and pairs[0]+i < len(wordGrid):
                        if(pairs[1]+y >= 0 and pairs[1]+y <= len(wordGrid[i])-1):
                            xmas += wordGrid[pairs[0]+i][pairs[1]+y]
                #             print(wordGrid[pairs[0]+i][pairs[1]+y])
                # print(xmas)
                if(xmas == "XMAS"):
                    total += 1

                
print(total)

#2549 was answer of part 1