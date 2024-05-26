fileContent = open("./sourcefiles/1-1.txt", "r")
total = 0
results = []
for lineContent in fileContent:
    splitLine = [*lineContent]
    print(splitLine)
    yes = True
    firstNumber = 0
    nextNumber = 0
    lastNumber = 0
    index = 0
    for character in splitLine:
        index += 1

        if (character.isnumeric()):
            nextNumber = character
        elif (character == "o" or character == "O"):  # one
            if (len(splitLine) >= index+2):
                if (splitLine[index] == "n" and splitLine[index+1] == "e"):
                    print("one")
                    nextNumber = 1
        elif (character == "t" or character == "T"):  # two three
            if (len(splitLine) >= index+2):
                if (splitLine[index] == "w" and splitLine[index+1] == "o"):
                    print("two")
                    nextNumber = 2
            if (len(splitLine) >= index+4):
                if (splitLine[index] == "h" and splitLine[index+1] == "r" and splitLine[index+2] == "e" and splitLine[index+3] == "e"):
                    print("three")
                    nextNumber = 3
        elif (character == "f" or character == "F"):  # four five
            if (len(splitLine) >= index+3):
                if (splitLine[index] == "o" and splitLine[index+1] == "u" and splitLine[index+2] == "r"):
                    print("four")
                    nextNumber = 4
            if (len(splitLine) >= index+3):
                if (splitLine[index] == "i" and splitLine[index+1] == "v" and splitLine[index+2] == "e"):
                    print("five")
                    nextNumber = 5
        elif (character == "s" or character == "S"):  # six seven
            if (len(splitLine) >= index+2):
                if (splitLine[index] == "i" and splitLine[index+1] == "x"):
                    print("six")
                    nextNumber = 6
            if (len(splitLine) >= index+4):
                if (splitLine[index] == "e" and splitLine[index+1] == "v" and splitLine[index+2] == "e" and splitLine[index+3] == "n"):
                    print("seven")
                    nextNumber = 7
        elif (character == "e" or character == "E"):  # eight
            if (len(splitLine) >= index+4):
                if (splitLine[index] == "i" and splitLine[index+1] == "g" and splitLine[index+2] == "h" and splitLine[index+3] == "t"):
                    print("eight")
                    nextNumber = 8
        elif (character == "n" or character == "N"):  # nine
            if (len(splitLine) >= index+3):
                if (splitLine[index] == "i" and splitLine[index+1] == "n" and splitLine[index+2] == "e"):
                    print("nine")
                    nextNumber = 9
        if (firstNumber == 0):
            firstNumber = nextNumber

    if (character == splitLine[len(splitLine)-1]):
        lastNumber = nextNumber
    print(str(firstNumber) + str(lastNumber))
    total += int(str(firstNumber) + str(lastNumber))
    results.append(int(str(firstNumber) + str(lastNumber)))
print(total)
# part 1 answer
# 55172

# 36595 too low

# part 2 answer
# 54925
