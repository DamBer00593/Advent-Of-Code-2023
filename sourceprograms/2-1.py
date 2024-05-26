fileContent = open("./sourcefiles/2-1.txt", "r")
total = 0
for lineContent in fileContent:
    print(lineContent)
    splitOne = lineContent.split(":")
    gameID = splitOne[0].split(" ")[1]
    #print(gameID)
    games = splitOne[1].split(";")
    possible = True
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
        if(int(colours[0]) <= 12 and int(colours[1]) <= 13 and int(colours[2]) <= 14):
            possible = True
            print("possible")
        else:
            possible = False
            print("impossible")
            break
    if(possible):
        total += int(gameID)
print(total)

#part 1 answer
# 2512   
