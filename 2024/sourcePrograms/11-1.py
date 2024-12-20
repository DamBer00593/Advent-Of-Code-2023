import time

start = time.time()

fileContent = open("./sourceFiles/11-1.txt", "r")
puzzleInput = []
nextPuzzleInput = []
def checkIfIn(item,count=1,list=puzzleInput):
    for i in list:
        if(i[0] == item):
           checkIfIn2(item,count)
    checkIfIn2(item,count)
def checkIfIn2(item,count=1,list2=nextPuzzleInput):
    for i in nextPuzzleInput:
        if(i[0] == item):
            i[1] += count
            return
    nextPuzzleInput.append([item,count])

for lineContent in fileContent:
    for item in (lineContent.split(" ")): 
        checkIfIn(item)

print(nextPuzzleInput,"START")
for i in range(75):
    puzzleInput = nextPuzzleInput[:]
    nextPuzzleInput = []
    for input in puzzleInput:
        if(input[0] == "0"):
            count = input[1]
            checkIfIn("1",count)
        elif(len(input[0])%2==0):
            count = input[1]
            firstVar = input[0][:int(len(input[0])/2)]
            var = str(int(input[0][int(len(input[0])/2):]))
            checkIfIn(firstVar,count)
            checkIfIn(var,count)
        else:
            count = input[1]
            checkIfIn(str(int(input[0])*2024),count)
total = 0
for i in nextPuzzleInput:
    total += i[1]

print(total)

# DO SOMETHING

# CALC & PRINT RUNTIME
end = time.time()

print(end - start)