fileContent = open("./sourcefiles/4-1.txt", "r")
total = 0

for lineContent in fileContent:
    #print(lineContent)
    firstSplit = lineContent.split(":")
    cardNum = firstSplit[0].split(" ")[1]
    print(cardNum)
    secondSplit = firstSplit[1].split("|")
    scratchedNumbers = secondSplit[0].strip().split(" ")
    winningNumbers = secondSplit[1].strip().split(" ")
    lineTotal = 0
    for cleaning in scratchedNumbers:
        if(cleaning == ""):
            scratchedNumbers.remove("")
    for cleaning in winningNumbers:
        if(cleaning == ""):
            winningNumbers.remove("")
        
    print(scratchedNumbers)
    print(winningNumbers)
    count = 0
    for scratched in scratchedNumbers:
        if(scratched in winningNumbers):
            count += 1
            if(lineTotal == 0):
                lineTotal += 1
            else:
                lineTotal *= 2
    total += lineTotal
    print(str(count) + "--- count --- ")
    print(str(lineTotal) + "--linetotal")
print(total)