import time
fileContent = open("./sourcefiles/5-1.txt", "r")

seedsArray = []
seedToSoil = False
seedToSoilArray = []
soilToFertilizer = False
soilToFertilizerArray = []
fertilizerToWater = False
fertilizerToWaterArray = []
waterToLight = False
waterToLightArray = []
lightToTemperature = False
lightToTemperatureArray = []
temperatureToHumidity = False
temperatureToHumidityArray = []
humidityToLocation = False
humidityToLocationArray = []
lowest = -1

starttime = time.time()
for lineContent in fileContent:
    if("seeds" in lineContent):
        seedsArray = lineContent.strip().split(" ")
        seedsArray.remove("seeds:")
    elif("seed-to-soil map" in lineContent or seedToSoil):
        seedToSoil = True
        if("seed-to-soil map" not in lineContent and "soil-to-fertilizer map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                seedToSoilArray.append(lineContent.strip().split(" "))
        if("soil-to-fertilizer map" in lineContent):
            seedToSoil = False
            soilToFertilizer = True
    elif(soilToFertilizer):
        if("soil-to-fertilizer map" not in lineContent and "fertilizer-to-water map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                soilToFertilizerArray.append(lineContent.strip().split(" "))
        if("fertilizer-to-water map" in lineContent):
            soilToFertilizer = False
            fertilizerToWater = True
    elif(fertilizerToWater):
        if("fertilizer-to-water map" not in lineContent and "water-to-light map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                fertilizerToWaterArray.append(lineContent.strip().split(" "))
        if("water-to-light map" in lineContent):
            fertilizerToWater = False
            waterToLight = True
    elif(waterToLight):
        if("water-to-light map" not in lineContent and "light-to-temperature map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                waterToLightArray.append(lineContent.strip().split(" "))
        if("light-to-temperature map" in lineContent):
            waterToLight = False
            lightToTemperature = True
    elif(lightToTemperature):
        if("light-to-temperature map" not in lineContent and "temperature-to-humidity map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                lightToTemperatureArray.append(lineContent.strip().split(" "))
        if("temperature-to-humidity map" in lineContent):
            lightToTemperature = False
            temperatureToHumidity = True
    elif(temperatureToHumidity):
        if("temperature-to-humidity map" not in lineContent and "humidity-to-location map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                temperatureToHumidityArray.append(lineContent.strip().split(" "))
        if("humidity-to-location map" in lineContent):
            temperatureToHumidity = False
            humidityToLocation = True
    elif(humidityToLocation):
        if("temperature-to-humidity map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                humidityToLocationArray.append(lineContent.strip().split(" "))

def functionThingy(array, source):
    destination = int(array[0]) + (int(source)-int(array[1]))
    return int(destination)
resultsArray = []
def seedIn(array):
    yap = True
    for results in resultsArray:
        if(array[0] == results[0]):
            yap = False
    return yap

def testSeed(seed):  
    global lowest  
    for soil in seedToSoilArray:
        seedSoil = True
        fertDestination = 0
        if(int(soil[1]) <= int(seed) and int(soil[1]+soil[2]) >= int(seed)):
            fertDestination = functionThingy(soil, seed)
            seedSoil = False
        else:
            if(seedToSoilArray[len(seedToSoilArray)-1] == soil and seedSoil):
                fertDestination = seed
                seedSoil = False
        if(seedSoil == False):
            for fertilizer in soilToFertilizerArray:
                soilFert = True
                watDestination = 0
                if(int(fertilizer[1]) <= int(fertDestination) and int(fertilizer[1])+int(fertilizer[2]) >= int(fertDestination)):
                    watDestination = functionThingy(fertilizer, fertDestination)
                    soilFert = False
                else:
                    if(soilToFertilizerArray[len(soilToFertilizerArray)-1] == fertilizer and soilFert):
                        watDestination = fertDestination
                        soilFert = False
                if(soilFert == False):
                    for water in fertilizerToWaterArray:
                        fertWat = True
                        if(int(water[1]) <= int(watDestination) and int(water[1])+int(water[2]) >= int(watDestination)):
                            lightDestination = functionThingy(water, watDestination)
                            fertWat = False
                        else:
                            if(fertilizerToWaterArray[len(fertilizerToWaterArray)-1] == water and fertWat):
                                lightDestination = watDestination
                                fertWat = False
                        if(fertWat == False):
                            for light in waterToLightArray:
                                watLight = True
                                if(int(light[1]) <= int(lightDestination) and int(light[1])+int(light[2]) >= int(lightDestination)):  
                                    tempDestination = functionThingy(light, lightDestination)
                                    watLight = False
                                else:
                                    if(waterToLightArray[len(waterToLightArray)-1] == light and watLight):
                                        tempDestination = lightDestination
                                        watLight = False
                                if(watLight == False):    
                                    for temperature in lightToTemperatureArray:
                                        lightTemp = True
                                        if(int(temperature[1]) <= int(tempDestination) and int(temperature[1])+int(temperature[2]) >= int(tempDestination)):
                                            humidDestination = functionThingy(temperature, tempDestination)
                                            lightTemp = False
                                        else:
                                            if(lightToTemperatureArray[len(lightToTemperatureArray)-1] == temperature and lightTemp):
                                                humidDestination = tempDestination
                                                lightTemp = False
                                        if(lightTemp == False):
                                            for humidity in temperatureToHumidityArray:
                                                tempHumid = True
                                                if(int(humidity[1]) <= int(humidDestination) and int(humidity[1])+int(humidity[2]) >= int(humidDestination)):
                                                    locationDestination = functionThingy(humidity, humidDestination)
                                                    tempHumid = False
                                                else:
                                                    if(temperatureToHumidityArray[len(temperatureToHumidityArray)-1] == humidity and tempHumid):
                                                        locationDestination = humidDestination
                                                        tempHumid = False
                                                if(tempHumid == False):
                                                    for location in humidityToLocationArray:
                                                        humidLoca = True
                                                        if(int(location[1]) <= int(locationDestination) and int(location[1])+int(location[2]) >= int(locationDestination)):
                                                            locationFinalDestination = functionThingy(location, locationDestination)  
                                                            humidLoca = False
                                                        else:
                                                            if(humidityToLocationArray[len(humidityToLocationArray)-1] == location and humidLoca):
                                                                locationFinalDestination = locationDestination
                                                                humidLoca = False
                                                        if(humidLoca == False):
                                                            if(seedIn([seed,locationFinalDestination])):
                                                                if(lowest == -1):
                                                                    lowest = [seed,locationFinalDestination]
                                                                    print(lowest)
                                                                else:
                                                                    if(int(lowest[1]) >= int(locationFinalDestination)):
                                                                        lowest = [seed,locationFinalDestination]
                                                                        print(lowest)   
                                                            resultsArray.append([seed,locationFinalDestination])                                                

for i,k in zip(seedsArray[0::2], seedsArray[1::2]):
    for itterator in range(int(k)):
        testSeed(int(i)+itterator)

    # testSeed(seed)
print(lowest)


print('That took {} seconds'.format(time.time() - starttime))
#3:18 is when i started the program

#try to cheat the loop with math
#if the seed is 768975 and the source range starts at 0
'''
the source is 768975 so the destination would be 
3378130613 + 768975
or destination = destinationStart + (sourceStart-seed)
3378899588 is the answer

'''