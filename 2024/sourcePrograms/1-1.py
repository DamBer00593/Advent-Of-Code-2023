fileContent = open("./sourceFiles/1-1.txt", "r")
leftList = []
rightList = []
for lineContent in fileContent:
    stuff = lineContent.strip().split("   ")
    leftList.append(stuff[0])
    rightList.append(stuff[1])

sortedLeftList = sorted(leftList)
sortedRightList = sorted(rightList)
total = 0
for i in range(len(sortedLeftList)):
    print(sortedRightList[i] , " : ", sortedLeftList[i], int(sortedRightList[i])-int(sortedLeftList[i]))
    total += abs(int(sortedRightList[i])-int(sortedLeftList[i]))
    
print(total)

#630426 is not right

#1341714 is part 1 answer
