fileContent = open("./sourceFiles/5-1.txt", "r")
index = 0
rules = []
testInputs = []
for lineContent in fileContent:
    if(index <= 21):
        rules.append(lineContent.strip().split("|"))
    elif index >= 23:
        testInputs.append(lineContent.strip().split(","))
    index += 1

def checkIfMatchRules(item):
    item
    matches = True
    for rule in rules:
        try:
            if item.index(rule[0]) > item.index(rule[1]):
                matches = False
        except:
            pass
    if matches:
        print("HI")
        print(item[len(item)//2])
        return [True,int(item[len(item)//2])]
    return [False,0]

def correctErrors(item):
    # print(item)
    for rule in rules:
        try:
            if item.index(rule[0]) < item.index(rule[1]):
                temp = int(item[item.index(rule[1])])
                item.insert(item.index(rule[0]),temp)
                del item[item.index(rule[1])] 
        except:
            pass
    if(checkIfMatchRules(item)[0]):
        return [True,int(item[len(item)//2])]
    else:
        print(item)
        correctErrors(item)
    return [False,0]



total = 0
total2 = 0
# print(rules)
# print(testInputs)
for item in testInputs:
    res = checkIfMatchRules(item)
    if(res[0]):
        total += res[1]
    else:
        # print(item)
        res2 = correctErrors(item)
        total2 += int(res2[1])
        for rule in rules:
            print(item)
            try:
                if item.index(rule[0]) < item.index(rule[1]):
                    temp = int(item[item.index(rule[1])])
                    item.insert(item.index(rule[0]),temp)
                    del item[item.index(rule[1])+1] 
            except:
                pass
print(total)