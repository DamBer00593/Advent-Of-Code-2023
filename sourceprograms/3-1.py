arraySplit = []
check = []
def checkForSpecial(indexi,indexy,length):
    checkArr = ["@","#","$","%","&","*","/","+","-","="]
    tempArr = []
    yaynah = False
    if(length == 3):
        tempArr = [arraySplit[indexi][indexy-3],arraySplit[indexi][indexy+1],arraySplit[indexi-1][indexy-3],arraySplit[indexi-1][indexy-2],arraySplit[indexi-1][indexy-1],arraySplit[indexi-1][indexy],arraySplit[indexi-1][indexy+1]]
        if(not len(arraySplit) == indexi+1):
            tempArr.extend([arraySplit[indexi+1][indexy-3],arraySplit[indexi+1][indexy-2],arraySplit[indexi+1][indexy-1],arraySplit[indexi+1][indexy],arraySplit[indexi+1][indexy+1]])
        for check in checkArr:
            temp = check in tempArr
            if(temp):
                yaynah = True
    elif(length == 2):

        tempArr = [arraySplit[indexi-1][indexy-2],arraySplit[indexi-1][indexy-1],arraySplit[indexi-1][indexy],
                   arraySplit[indexi-1][indexy+1],arraySplit[indexi][indexy-2],arraySplit[indexi][indexy+1]]
        if(not len(arraySplit) == indexi+1):
            tempArr.extend([arraySplit[indexi+1][indexy-2],arraySplit[indexi+1][indexy-1],arraySplit[indexi+1][indexy],arraySplit[indexi+1][indexy+1]])
     
        for check in checkArr:
            temp = check in tempArr
            if(temp):
                yaynah = True
    elif(length == 1):
        tempArr = [arraySplit[indexi-1][indexy-1],arraySplit[indexi-1][indexy],arraySplit[indexi-1][indexy+1],arraySplit[indexi][indexy-2],arraySplit[indexi][indexy+1]]
        if(not len(arraySplit) == indexi+1):
            tempArr.extend([arraySplit[indexi+1][indexy-1],arraySplit[indexi+1][indexy],arraySplit[indexi+1][indexy+1]])
     
        for check in checkArr:
            temp = check in tempArr
            if(temp):
                yaynah = True
    if(yaynah):
        return True
    else:         
        return False

fileContent = open("./sourcefiles/3-1.txt", "r")

total = 0
for lineContent in fileContent:
    splitLine = [*lineContent]
    arraySplit.append(splitLine)

conditioni = True
indexi = 0
while conditioni:
    conditiony = True
    indexy = 0
    while conditiony:
        test1 = ""
        test2 = ""
        if(len(arraySplit[indexi]) >= indexy+3):
            test1 = str(arraySplit[indexi][indexy]) + str(arraySplit[indexi][indexy+1]) + str(arraySplit[indexi][indexy+2])
        if(len(arraySplit[indexi]) >= indexy+2):
            test2 = str(arraySplit[indexi][indexy]) + str(arraySplit[indexi][indexy+1])
        if(len(arraySplit[indexi]) >= indexy+1):
            test3 = str(arraySplit[indexi][indexy])
        # [@#$%&*/+-=]
        if(test1.isnumeric()):
            indexy += 2
            
            if(checkForSpecial(indexi, indexy,3)):
                total += int(test1)
                check.append(int(test1))
        elif(test2.isnumeric()):
            indexy+= 1
            
            if(checkForSpecial(indexi, indexy,2)):
                total += int(test2)
                check.append(int(test2))
        elif(test3.isnumeric()):
            if(checkForSpecial(indexi, indexy,1)):
                total += int(test3)
                check.append(int(test3))
        indexy += 1
        conditiony = (not len(arraySplit[indexi]) == indexy)
    indexi += 1
    conditioni = (not len(arraySplit) == indexi)

print(total)

#555975 too low
#556057 was the answer
print(check)