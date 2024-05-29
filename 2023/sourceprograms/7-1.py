fileContent = open("./sourceFiles/7-1.txt", "r")
bidsArray = []
cardsArray = []
for lineContent in fileContent:
    firstSplit = lineContent.strip().split(" ")
    bidsArray.append(firstSplit[1])
    cardsArray.append([*firstSplit[0]])
allCardScores = []
fiveOfAKindHands = []
fiveOfAKindCards = []
fourOfAKindHands = []
fourOfAKindCards = []
FullHouseHands = []
FullHouseCards = []
threeOfAKindHands = []
threeOfAKindCards = []
twoOfAKindHands = []
twoOfAKindCards = []
leftOverHands = []
leftOverCards = []
for cards in cardsArray:
    cardLabel = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cardScore = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(cards)):
        cardScore[cardLabel.index(cards[i])]+=1
    allCardScores.append(cardScore)
        
itter = 0        
for scores in allCardScores:
    success = True
    for i in range(len(scores)):
        if(scores[i] == 5):
            fiveOfAKindHands.append(scores)
            fiveOfAKindCards.append(cardsArray[itter])
            success = False
        elif(scores[i] == 4):
            fourOfAKindHands.append(scores)
            fourOfAKindCards.append(cardsArray[itter])
            success = False
        elif(scores[i] == 3):   
            fullhou = False
            for i in range(len(scores)):
                if(scores[i] == 2):
                    FullHouseCards.append(cardsArray[itter])
                    FullHouseHands.append(scores)
                    success = False  
                    fullhou = True   
            if(fullhou == False):
                threeOfAKindHands.append(scores)
                threeOfAKindCards.append(cardsArray[itter])
                success = False        
        elif(scores[i]==2):
            fullhou = False
            for i in range(len(scores)):
                if(scores[i] == 3):
                    FullHouseCards.append(cardsArray[itter])
                    FullHouseHands.append(scores)
                    success = False  
                    fullhou = True       
            if(fullhou == False):
                twoOfAKindHands.append(scores)
                twoOfAKindCards.append(cardsArray[itter]) 
                success = False   
        else:
            amireal = True
            for i in range(len(scores)):
                if(scores[i] != 0 and scores[i] != 1):
                    amireal=False
                     
            if(amireal):
                leftOverHands.append(scores)
                leftOverCards.append(cardsArray[itter])
                success = False
        if(success == False):
            break
    itter+=1

# print(bidsArray)
# print(cardsArray)
print(len(allCardScores))

print(len(fiveOfAKindHands))
print(len(fourOfAKindHands))
print(len(threeOfAKindHands))
print(len(twoOfAKindHands))
print(len(FullHouseHands))
print(len(leftOverHands))

# print(fiveOfAKindCards)
# print(fourOfAKindCards)
# print(FullHouseCards)f
# print(threeOfAKindCards)
# print(twoOfAKindCards)
# print(leftOverHands)
