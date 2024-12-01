fileContent = open("./sourceFiles/4-1.txt", "r")

totalPairs = []
total = 0

for lineItem in fileContent:
    pairs = lineItem.strip().split(",")
    totalPairs.append([pairs[0].split("-"),pairs[1].split("-")])
# print(totalPairs)

for pair in totalPairs:
    if(pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
        total += 1
        print(pair, "0")
    elif(pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
        total += 1
        print(pair, "1")

print(total)


#276 is too low
#388 is too low

#776 is too high
#759 is not the right answer
#575 is not the right answer
#546 is not the right answer