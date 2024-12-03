import copy
fileContent = open("./sourceFiles/2-1.txt", "r")
total = 0

def isRight(testInput):
    index = 0
    lastItem = None
    greater = None
    wrong = False
    # print(testInput)
    for item in testInput:
        if lastItem == None:
            lastItem = int(item)
        else:
            if greater == None:
                if(int(item) > lastItem and abs(int(item)-lastItem) <= 3):
                    greater = True
                    lastItem = int(item)
                elif(int(item) < lastItem and abs(int(item)-lastItem) <= 3):
                    greater = False
                    lastItem = int(item)
                else:
                    return [False, index,item, testInput]
            elif greater == True:
                if(int(item) > lastItem and abs(int(item)-lastItem) <= 3):
                    lastItem = int(item)
                else:
                    return [False, index,item, testInput]
            else:
                if(int(item) < lastItem and abs(int(item)-lastItem) <= 3):
                    lastItem = int(item)
                    
                else:
                    return [False, index,item, testInput]
        index += 1
    return [True]
       

for lineContent in fileContent:
    testInput = lineContent.strip().split(" ")
    res = isRight(testInput)
    if res[0] == True:
        total+=1
    else:
        

        for i in range (0,res[1]+1):
            print(res, i)
            testInput2 = copy.copy(testInput)
            print(testInput2)
            del testInput2[i]
            res2 = isRight(testInput2)

            print(res2, "AFTER")
            if(res2[0] == True):
                total += 1
                break
print(total)

#320 is too low
#323 is too low

