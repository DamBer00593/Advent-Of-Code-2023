fileContent = open("./sourcefiles/3-1.txt", "r")
total = 0
indexy = 0
twodig = 0
threedig = 0
previousLine = None
for lineContent in fileContent:
    previousLine = lineContent
    splitLine = [*lineContent]
    indexi = 0
    looping = True
    while looping:
        #print(indexi)
        #print(len(lineContent))
        startingindex = -1
        #print(splitLine[indexi])
        if(splitLine[indexi].isnumeric()):
            if(splitLine[indexi].isnumeric() and splitLine[indexi+1].isnumeric() and splitLine[indexi+2].isnumeric()):
                #print("three digits")
                #print(str(splitLine[indexi]) + str(splitLine[indexi+1]) + str(splitLine[indexi+2]))
                threedig += 1
                indexi += 2
                
                #nextNumber = character
            elif(splitLine[indexi].isnumeric() and splitLine[indexi+1].isnumeric()):
                #print("two digits")
                indexi += 1
                twodig += 1
        if(indexi >= len(lineContent)-1):
            looping = False
            print("new line")
        indexi += 1
    indexy += 1
print(twodig)
print(threedig)