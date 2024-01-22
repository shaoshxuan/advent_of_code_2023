testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

heaviestIdx = len(testData)

tracker = {}

totalWeight = 0

for lineIdx in range(len(testData)):
  for charIdx in range(len(testData[lineIdx])):
    if charIdx not in tracker:
      tracker[charIdx] = {
        "cubeIdx": -1,
        "rockCount": 0
      }

    if testData[lineIdx][charIdx] == "#":
      for rock in range(tracker[charIdx]["rockCount"]):
        totalWeight += heaviestIdx - tracker[charIdx]["cubeIdx"] - 1 - rock
      tracker[charIdx]["cubeIdx"] = lineIdx
      tracker[charIdx]["rockCount"] = 0
    elif testData[lineIdx][charIdx] == "O":
      tracker[charIdx]["rockCount"] += 1
      
for value in tracker.values():
  for rock in range(value["rockCount"]):
    totalWeight += heaviestIdx - value["cubeIdx"] - 1 - rock
print(totalWeight)