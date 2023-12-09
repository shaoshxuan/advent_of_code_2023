testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

numberStr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0

for line in testData:
  numberArr = []
  for startChar in range(len(line)):
    for endChar in range(startChar+1, len(line)+1):
      formedStr = line[startChar:endChar]
      if (len(formedStr) == 1):
        if (formedStr.isdigit()):
          numberArr.append(formedStr)
      else:
        try:
          foundIndex = numberStr.index(formedStr)
          numberArr.append(str(foundIndex+1))
        except:
          None
  if (len(numberArr) > 0):
    total += int(numberArr[0] + numberArr[-1])

print(total)
