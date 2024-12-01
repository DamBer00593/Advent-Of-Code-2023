fileContent = open("./sourceFiles/3-1.txt", "r")
total = 0
f = open("./programOutputs/3-1.txt", "a")
# a = 97
# z = 122   
# A = 65
# Z = 90

for lineContent in fileContent:
    lineItem = [*lineContent.strip()]
    firstCompartment = lineItem[0:int(len(lineItem)/2)]
    secondCompartment = lineItem[int(len(lineItem)/2):]
    compartmentValues = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for item in firstCompartment:
        asciiVal = ord(item)
        if asciiVal >= 65 and asciiVal <= 90:
            compartmentValues[0][asciiVal-39] += 1
        elif asciiVal >= 97 and asciiVal <= 122:
            compartmentValues[0][asciiVal-97] += 1
    for item in secondCompartment:
        asciiVal = ord(item)
        if asciiVal >= 65 and asciiVal <= 90:
            compartmentValues[1][asciiVal-39] += 1
        elif asciiVal >= 97 and asciiVal <= 122:
            compartmentValues[1][asciiVal-97] += 1
    for i in range (52):
        if compartmentValues[0][i] >= 1 and compartmentValues[1][i] >= 1:
            total += i+1
print(total)
f.close()
# 290668 is too high
# 7051 is too low
