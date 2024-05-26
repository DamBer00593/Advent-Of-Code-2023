checkArr = ["*"]
arraySplit = []
total = 0
fileContent = open("./sourcefiles/3-1.txt", "r")
for lineContent in fileContent:
    splitLine = [*lineContent]
    arraySplit.append(splitLine)
    


def checkForNum(indexi,indexy):
    checkedLeft = []
    checkedRight = []
    results = []
    tempArr = [[indexi-1,indexy-1],[indexi-1,indexy],[indexi-1,indexy+1],[indexi, indexy-1],[indexi, indexy+1],[indexi+1, indexy-1], [indexi+1, indexy],[indexi+1, indexy+1]]
    for x,y in tempArr:
        if(arraySplit[x][y].isnumeric()):
            checkVal = True
            left = True
            stopit = False  
            looped = 0
            left = True
            stopit = False
            farthestBack = 0
            stringthing = ""
            tryThisY = 0
            while checkVal:
                if(left):
                    if(arraySplit[x][y-looped].isnumeric()):# and [x,y-looped] not in checkedLeft
                        farthestBack = (arraySplit[x][y-looped])
                        checkedLeft.append([x, y-looped])
                    else:
                        tryThisY = y-looped+1
                        if([x,y-looped] not in checkedLeft):
                            stringthing += str(farthestBack)
                        looped = 0
                        left = False
                else:
                    if(arraySplit[x][tryThisY+looped].isnumeric()):
                        checkedRight.append([x, tryThisY+looped])
                        stringthing += str(arraySplit[x][tryThisY+looped])
                    else:
                        stopit = True
                
                if(stopit):
                    if(stringthing == ""):
                        print("nothing to see here")
                    else:
                        results.append(int(stringthing))
                    break
                        
                looped += 1
    return results
                



conditioni = True
indexi = 0
while conditioni:
    conditiony = True
    indexy = 0
    while conditiony:
        exists = arraySplit[indexi][indexy] in checkArr
        if(exists):
            results = checkForNum(indexi,indexy)
            print(results)
            if(len(results) == 2):
                total = results[0]*results[1]
        indexy += 1
        conditiony = (not len(arraySplit[indexi]) == indexy)
    indexi += 1
    conditioni = (not len(arraySplit) == indexi)

# 55588192 is too
# 82454502 is too low

print(total)