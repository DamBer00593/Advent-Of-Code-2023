fileContent = open("./sourcefiles/6-1.txt", "r")
timeArray = []
distanceArray = []
for lineContent in fileContent:
    splitFirst = lineContent.strip().split(":")
    if(splitFirst[0] == "Time"):
        timeArray = lineContent.strip().split(":")[1].split(" ")
        timeArray = list(filter(None, timeArray))
    elif(splitFirst[0] == "Distance"):
        distanceArray = lineContent.strip().split(":")[1].split(" ")
        distanceArray = list(filter(None, distanceArray))
print(timeArray)
print(distanceArray)


index = 0
count = []
for time in timeArray:
    localcount = 0
    for i in range(0,int(time)):
        distance = i*(int(time)-i)
        
        if(int(distanceArray[index]) < distance):
            print(distance)
            localcount += 1
    index+=1
    count.append(localcount)
total = 1
print(count)
for coun in count:

    total *= int(coun)

print(total)

#3370125 too high

#220320 was the answer had the < flipped