fileContent = open("./sourceFiles/2-1.txt", "r")
testInput = []
total = 0
for lineContent in fileContent:
    testInput = lineContent.strip().split(" ")
    lastItem = None
    greater = None
    wrong = False
    # print(testInput)
    for item in testInput:
        if lastItem == None:
            lastItem = int(item)
        else:
            if greater == None:
                if(int(item) > lastItem and abs(int(item)-lastItem) <= 3):
                    greater = True
                    
                    # print("Greater", item,abs(int(item)-lastItem))
                    lastItem = int(item)
                elif(int(item) < lastItem and abs(int(item)-lastItem) <= 3):
                    greater = False
                    # print("Lesser", item,abs(int(item)-lastItem))
                    lastItem = int(item)
                else:
                    wrong = True
            elif greater == True:
                if(int(item) > lastItem and abs(int(item)-lastItem) <= 3):
                    # print("right", item,abs(int(item)-lastItem))
                    lastItem = int(item)
                else:
                    # print("wrong", item, abs(int(item)-lastItem))
                    wrong = True
                    lastItem = int(item)
            else:
                if(int(item) < lastItem and abs(int(item)-lastItem) <= 3):
                #    print("right", item,abs(int(item)-lastItem))
                    lastItem = int(item)
                    
                else:
                    wrong = True
                    # print("wrong",item,abs(int(item)-lastItem))
                    lastItem = int(item)
    if wrong == False:
        total += 1
        # print(testInput,"+1")
    else:
        # print(testInput, "WRONG")
        pass
print(total)


#504 is not the right answer
#534 is someone elses answer
#580 is wrong

# ['57', '57', '54', '53', '50', '47', '46', '43'] +1

#279 is right