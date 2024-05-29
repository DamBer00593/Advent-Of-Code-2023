fileContent = open("./sourceFiles/2-1.txt", "r")
feetSquared = 0
lengthForRibbon = 0
for content in fileContent:
    firstSplit = content.strip().split("x")
    firstSplit = list(map(int, firstSplit))
    lw = firstSplit[0]*firstSplit[1]
    wh = firstSplit[1]*firstSplit[2]
    hl = firstSplit[0]*firstSplit[2]
    l = [lw, wh, hl]
    minSide = min(l)
    min1, min2 = sorted([firstSplit[0], firstSplit[1], firstSplit[2]])[:2]
    areaOfRibbon = firstSplit[0]*firstSplit[1]*firstSplit[2]
    lengthOfRibbon = min1+min1+min2+min2
    areaofBox = 2*lw+2*wh+2*hl
    feetSquared += minSide + areaofBox
    lengthForRibbon += lengthOfRibbon + areaOfRibbon


print(feetSquared)
print(lengthForRibbon)

# 4448717 too high
# 3828105 too high
# 3812909 is the right answer
