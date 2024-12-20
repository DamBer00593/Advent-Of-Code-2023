fileContent = open("./sourceFiles/15-1.txt", "r")
mapArray = []
puzzleInput = []
top = True
index = 0
startingPoint = []

def getThingAtPoint(startingPoint):
    return mapArray[int(startingPoint[0])][int(startingPoint[1])]
def printMapOut(mapArray):
    for i in mapArray:
        print(i)
for lineContent in fileContent:
    if(top==True and lineContent != "\n"):
        # print(lineContent,"one")
        layer = [*lineContent.strip()]
        mapArray.append(layer)
        if("@" in layer):
            startingPoint = [index,layer.index("@")]
            # print(startingPoint)
    elif(top==False):
        # print(lineContent,"two")
        puzzleInput += [*lineContent.strip()]
    else:
        # print("I switched")
        top = False
    index += 1
# print(mapArray)
# print(puzzleInput)

# print(getThingAtPoint(startingPoint))
for puzzle in puzzleInput:
    # print(startingPoint)

    if puzzle == "<":
        if(startingPoint[1]-1 >= 0):
            testCoords = [startingPoint[0],startingPoint[1]-1]
            testPos = getThingAtPoint(testCoords)
            if(testPos == "#"):
                pass
            elif(testPos == "." or testPos == "@"):
                startingPoint[1] -= 1
            elif(testPos == "O"):
                print("<",testCoords,testPos,"START")
                printMapOut(mapArray)
                
                
                # print(testCoords[1])
                blocks = []
                print(0,testCoords[1]+1)
                for i in reversed(range(0,testCoords[1]+1)):
                    print(i)
                    checkCase = [testCoords[0],i]
                    checkBlock = getThingAtPoint(checkCase)
                    print(checkBlock,checkCase,"HI")
                    if(checkBlock == "O"):
                        blocks.append(checkCase)
                    elif(checkBlock == "."):
                        startingPoint[1] -= 1
                        break
                    elif(checkBlock == "#"):
                        blocks = []
                        break
                for block in reversed(blocks):
                    mapArray[block[0]][block[1]] = "."
                    mapArray[block[0]][block[1]-1] = "O"
                
                print(blocks)
                printMapOut(mapArray)  
                print("END")  
    elif puzzle == "^":
        if(startingPoint[0]-1 >= 0):
            testCoords = [startingPoint[0]-1,startingPoint[1]]
            testPos = getThingAtPoint(testCoords)
            if(testPos == "#"):
                pass
            elif(testPos == "." or testPos == "@"):
                startingPoint[0] -= 1
            elif(testPos == "O"):
                print("^",testCoords,testPos,"START")
                printMapOut(mapArray)
                
                
                blocks = []
                for i in reversed(range(0,testCoords[0]+1)):
                    print(i)
                    checkCase = [i,testCoords[1]]
                    checkBlock = getThingAtPoint(checkCase)
                    print(checkCase,checkBlock)
                    if(checkBlock == "O"):
                        blocks.append(checkCase)
                    elif(checkBlock == "."):
                        startingPoint[1] += 1
                        break
                    elif(checkBlock == "#"):
                        blocks = []
                        break
                for block in reversed(blocks):
                    mapArray[block[0]][block[1]] = "."
                    mapArray[block[0]-1][block[1]] = "O"
                
                print(blocks)
                printMapOut(mapArray)  
                print("END")  
                
        pass
    elif puzzle == ">":
        if(startingPoint[1]+1 < len(mapArray[0])):
            testCoords = [startingPoint[0],startingPoint[1]+1]
            testPos = getThingAtPoint(testCoords)
            if(testPos == "#"):
                pass
            elif(testPos == "." or testPos == "@"):
                startingPoint[1] += 1
            elif(testPos == "O"):
                print(">",testCoords,testPos,"START")
                printMapOut(mapArray)
                
                blocks = []
                for i in range(testCoords[1],len(mapArray[0])):
                    checkCase = [testCoords[0],i]
                    checkBlock = getThingAtPoint(checkCase)
                    if(checkBlock == "O"):
                        blocks.append(checkCase)
                    elif(checkBlock == "."):
                        startingPoint[1] += 1
                        break
                    elif(checkBlock == "#"):
                        blocks = []
                        break
                for block in reversed(blocks):
                    mapArray[block[0]][block[1]] = "."
                    mapArray[block[0]][block[1]+1] = "O"
                
                print(blocks)
                printMapOut(mapArray)  
                print("END")  
                
        pass
    elif puzzle == "v":
        
        if(startingPoint[0]+1 < len(mapArray)):
            # print(startingPoint[1],"STFF")
            # print(len(mapArray))
            testCoords = [startingPoint[0]+1,startingPoint[1]]
            testPos = getThingAtPoint(testCoords)
            if(testPos == "#"):
                pass
            elif(testPos == "." or testPos == "@"):
                startingPoint[0] += 1
            elif(testPos == "O"):
                print("v",testCoords,testPos,"START")
                printMapOut(mapArray)
                
                blocks = []
                for i in range(testCoords[0],len(mapArray[0])):
                    checkCase = [i,testCoords[1]]
                    checkBlock = getThingAtPoint(checkCase)
                    if(checkBlock == "O"):
                        blocks.append(checkCase)
                    elif(checkBlock == "."):
                        startingPoint[0] += 1
                        break
                    elif(checkBlock == "#"):
                        blocks = []
                        break
                for block in reversed(blocks):
                    mapArray[block[0]][block[1]] = "."
                    mapArray[block[0]+1][block[1]] = "O"
                print(blocks)
                printMapOut(mapArray)  
                print("END")  