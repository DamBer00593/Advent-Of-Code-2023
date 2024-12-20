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
    

# print(visualOutput)
index = 0
num = 0
size = 0
lastNum = 0
moved = []
try:
    for item in reversed(visualOutput):
        # print(size,num,item)
        if item != ".":
            if(num == 0):
                num = int(item)
                size = 1
            elif num == int(item):
                size += 1
            else:
                if num not in moved:
                    count = 0
                    indexy = 0
                    fitting = False
                    while True:
                        for forwardLoop in visualOutput:
                            if(forwardLoop == "."):
                                count += 1
                                if(count == size):
                                    # print(count)
                                    if(indexy > abs(i-len(visualOutput)+1)):
                                        # print("i fit but im too far")
                                        # print(index)
                                        # print(indexy)
                                        pass
                                    else:
                                        # print([num,size])
                                        fitting = True
                                        # print("i fit")
                                        moved.append(num)
                                        for i in range(indexy-size, indexy):
                                            # print(i+1)
                                            visualOutput[i+1] = num
                                        # print(visualOutput,"hello?")
                                    break
                            else:
                                count = 0
                            indexy +=1
                        break
                    if(fitting == True):
                        # print("hi")
                        # for i in range(index-size, index):
                        #     visualOutput[abs(i-len(visualOutput)+1)] = "."
                        #     print(abs(i-len(visualOutput)+1))
                        # print(visualOutput,"AFTER")
                        count2 = 0
                        index3 = 0
                        for item2 in visualOutput:
                            if(item2 == num):
                                if(count2<size):
                                    # print(item2)
                                    pass
                                else:
                                    # print(item2,"extra")
                                    visualOutput[index3] = "."
                                count2+=1
                            index3+=1
                                
                if(num != "."):
                    lastNum = int(num)
                    num = int(item)
                    size = 1
                    
        index +=1   
except:
    print(visualOutput)
print(visualOutput)
index = 0
total = 0
for item in visualOutput:
    if item != ".":
        total += index * int(item)
    index +=1
print(total)



#6389449758509 is too high