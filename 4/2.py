testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

scratchCards = {
  1: 0
}

for index, card in enumerate(testData):
  cardNumber = index + 1
  if cardNumber not in scratchCards:
    scratchCards[index+1] = 1
  else:
    scratchCards[index+1] += 1
  cardNums = card.split(": ")[1]
  bothNums = cardNums.split(" | ")
  myNums = bothNums[0].split(" ")
  winningNums = bothNums[1].split(" ")

  cardPoints = 0

  for myNum in myNums:
    if myNum != "" and myNum in winningNums:
      cardPoints += 1

  for i in range(cardPoints):
    if cardNumber+i+1 not in scratchCards:
      scratchCards[cardNumber+i+1] = scratchCards[cardNumber]
    else:
      scratchCards[cardNumber+i+1] += scratchCards[cardNumber]

total = 0

for card, count in scratchCards.items():
  total += count

print(total)