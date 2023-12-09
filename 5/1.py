def cleanSplits(data):
  cleanData = []
  for ele in data:
    cleanData.append(ele.split(" "))
  return cleanData

seeds = open('seeds.txt', 'r').read().split(' ')
seedToSoil = cleanSplits(open('seedToSoil.txt', 'r').read().split('\n'))
soilToFerti = cleanSplits(open('soilToFerti.txt', 'r').read().split('\n'))
fertiToWater = cleanSplits(open('fertiToWater.txt', 'r').read().split('\n'))
waterToLight = cleanSplits(open('waterToLight.txt', 'r').read().split('\n'))
lightToTemp = cleanSplits(open('lightToTemp.txt', 'r').read().split('\n'))
tempToHumid = cleanSplits(open('tempToHumid.txt', 'r').read().split('\n'))
humidToLoc = cleanSplits(open('humidToLoc.txt', 'r').read().split('\n'))

def mapperFunc(data, toFind):
  data = int(data)
  for ele in toFind:
    if (data >= int(ele[1])) and (data < (int(ele[1]) + int(ele[2]))):
      diff = data - int(ele[1])
      return (int(ele[0]) + diff)
  return data

locations = []

for seed in seeds:
  soilNo = mapperFunc(seed, seedToSoil)
  fertiNo = mapperFunc(soilNo, soilToFerti)
  waterNo = mapperFunc(fertiNo, fertiToWater)
  lightNo = mapperFunc(waterNo, waterToLight)
  tempNo = mapperFunc(lightNo, lightToTemp)
  humidNo = mapperFunc(tempNo, tempToHumid)
  locNo = mapperFunc(humidNo, humidToLoc)

  locations.append(locNo)

print(min(locations))