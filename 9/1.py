testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

def difference(data):
  if all(ele == 0 for ele in data):
    return 0
  nextDiff = []
  for i in range(len(data)-1):
    nextDiff.append(int(data[i+1]) - int(data[i]))

  return difference(nextDiff) + nextDiff[-1]

total = 0
for line in testData:
  lineArr = line.split(" ")
  total += difference(lineArr) + int(lineArr[-1])

print(total)
