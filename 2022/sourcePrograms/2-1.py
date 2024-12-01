fileContent = open("./sourceFiles/2-1.txt", "r")
total = 0


##A is rock
##B is paper
##C is scissors 
##Z is scissors
##X is rock
##Y is paper


pointValue = {
    'X':1,
    'Y':2,
    'Z':3
}
handOrder = {
    'A': ['Y','X','Z'],
    'B': ['Z','Y','X'],
    'C': ['X','Z','Y']
}

print(handOrder['B'].index("X"))
for lineContent in fileContent:
    hands = lineContent.strip().split(" ")
    roundTotal = pointValue[hands[1]] + (6 if handOrder[hands[0]].index(hands[1]) == 0 else 3 if handOrder[hands[0]].index(hands[1]) == 1 else 0)
    print(hands[0] + " : " +  hands[1])
    print("Hand Order", handOrder[hands[0]])
    print("Round Identifier", handOrder[hands[0]].index(hands[1]))
    print("Round Total", roundTotal)
    total += roundTotal
    

print(total)