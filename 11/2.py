testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

emptyRows = []
emptyCols = [item for item in range(0, len(testData))]
galaxyIdx = []

expansionSize = 1000000

for rowIdx, row in enumerate(testData):
  if testData[rowIdx].find("#") == -1:
    emptyRows.append(rowIdx)
  for colIdx, col in enumerate(row):
    if col == "#":
      galaxyIdx.append([rowIdx, colIdx])
      try:
        emptyCols.remove(colIdx)
      except ValueError:
        pass

def xCounter(val1, val2):
  lower = min(val1, val2)
  higher = max(val1, val2)
  return len(list(filter(lambda x: lower < x < higher, emptyCols)))

def yCounter(val1, val2):
  lower = min(val1, val2)
  higher = max(val1, val2)
  return len(list(filter(lambda x: lower < x < higher, emptyRows)))

total = 0

for galaxyOneIdx in range(len(galaxyIdx)-1):
  for galaxyTwoIdx in range(galaxyOneIdx+1, len(galaxyIdx)):
    xCountExp = xCounter(galaxyIdx[galaxyOneIdx][1], galaxyIdx[galaxyTwoIdx][1])
    yCountExp = yCounter(galaxyIdx[galaxyOneIdx][0], galaxyIdx[galaxyTwoIdx][0])

    total += (abs(galaxyIdx[galaxyOneIdx][0] - galaxyIdx[galaxyTwoIdx][0]) - yCountExp + (yCountExp * expansionSize)) + (abs(galaxyIdx[galaxyOneIdx][1] - galaxyIdx[galaxyTwoIdx][1]) - xCountExp + (xCountExp * expansionSize))

print(total)