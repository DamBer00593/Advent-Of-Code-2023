fileContent = open("./sourcefiles/2-1.txt", "r")
total = 0
for lineContent in fileContent:
    print(lineContent)
    splitOne = lineContent.split(":")
    gameID = splitOne[0].split(" ")[1]
    #print(gameID)
    games = splitOne[1].split(";")
    totalColours = [-1,-1,-1]
    for game in games:
        turns = game.split(",")
        #print(turns)
        colours = [0,0,0] #R G B
        for turn in turns:
            colour = turn.split(" ")
            #print(colour)
            
            if("red" in colour[2]):
                #print("red" + str(colour[1]))
                colours[0] = colour[1]
            elif("green" in colour[2]):
                #print("green")
                colours[1] = colour[1]
            elif("blue" in colour[2]):
                #print("blue")
                colours[2] = colour[1]
        print(colours)
        if(int(totalColours[0]) == -1):
            if(colours[0] != 0):
                totalColours[0] = colours[0]
        if(int(totalColours[1]) == -1):
            if(colours[1] != 0):
                totalColours[1] = colours[1]
        if(int(totalColours[2]) == -1):
            if(colours[2] != 0):
                totalColours[2] = colours[2]
        if(int(colours[0]) >= int(totalColours[0])):
            if(colours[0] != 0):
                totalColours[0] = colours[0]
        if(int(colours[1]) >= int(totalColours[1])):
            if(colours[1] != 0):
                totalColours[1] = colours[1]
        if(int(colours[2]) >= int(totalColours[2])):
            if(colours[2] != 0):
                totalColours[2] = colours[2]
    print(totalColours)
    print(int(totalColours[0])*int(totalColours[1])*int(totalColours[2]))
    total += (int(totalColours[0])*int(totalColours[1])*int(totalColours[2]))
    
print(total)

#part 1 answer
# 2512   

#956 too low
#2005 too low
#part 2 Answer
#67335