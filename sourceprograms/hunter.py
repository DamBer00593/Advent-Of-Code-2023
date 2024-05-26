file = open("./sourcefiles/4-1.txt", "r")
cards = []

for line in file:
    cards.append(line.strip().split(":")[1].split("|"))
final = 0
active = list(range(len(cards)))
while len(active) > 0:
    cardNums = list(filter(None, cards[active[0]][0].split(" ")))
    cardWin = list(filter(None, cards[active[0]][1].split(" ")))
    points = 0
    for i in range(0, len(cardNums)):
        for j in range(0, len(cardWin)):
            if cardNums[i] == cardWin[j]:
                points += 1
    for i in range(1, points+1):
        active.append(active[0]+i)
    final += 1
    print(active)
    active.pop(0)

print(final)