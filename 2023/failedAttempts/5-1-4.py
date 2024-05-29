import time
fileContent = open("./sourcefiles/5-1.txt", "r")
outfile = open("./destinationfiles/5-1.txt","w")
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

resultsArray = []
lowest = -1
for lineContent in fileContent:
    if("seeds" in lineContent):
        seedsArray = lineContent.strip().split(" ")
        seedsArray.remove("seeds:")
    elif("seed-to-soil map" in lineContent or seedToSoil):
        seedToSoil = True
        #print("seedToSoil")
        if("seed-to-soil map" not in lineContent and "soil-to-fertilizer map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                seedToSoilArray.append(lineContent.strip().split(" "))
        if("soil-to-fertilizer map" in lineContent):
            seedToSoil = False
            soilToFertilizer = True
    elif(soilToFertilizer):
        #print("soilToFertilizer")
        if("soil-to-fertilizer map" not in lineContent and "fertilizer-to-water map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                soilToFertilizerArray.append(lineContent.strip().split(" "))
        if("fertilizer-to-water map" in lineContent):
            soilToFertilizer = False
            fertilizerToWater = True
    elif(fertilizerToWater):
        #print("fertilizerToWater")
        if("fertilizer-to-water map" not in lineContent and "water-to-light map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                fertilizerToWaterArray.append(lineContent.strip().split(" "))
        if("water-to-light map" in lineContent):
            fertilizerToWater = False
            waterToLight = True
    elif(waterToLight):
        #print("waterToLight")
        if("water-to-light map" not in lineContent and "light-to-temperature map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                waterToLightArray.append(lineContent.strip().split(" "))
        if("light-to-temperature map" in lineContent):
            waterToLight = False
            lightToTemperature = True
    elif(lightToTemperature):
        #print("lightToTemperature")
        if("light-to-temperature map" not in lineContent and "temperature-to-humidity map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                lightToTemperatureArray.append(lineContent.strip().split(" "))
        if("temperature-to-humidity map" in lineContent):
            lightToTemperature = False
            temperatureToHumidity = True
    elif(temperatureToHumidity):
        #print("temperatureToHumidity")
        if("temperature-to-humidity map" not in lineContent and "humidity-to-location map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                temperatureToHumidityArray.append(lineContent.strip().split(" "))
        if("humidity-to-location map" in lineContent):
            temperatureToHumidity = False
            humidityToLocation = True
    elif(humidityToLocation):
        #print("humidityToLocation")
        if("temperature-to-humidity map" not in lineContent):
            appendable = lineContent.strip().split(" ")
            if(appendable[0] != ""):
                humidityToLocationArray.append(lineContent.strip().split(" "))

def functionThingy(array, source):
    destination = int(array[0]) + (int(source)-int(array[1]))

    #print(str(source) + " -> " + str(destination) + "\n")
    return int(destination)
def seedIn(array):
    yap = True
    for results in resultsArray:
        # print(array[0])
        # print(resultsArray)print(array[0])
        # print(resultsArray)
        if(array[0] == results[0]):
            yap = False
    return yap
for seed in seedsArray:
    outfile.write("NEW SEED: \n")
    outfile.write(str(seed) + " SEED IS\n")
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
            outfile.write("soil")
            outfile.write(str(seed) + " -> " + str(fertDestination)  + "\n")
            #print(str(seed) + " -> " + str(fertDestination)  + "\n")
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
                    outfile.write("fert")
                    outfile.write(str(fertDestination) + " -> " + str(watDestination)  + "\n")
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
                            outfile.write("wat")
                            outfile.write(str(watDestination) + " -> " + str(lightDestination)  + "\n")
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
                                    outfile.write("light")
                                    outfile.write(str(lightDestination) + " -> " + str(tempDestination)  + "\n")
                                    for temperature in lightToTemperatureArray:
                                        lightTemp = True
                                        if(int(temperature[1]) <= int(tempDestination) and int(temperature[1])+int(temperature[2]) >= int(tempDestination)):
                                            humidDestination = functionThingy(temperature, tempDestination)
                                            lightTemp = False
                                            # print(str(humidDestination) + " - - - -")
                                            # print(int(temperature[1]) < int(tempDestination))
                                            # print(int(temperature[1])+int(temperature[2]) > int(tempDestination))
                                        else:
                                            if(lightToTemperatureArray[len(lightToTemperatureArray)-1] == temperature and lightTemp):
                                                humidDestination = tempDestination
                                                lightTemp = False
                                                #print(humidDestination)
                                        if(lightTemp == False):
                                            outfile.write("temp")
                                            outfile.write(str(tempDestination) + " -> " + str(humidDestination)  + "\n")
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
                                                    outfile.write("humid")
                                                    outfile.write(str(humidDestination) + " -> " + str(locationDestination)  + "\n")
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
                                                            if(lowest == -1):
                                                                    lowest = locationFinalDestination
                                                            else:
                                                                if(int(lowest) >= int(locationFinalDestination)):
                                                                    lowest = locationFinalDestination
                                                            outfile.write("location")
                                                            outfile.write(str(locationDestination) + " -> " + str(locationFinalDestination) + "\n")
                                                            if(seedIn([seed,locationFinalDestination])):
                                                                resultsArray.append([seed,locationFinalDestination])
                                                            #print(str(lowest) + "---LOWEST---")
print(resultsArray)
lowest = resultsArray[0]
for res in resultsArray:
    if(int(lowest[1]) >= int(res[1])):
        lowest = res
print(lowest[1])
#3:18 is when i started the program

#try to cheat the loop with math
#if the seed is 768975 and the source range starts at 0
'''
the source is 768975 so the destination would be 
3378130613 + 768975
or destination = destinationStart + (sourceStart-seed)
3378899588 is the answer

'''