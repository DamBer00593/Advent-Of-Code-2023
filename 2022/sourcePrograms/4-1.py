fileContent = open("./sourceFiles/4-1.txt", "r")

totalPairs = []
total = 0

for lineItem in fileContent:
    pairs = lineItem.strip().split(",")
    totalPairs.append([pairs[0].split("-"),pairs[1].split("-")])
# print(totalPairs)

for pair in totalPairs:
    pair1 = list(range(int(pair[0][0]),int(pair[0][1])+1))
    pair2 = list(range(int(pair[1][0]),int(pair[1][1])+1))
    total1 = True
    total2 = True
    
    for items in pair1:
        if items  in pair2:
            pass
            
        else:
            total1 = False



    for items in pair2:
        if items in pair1:
            pass
        else:
            total2 = False


    print(pair1)
    print(pair2)

    print(total1)
    print(total2)

    if total1 == True or total2 == True:
        total += 1

print(total)
#276 is too low
#388 is too low

#776 is too high
#759 is not the right answer
#575 is not the right answer
#546 is not the right answer
#359 is not the right answer

#507 is the right answer