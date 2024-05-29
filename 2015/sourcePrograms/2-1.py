fileContent = open("./sourceFiles/2-1.txt", "r")
feetSquared = 0
for content in fileContent:
    firstSplit = content.strip().split("x")
    firstSplit = list(map(int, firstSplit))
    lw = firstSplit[0]*firstSplit[1]
    wh = firstSplit[1]*firstSplit[2]
    hl = firstSplit[0]*firstSplit[2]
    minside = min(lw, wh, hl)
    areaofBox = 2*lw+2*wh+2*hl
    feetSquared += minside + areaofBox

print(feetSquared)
