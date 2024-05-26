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

corSeedToSoilArray = []
corSoilToFertilizerArray = []
corFertilizerToWaterArray = []
corWaterToLightArray = []
corLightToTemperatureArray = []
corTemperatureToHumidityArray = []
corHumidityToLocationArray = []

def test(lineContent):
    appendable = lineContent.strip().split(" ")
    print(appendable)
    if(appendable[0] != ""):
        seedToSoilArray.append(lineContent.strip().split(" "))
        for index in range(0,int(appendable[2])):
            corSeedToSoilArray.append([int(appendable[1])+index,int(appendable[0])+index])
processes = []
if __name__ == '__main__':
    for lineContent in fileContent:
        if("seeds" in lineContent):
            seedsArray = lineContent.strip().split(" ")
            seedsArray.remove("seeds:")
        elif("seed-to-soil map" in lineContent or seedToSoil):
            seedToSoil = True
            print("seedToSoil")
            start = time.time()
            if("seed-to-soil map" not in lineContent and "soil-to-fertilizer map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    seedToSoilArray.append(lineContent.strip().split(" "))
                    for index in range(int(appendable[2])):
                        corSeedToSoilArray.append([int(appendable[1])+index,int(appendable[0])+index])
                        if("soil-to-fertilizer map" in lineContent):
                            seedToSoil = False
                            soilToFertilizer = True
            end = time.time()
            print("it took"+ str(start-end))
        elif(soilToFertilizer):
            print("soilToFertilizer")
            if("soil-to-fertilizer map" not in lineContent and "fertilizer-to-water map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    soilToFertilizerArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corSoilToFertilizerArray.append([int(appendable[1])+index,int(appendable[0])+index])
            if("fertilizer-to-water map" in lineContent):
                soilToFertilizer = False
                fertilizerToWater = True
        elif(fertilizerToWater):
            print("fertilizerToWater")
            if("fertilizer-to-water map" not in lineContent and "water-to-light map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    fertilizerToWaterArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corFertilizerToWaterArray.append([int(appendable[1])+index,int(appendable[0])+index])
            if("water-to-light map" in lineContent):
                fertilizerToWater = False
                waterToLight = True
        elif(waterToLight):
            print("waterToLight")
            if("water-to-light map" not in lineContent and "light-to-temperature map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    waterToLightArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corWaterToLightArray.append([int(appendable[1])+index,int(appendable[0])+index])
            if("light-to-temperature map" in lineContent):
                waterToLight = False
                lightToTemperature = True
        elif(lightToTemperature):
            print("lightToTemperature")
            if("light-to-temperature map" not in lineContent and "temperature-to-humidity map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    lightToTemperatureArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corLightToTemperatureArray.append([int(appendable[1])+index,int(appendable[0])+index])
            if("temperature-to-humidity map" in lineContent):
                lightToTemperature = False
                temperatureToHumidity = True
        elif(temperatureToHumidity):
            print("temperatureToHumidity")
            if("temperature-to-humidity map" not in lineContent and "humidity-to-location map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    temperatureToHumidityArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corTemperatureToHumidityArray.append([int(appendable[1])+index,int(appendable[0])+index])
            if("humidity-to-location map" in lineContent):
                temperatureToHumidity = False
                humidityToLocation = True
        elif(humidityToLocation):
            print("humidityToLocation")
            if("temperature-to-humidity map" not in lineContent):
                appendable = lineContent.strip().split(" ")
                if(appendable[0] != ""):
                    humidityToLocationArray.append(lineContent.strip().split(" "))
                    for index in range(0,int(appendable[2])):
                        corHumidityToLocationArray.append([int(appendable[1])+index,int(appendable[0])+index])
    absoluteResolution = []
    def checkLocation(locationIn):
        yay = True
        for temp in corHumidityToLocationArray:
            if(int(locationIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                absoluteResolution.append(int(temp[1]))
                yay = False
            if(temp == corHumidityToLocationArray[len(corHumidityToLocationArray)-1] and yay):
                print(str(locationIn) + " -> " + str(locationIn))
                absoluteResolution.append(int(locationIn))



    def checkTemp(tempIn):
        yay = True
        for temp in corTemperatureToHumidityArray:
            if(int(tempIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkLocation(temp[1])
            if(temp == corTemperatureToHumidityArray[len(corTemperatureToHumidityArray)-1] and yay):
                print(str(tempIn) + " -> " + str(tempIn))
                checkLocation(tempIn)


    def checkLight(lightIn):
        yay = True
        for temp in corLightToTemperatureArray:
            if(int(lightIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkTemp(temp[1])
            if(temp == corLightToTemperatureArray[len(corLightToTemperatureArray)-1] and yay):
                print(str(lightIn) + " -> " + str(lightIn))
                checkTemp(lightIn)

    def checkWater(waterIn):
        yay = True
        for temp in corWaterToLightArray:
            if(int(waterIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkLight(temp[1])
            if(temp == corWaterToLightArray[len(corWaterToLightArray)-1] and yay):
                print(str(waterIn) + " -> " + str(waterIn))
                checkLight(waterIn)

    def checkFertilizer(fertIn):
        yay = True
        for temp in corFertilizerToWaterArray:
            if(int(fertIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkWater(temp[1])
            if(temp == corFertilizerToWaterArray[len(corFertilizerToWaterArray)-1] and yay):
                print(str(fertIn) + " -> " + str(fertIn))
                checkWater(fertIn)
    def checkSoil(soilIn):
        yay = True
        for temp in corSoilToFertilizerArray:
            if(int(soilIn) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkFertilizer(temp[1])
            if(temp == corSoilToFertilizerArray[len(corSoilToFertilizerArray)-1] and yay):
                print(str(soilIn) + " -> " + str(soilIn))
                checkFertilizer(soilIn)
    for seed in seedsArray:
        print("---------------------------")
        yay = True
        for temp in corSeedToSoilArray:
            if(int(seed) == temp[0]):
                print(str(temp[0]) + " -> " + str(temp[1]))
                yay = False
                checkSoil(temp[1])
            
            if(temp == corSeedToSoilArray[len(corSeedToSoilArray)-1] and yay):
                print(str(seed) + " -> " + str(seed))
                checkSoil(seed)
    print(absoluteResolution)
    lowest = absoluteResolution[0]
    for res in absoluteResolution:
        if(lowest >= res):
            lowest = res
    print(lowest)


#3:18 is when i started the program