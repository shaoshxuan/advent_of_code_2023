testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

mostEnergized = 0

for row in range(len(testData)):
  for col in range(len(testData[0])):
    direction = ""
    if row == 0:
      direction = "D"
    elif row == len(testData)-1:
      direction = "U"
    elif col == 0:
      direction = "R"
    elif col == len(testData[0])-1:
      direction = "L"
    else: 
      continue

    energized = set()
    pathTaken = set()

    beamPath = [[row,col,direction]]
    print(beamPath)

    while len(beamPath) != 0:
      nextBeam = beamPath.pop(0)
      if nextBeam[0] < 0 or nextBeam[1] < 0:
        continue
      try:
        energized.add((nextBeam[0], nextBeam[1]))
        if nextBeam[2] == "D":
          nextBeamCoord = [nextBeam[0]+1,nextBeam[1]]
          if testData[nextBeamCoord[0]][nextBeamCoord[1]] == "." or testData[nextBeamCoord[0]][nextBeamCoord[1]] == "|":
            beamPath.append(nextBeamCoord + [nextBeam[2]])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "-":
            beamPath.append(nextBeamCoord + ["R"])
            beamPath.append(nextBeamCoord + ["L"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "/":
            beamPath.append(nextBeamCoord + ["L"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "\\":
            beamPath.append(nextBeamCoord + ["R"])
        elif nextBeam[2] == "U":
          nextBeamCoord = [nextBeam[0]-1,nextBeam[1]]
          if testData[nextBeamCoord[0]][nextBeamCoord[1]] == "." or testData[nextBeamCoord[0]][nextBeamCoord[1]] == "|":
            beamPath.append(nextBeamCoord + [nextBeam[2]])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "-":
            beamPath.append(nextBeamCoord + ["R"])
            beamPath.append(nextBeamCoord + ["L"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "/":
            beamPath.append(nextBeamCoord + ["R"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "\\":
            beamPath.append(nextBeamCoord + ["L"])
        elif nextBeam[2] == "R":
          nextBeamCoord = [nextBeam[0],nextBeam[1]+1]
          if testData[nextBeamCoord[0]][nextBeamCoord[1]] == "." or testData[nextBeamCoord[0]][nextBeamCoord[1]] == "-":
            beamPath.append(nextBeamCoord + [nextBeam[2]])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "|":
            beamPath.append(nextBeamCoord + ["U"])
            beamPath.append(nextBeamCoord + ["D"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "/":
            beamPath.append(nextBeamCoord + ["U"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "\\":
            beamPath.append(nextBeamCoord + ["D"])
        elif nextBeam[2] == "L":
          nextBeamCoord = [nextBeam[0],nextBeam[1]-1]
          if testData[nextBeamCoord[0]][nextBeamCoord[1]] == "." or testData[nextBeamCoord[0]][nextBeamCoord[1]] == "-":
            beamPath.append(nextBeamCoord + [nextBeam[2]])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "|":
            beamPath.append(nextBeamCoord + ["U"])
            beamPath.append(nextBeamCoord + ["D"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "/":
            beamPath.append(nextBeamCoord + ["D"])
          elif testData[nextBeamCoord[0]][nextBeamCoord[1]] == "\\":
            beamPath.append(nextBeamCoord + ["U"])
        pathTaken.add((nextBeam[0], nextBeam[1], nextBeam[2]))
        if (beamPath[-1][0], beamPath[-1][1],beamPath[-1][2]) in pathTaken:
          del beamPath[-1]
      except:
        continue

    if len(energized) > mostEnergized:
      mostEnergized = len(energized)

print(mostEnergized)