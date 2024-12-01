fileContent = open("./sourceFiles/6-1.txt", "r")
letters = [*fileContent.read().strip()]
checkedLetters = []
string = letters[0] +letters[1] + letters[2] + letters[3]
checkedLetters.append(string)
for i in range(4,len(letters)):
    string = string[1:]+letters[i]
    if len(list(set(string))) == 4:
        print(string)
        print(i+1)
        break

#1141 is too low
