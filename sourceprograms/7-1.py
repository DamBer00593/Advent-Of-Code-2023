fileContent = open("./sourceFiles/7-1.txt", "r")
bidsArray = []
cardsArray = []
for lineContent in fileContent:
    firstSplit = lineContent.strip().split(" ")

    bidsArray.append(firstSplit[1])
    cardsArray.append([*firstSplit[0]])

for cards in cardsArray:
    #print(cards)
    for i in range(len(cards)):
        print(cards[i])

print(bidsArray[0])
print(cardsArray[0])
