testFile = open('test.txt', 'r')
testData = testFile.read().split(',')

def hashVal(word):
  currentVal = 0
  for char in word:
    currentVal = ((currentVal + ord(char))*17)%256
  print(currentVal)
  return currentVal

total = 0

for seq in testData:
  total += hashVal(seq)

print(total)