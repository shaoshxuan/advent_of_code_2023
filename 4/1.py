testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

total = 0

for card in testData:
  cardNums = card.split(": ")[1]
  bothNums = cardNums.split(" | ")
  myNums = bothNums[0].split(" ")
  winningNums = bothNums[1].split(" ")

  cardPoints = 0

  for myNum in myNums:
    if myNum != "":
      if myNum in winningNums:
        if cardPoints == 0:
          cardPoints = 1
        else:
          cardPoints *= 2
  total += cardPoints
  
print(total)