testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

timing = int("".join(testData[0].split()[1:]))
distance = int("".join(testData[1].split()[1:]))

def distanceTrav(held, time):
  timeLeft = time - held
  distanceTotal = timeLeft * held

  return distanceTotal

count = 0

for duration in range(1, timing+1):
  if distanceTrav(duration, timing) > int(distance):
    count += 1

  
print(count)