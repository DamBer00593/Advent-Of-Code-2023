fileContent = open("./sourceFiles/25-1.txt", "r")

SNAFUVALUES = {
    "2":2,
    "1":1,
    "0":0,
    "-":-1,
    "=":-2
}


def SNAFUtoDECIMAL(SNAFUFORMAT):
    itt = 0
    total = 0
    for char in SNAFUFORMAT:
        total += SNAFUVALUES[char]*(5**itt)
        itt+=1
    return total

def DECIMALtoSNAFU(total):
    snafu = ""
    localTotal = total
    print(localTotal)
    for i in reversed(range(0,20)):
        print(i,":", localTotal)
        if localTotal > 0:
            print("positive", localTotal // 5**i, localTotal, 5**i, i)
            if localTotal // 5**i == 0:
                localTotal = localTotal - 5**i
                snafu += "1"
            if localTotal // 5**i == 2:
                localTotal = localTotal - 5**i
                snafu += "2"
        elif localTotal < 0:
            print("negitave", localTotal * -1 // 5**i, localTotal, 5**i*-1, i)
            if(localTotal * -1 // 5**i >= 2):
                localTotal = localTotal + 5**i*2
                snafu+="="
                print(i, "=")
            elif(localTotal * -1 // 5**i == 1):
                localTotal = localTotal + 5**i
                snafu+="-"
                print(i, "-")
            elif(localTotal * -1 // 5**i == 0):
                print((localTotal * -1 // 5**i) - 5**(i-1)*2)
                if (localTotal * -1 // 5**i) - 5**(i-1)*2 >= -2:
                    localTotal = localTotal + 5**i
                    snafu+="-"
                    print(i, "-")
                else:
                    snafu+="0"
                    print(i, "0")
            
        else:
            pass
    return reversed(snafu)




total = 0
for lineContent in fileContent:
    splitLine = [*lineContent.strip()]
    #print(splitLine)
    total += SNAFUtoDECIMAL(reversed(splitLine))

print(total)
SNAFURep = DECIMALtoSNAFU(total)
print(SNAFURep)
print(SNAFUtoDECIMAL(SNAFURep))
# 1747

# 1747 - 3125
# -1378 + 1250
# -128 + 125
# -3 + 0
# -3+5
# 2 - 2

# 1=-0-2