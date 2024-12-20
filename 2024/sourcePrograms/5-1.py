fileContent = open("./sourceFiles/5-1.txt", "r")
index = 0
rules = []
testInputs = []
for lineContent in fileContent:
    if(index <= 1175):
        rules.append(lineContent.strip().split("|"))
    elif index >= 1177:
        testInputs.append(lineContent.strip().split(","))
    index += 1



total = 0
print(rules)
print(testInputs)
for item in testInputs:
    matches = True
    for rule in rules:
        try:
            if item.index(rule[0]) > item.index(rule[1]):
                matches = False
        except:
            pass
    if matches:
        print("HI")
        total += int(item[len(item)//2])
print(total)