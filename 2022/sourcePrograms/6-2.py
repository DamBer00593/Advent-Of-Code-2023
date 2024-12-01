fileContent = open("./sourceFiles/6-1.txt", "r")
letters = [*fileContent.read().strip()]
checkedLetters = []
string = letters[0] +letters[1] + letters[2] + letters[3] + letters[4] +letters[5] + letters[6] + letters[7] + letters[8] +letters[9] + letters[10] + letters[11] + letters[12] +letters[13]
checkedLetters.append(string)
for i in range(14,len(letters)):
    string = string[1:]+letters[i]
    if len(list(set(string))) == 14:
        print(string)
        print(i+1)
        break

#1141 is too low
