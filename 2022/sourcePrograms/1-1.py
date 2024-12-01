fileContent = open("./sourceFiles/1-1.txt", "r")
calList = []
total = 0
for lineContent in fileContent:
    if lineContent.strip() == "":
        calList.append(total)
        total = 0
    else:
        total += int(lineContent.strip())
print(max(calList))