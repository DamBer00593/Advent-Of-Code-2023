import time
'''
def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'
  
starttime = time.time()
for i in range(0,10):
    y = i*i
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(i, basic_func(y)))
    
print('That took {} seconds'.format(time.time() - starttime))

'''


# ffs = [2797638787,1764015146,26675178]
# temp = []
# start = time.time()
# for i in range(ffs[2]):
#     temp.append([ffs[1]+i, ffs[0]+i])
# end = time.time()

# print("it took"+ str(start-end))
# start = time.time()
# for te in temp:
#     if(temp[0] == 1766679433):
#         print("test")
#         break

# end = time.time()

# print("it took"+ str(start-end))



# help = ["hello"]

# help.extend(["hi"])

# print(help)

import numpy as np

starttime = time.time()
newSeedsArray = []
indexi = 0
fileContent = open("./sourcefiles/5-1.txt", "r")
outfile = open("./destinationfiles/5-1.txt","w")
seedsArray = []
itterable = True
for lineContent in fileContent:
    if("seeds" in lineContent):
        seedsArray = lineContent.strip().split(" ")
        seedsArray.remove("seeds:")

while itterable:
    starttime = time.time()
    if(indexi >= len(seedsArray)-1):
        print("lastOne")
        itterable = False
        break
    if(itterable):
        #print(seedsArray[indexi])
        newSeedsArray.append(())
        if(seedsArray[indexi] < seedsArray[indexi+1]):
            newSeedsArray.append((np.arange(int(seedsArray[indexi]),int(seedsArray[indexi+1]))))
        else:
            for i in np.arange(0,int(seedsArray[indexi+1])):
                #print(i + int(seedsArray[indexi]))
                newSeedsArray.append(i + int(seedsArray[indexi]))
           # newSeedsArray.append((np.arange(int(seedsArray[indexi+1]),int(seedsArray[indexi]))))
    indexi += 2
    print('That took {} seconds'.format(time.time() - starttime))
newnewSeedsArray = []
print(newSeedsArray)

print('That took {} seconds'.format(time.time() - starttime))