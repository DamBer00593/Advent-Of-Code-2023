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
    count = 0
    for items in sortedRightList:
        if sortedLeftList[i] == items:
            count+=1
    
    total += count * int(sortedLeftList[i])

    
print(total)


#27384707 is part two answer