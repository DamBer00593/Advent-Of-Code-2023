fileContent = open("./sourceFiles/3-1.txt", "r")
import re
inputString = ""
for lineContent in fileContent:
    inputString += lineContent.strip()

total = 0
x = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)",inputString)
for i in x:
    i = i.replace("mul(","")
    i = i.replace(")","")
    splitString = i.split(",")
    total += int(splitString[0]) * int(splitString[1])
print(total)