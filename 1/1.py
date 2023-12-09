testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

total = 0

for line in testData:
  numberArr = []
  for char in line:
    if (char.isdigit()):
      numberArr.append(char)
  if (len(numberArr) > 0):
    total += int(numberArr[0] + numberArr[-1])

print(total)
