import string

testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

special_characters = list(string.punctuation)
special_characters.remove(".")

def padData(testData):
  lineLen = len(testData)+2
  paddedData = ["." * lineLen]
  for line in testData:
    paddedData.append("." + line + ".")
  paddedData.append("." * lineLen)
  return(paddedData)

paddedData = padData(testData)

total = 0

for lineNo in range(1, len(paddedData)-1):
  lineLen = len(paddedData[lineNo])
  skipTill = 0
  for charStart in range(lineLen):
    if (charStart < skipTill):
      continue
    endIndex = charStart
    if (paddedData[lineNo][charStart].isdigit()):
      for charEnd in range(charStart, lineLen):
        if (paddedData[lineNo][charEnd].isdigit()):
          endIndex = charEnd
        else:
          skipTill = charEnd
          scanArea = paddedData[lineNo-1][charStart-1:charEnd+1] + paddedData[lineNo][charStart-1:charEnd+1] + paddedData[lineNo+1][charStart-1:charEnd+1]
          print("===")
          print(paddedData[lineNo-1][charStart-1:charEnd+1])
          print(paddedData[lineNo][charStart-1:charEnd+1])
          print(paddedData[lineNo+1][charStart-1:charEnd+1])
          if (any(ele in scanArea for ele in special_characters)):
            print(int(paddedData[lineNo][charStart: charEnd]))
            print("===")
            total += int(paddedData[lineNo][charStart: charEnd])
          break

print(total)
