testFile = open('test.txt', 'r')
testData = testFile.read().split('\n')

timings = testData[0].split()
distances = testData[1].split()

def distanceTrav(held, time):
  timeLeft = time - held
  distanceTotal = timeLeft * held

  return distanceTotal

total = ""

for timing in range(1, len(timings)):
  count = 0
  distance = distances[timing]
  for duration in range(int(timings[timing])):
    if distanceTrav(duration, int(timings[timing])) > int(distance):
      count += 1
  if total == "":
    total = count
  else: 
    total *= count
  
print(total)