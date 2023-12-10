import sys
sys.setrecursionlimit(1000)

testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

def findStart(data):
  for index, line in enumerate(data):
    sIndex = line.find("S")
    if sIndex != -1:
      return [index, sIndex]

def tracePath(data, startPoint, direction):
  print(startPoint, direction)
  print(data[startPoint[0]][startPoint[1]])
  if direction == "U":
    if data[startPoint[0]-1][startPoint[1]] == "S":
      return 1
    elif data[startPoint[0]-1][startPoint[1]] == "|":
      return 1 + tracePath(data, [startPoint[0]-1, startPoint[1]], "U")
    elif data[startPoint[0]-1][startPoint[1]] == "7":
      return 1 + tracePath(data, [startPoint[0]-1, startPoint[1]], "L")
    elif data[startPoint[0]-1][startPoint[1]] == "F":
      return 1 + tracePath(data, [startPoint[0]-1, startPoint[1]], "R")
  elif direction == "D":
    if data[startPoint[0]+1][startPoint[1]] == "S":
      return 1
    elif data[startPoint[0]+1][startPoint[1]] == "|":
      return 1 + tracePath(data, [startPoint[0]+1, startPoint[1]], "D")
    elif data[startPoint[0]+1][startPoint[1]] == "J":
      return 1 + tracePath(data, [startPoint[0]+1, startPoint[1]], "L")
    elif data[startPoint[0]+1][startPoint[1]] == "L":
      return 1 + tracePath(data, [startPoint[0]+1, startPoint[1]], "R")
  elif direction == "L":
    if data[startPoint[0]][startPoint[1]-1] == "S":
      return 1
    elif data[startPoint[0]][startPoint[1]-1] == "-":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]-1], "L")
    elif data[startPoint[0]][startPoint[1]-1] == "L":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]-1], "U")
    elif data[startPoint[0]][startPoint[1]-1] == "F":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]-1], "D")
  elif direction == "R":
    if data[startPoint[0]][startPoint[1]+1] == "S":
      return 1
    elif data[startPoint[0]][startPoint[1]+1] == "-":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]+1], "R")
    elif data[startPoint[0]][startPoint[1]+1] == "J":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]+1], "U")
    elif data[startPoint[0]][startPoint[1]+1] == "7":
      return 1 + tracePath(data, [startPoint[0], startPoint[1]+1], "D")
    

starting = findStart(testData)
print(tracePath(testData, starting, "U")//2)