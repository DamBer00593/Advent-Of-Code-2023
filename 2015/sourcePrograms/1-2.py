fileContent = open("./sourceFiles/1-1.txt", "r")
for content in fileContent:
    letters = ([*content])
count = 0
itter = 0
for lett in letters:
    if (count == -1):
        print(itter)
    if (lett == "("):
        count += 1
    elif (lett == ")"):
        count -= 1
    itter += 1

print(count)
