testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

total = 0

for gameNo in range(len(testData)):
  stock = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  
  possible = True
  noGame = testData[gameNo][testData[gameNo].find(":")+2:]
  drawArr = noGame.split("; ")
  for draws in drawArr:
    drawSplit = draws.split(", ")
    for eachSplit in drawSplit:
      colorize = eachSplit.split(" ")
      if (int(colorize[0]) > stock[colorize[1]]):
        stock[colorize[1]] = int(colorize[0])
  
  cubePower = stock["red"] * stock["green"] * stock["blue"]
  if (cubePower > 0):
    if (total == 0):
      total = cubePower
    else:
      total += cubePower

print(total)
