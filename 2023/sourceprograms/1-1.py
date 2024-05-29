fileContent = open("./sourcefiles/1-1.txt", "r")
something = fileContent.read()
total = 0
for lineContent in fileContent:
    splitLine = [*lineContent]
    print(splitLine)
    firstNumber = 0
    nextNumber = 0
    lastNumber = 0
    for character in splitLine:

        if (character.isnumeric()):
            if (nextNumber == 0):
                firstNumber = character
                print("firstNumber" + str(firstNumber))
            nextNumber = character
        if (character == splitLine[len(splitLine)-1]):
            lastNumber = nextNumber
    print(str(firstNumber) + str(lastNumber))
    total += int(str(firstNumber) + str(lastNumber))
print(total)
# part 1 answer
# 55172
