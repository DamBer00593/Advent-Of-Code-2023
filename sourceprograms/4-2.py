fileContent = open("./sourcefiles/4-1.txt", "r")
total = 0
resnum = []
fileArray = []
for lineContent in fileContent:
    firstSplit = lineContent.split(":")
    cardNum = firstSplit[0].split(" ")
    cardNum = list(filter(None, cardNum))[1]
    resnum.insert(int(cardNum), 0)
    fileArray.append(lineContent)
for lineContent in fileArray:
    firstSplit = lineContent.split(":")
    cardNum = firstSplit[0].split(" ")
    cardNum = list(filter(None, cardNum))[1]
    secondSplit = firstSplit[1].split("|")
    scratchedNumbers = secondSplit[0].strip().split(" ")
    scratchedNumbers = list(filter(None, scratchedNumbers))
    winningNumbers = secondSplit[1].strip().split(" ")
    winningNumbers = list(filter(None, winningNumbers))
    lineTotal = 0
    count = 0
    for scratched in scratchedNumbers:
        if(scratched in winningNumbers):
            count += 1
            if(lineTotal == 0):
                lineTotal += 1
            else:
                lineTotal *= 2
    total += lineTotal
    first = False
    nummie = 0
    for teehee in range(int(cardNum), count+int(cardNum)+1):
        print(resnum)

        if(first):
            resnum[teehee-1]+= (resnum[int(cardNum)-1])
        else:
            resnum[teehee-1]+=1
            first = True
print(resnum)
sen = 0
for res in resnum:
    sen += res
print(sen)
