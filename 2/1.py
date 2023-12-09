testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

stock = {
  "red": 12,
  "green": 13,
  "blue": 14
}

total = 0

for gameNo in range(len(testData)):
  possible = True
  noGame = testData[gameNo][testData[gameNo].find(":")+2:]
  drawArr = noGame.split("; ")
  for draws in drawArr:
    drawSplit = draws.split(", ")
    for eachSplit in drawSplit:
      colorize = eachSplit.split(" ")
      if (int(colorize[0]) > stock[colorize[1]]):
        possible = False
  if (possible):
    total += gameNo+1

print(total)