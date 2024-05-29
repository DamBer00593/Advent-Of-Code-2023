fileContent = open("./sourceFiles/3-1.txt", "r")
for content in fileContent:
    directions = ([*content])
    print(directions)
