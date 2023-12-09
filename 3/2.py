import string

testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

special_characters = list(string.punctuation)
special_characters.remove("*")

def padData(testData):
  lineLen = len(testData)+2
  paddedData = ["." * lineLen]
  for line in testData:
    paddedData.append("." + line + ".")
  paddedData.append("." * lineLen)

  for lineNo in range(len(paddedData)):
    for charNo in range(len(paddedData[lineNo])):
      if paddedData[lineNo][charNo] in special_characters:
        paddedData[lineNo] = paddedData[lineNo][:charNo] + "." + paddedData[lineNo][charNo+1:len(paddedData[lineNo])]
  return(paddedData)

paddedData = padData(testData)

total = 0

def findDigitStartIndex(line):
  return line.rfind(".")+1

def findDigitStopIndex(line):
  return line.find(".")

def getCenter(line, asteriskIndex):
  leftSide = line[findDigitStartIndex(line[:asteriskIndex]):asteriskIndex]
  rightSide = line[asteriskIndex:findDigitStopIndex(line[asteriskIndex:])+asteriskIndex]
  return int(leftSide + rightSide)

def getLeft(line, asteriskIndex):
  return int(line[findDigitStartIndex(line[:asteriskIndex]): asteriskIndex])

def getRight(line, asteriskIndex):
  return int(line[asteriskIndex+1:findDigitStopIndex(line[asteriskIndex+1:])+asteriskIndex+1])

for lineNo in range(1, len(paddedData)-1):
  lineLen = len(paddedData[lineNo])
  for charNo in range(len(paddedData[lineNo])):
    adjacentNums = []
    if paddedData[lineNo][charNo] == "*":
      for line in range(lineNo-1, lineNo+2):
        if (paddedData[line][charNo].isdigit()):
          adjacentNums.append(getCenter(paddedData[line], charNo))
        else:
          if (paddedData[line][charNo-1].isdigit()):
            adjacentNums.append(getLeft(paddedData[line], charNo))
          if (paddedData[line][charNo+1].isdigit()):
            adjacentNums.append(getRight(paddedData[line], charNo))

    if len(adjacentNums) == 2:
      total +=  adjacentNums[0] * adjacentNums[1]

print(total)