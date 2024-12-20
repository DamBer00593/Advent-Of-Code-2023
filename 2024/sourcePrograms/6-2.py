fileContent = open("./sourceFiles/6-1.txt", "r")
stops = []
mapLayout = []
index = 0
startingPoint = []
for lineContent in fileContent:
    layer = [*lineContent.strip()]
    mapLayout.append(layer)
    if('^' in layer):
        print(layer)
        startingPoint = [index,layer.index('^')]
    index += 1


# print(mapLayout)
print(startingPoint)
stops.append([startingPoint[0],startingPoint[1]])
print()

dir = "up"
try:
    while True:
        # print(startingPoint)
        if(startingPoint[0]>0):
            if(dir == "up"):
                # print(startingPoint[0])
                if(mapLayout[startingPoint[0]-1][startingPoint[1]] in ['.','^']):
                    # print(mapLayout[startingPoint[0]-1][startingPoint[1]], "UP", startingPoint)
                    startingPoint[0] -= 1
                    if(startingPoint in stops):
                        # print(startingPoint)
                        pass
                    else:
                        stops.append([startingPoint[0],startingPoint[1]])
                        print(mapLayout[startingPoint[0]][startingPoint[1]],"UP", startingPoint)
                else:
                    dir = "right"
                    # print(mapLayout[startingPoint[0]-1][startingPoint[1]])
            elif(dir == "right"):
                if(mapLayout[startingPoint[0]][startingPoint[1]+1] in ['.','^']):
                    # print(mapLayout[startingPoint[0]][startingPoint[1]+1], "RIGHT")
                    startingPoint[1] += 1
                    if(startingPoint in stops):
                        # print(startingPoint)
                        pass
                    else:
                        stops.append([startingPoint[0],startingPoint[1]])
                        print(mapLayout[startingPoint[0]][startingPoint[1]],"RIGHT", startingPoint)
                else:
                    dir = "down"
                    # print(mapLayout[startingPoint[0]][startingPoint[1]+1])
            elif(dir == "down"):
                if(mapLayout[startingPoint[0]+1][startingPoint[1]] in ['.','^']):
                    # print(mapLayout[startingPoint[0]+1][startingPoint[1]],"DOWN")
                    startingPoint[0] += 1
                    if(startingPoint in stops):
                        # print(startingPoint)
                        pass
                    else:
                        stops.append([startingPoint[0],startingPoint[1]])
                        print(mapLayout[startingPoint[0]][startingPoint[1]],"DOWN", startingPoint, len(stops))
                else:
                    dir = "left"
                    # print(mapLayout[startingPoint[0]+1][startingPoint[1]])
            elif(dir == "left"):
                if(mapLayout[startingPoint[0]][startingPoint[1]-1] in ['.','^']):
                    # print(mapLayout[startingPoint[0]][startingPoint[1]-1],"LEFT")
                    startingPoint[1] -= 1
                    if(startingPoint in stops):
                        # print(startingPoint)
                        pass
                    else:
                        stops.append([startingPoint[0],startingPoint[1]])
                        print(mapLayout[startingPoint[0]][startingPoint[1]],"LEFT", startingPoint)
                else:
                    dir = "up"
                    # print(mapLayout[startingPoint[0]][startingPoint[1]-1])
        else:
            break
except Exception as e: print(e)

print(len(stops))

#4606 is too high
#4559 is the answer