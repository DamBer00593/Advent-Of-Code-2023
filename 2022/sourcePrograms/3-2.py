fileContent = open("./sourceFiles/3-1.txt", "r")
totalCompartmentValues = []
total = 0

for lineContent in fileContent:
    compartmentValues = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for item in [*lineContent.strip()]:
        asciiVal = ord(item)
        if asciiVal >= 65 and asciiVal <= 90:
            compartmentValues[asciiVal-39] += 1
        elif asciiVal >= 97 and asciiVal <= 122:
            compartmentValues[asciiVal-97] += 1  
    totalCompartmentValues.append(compartmentValues)

for i in range (0,len(totalCompartmentValues),3):
    for y in range (52):
        if totalCompartmentValues[i][y] >= 1 and totalCompartmentValues[i+1][y] >= 1 and totalCompartmentValues[i+2][y] >= 1:
            total += y+1

print(total)

# 290668 is too high
# 7051 is too low



#2683 is the answer to part 2