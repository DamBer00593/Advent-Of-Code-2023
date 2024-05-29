fileContent = open("./sourceFiles/1-1.txt", "r")
for content in fileContent:
    letters = ([*content])
count = 0

for lett in letters:
    if (lett == "("):
        count += 1
    elif (lett == ")"):
        count -= 1

print(count)
