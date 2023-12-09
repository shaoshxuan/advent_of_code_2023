testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

steps = list(testData[0])
cleanedSteps = []
for step in steps:
  if step == "L":
    cleanedSteps.append(0)
  elif step == "R":
    cleanedSteps.append(1)

cleanedData = {}

for line in testData[1:]:
  splitLine = line.split(" = ")
  destiArr = splitLine[1][1:-1].split(", ")
  cleanedData[splitLine[0]] = destiArr

destination = "AAA"
counter = 0

while destination != "ZZZ":
  for step in cleanedSteps:
    destination = cleanedData[destination][step]
    counter += 1
    if destination == "ZZZ":
      break

print(counter)