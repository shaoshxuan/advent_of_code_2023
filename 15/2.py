testFile = open('test.txt', 'r')
testData = testFile.read().split(',')

def hashVal(word):
  currentVal = 0
  for char in word:
    currentVal = ((currentVal + ord(char))*17)%256
  return currentVal

boxes = {}

for seq in testData:
  if "-" in seq:
    opIdx = seq.find("-")
    boxNo = hashVal(seq[:opIdx])
    if (boxNo in boxes and seq[:opIdx] in boxes[boxNo]):
      boxes[boxNo].pop(seq[:opIdx])
  elif "=" in seq:
    splitSeq = seq.split("=")
    boxNo = hashVal(splitSeq[0])
    if boxNo in boxes:
      boxes[boxNo][splitSeq[0]] = int(splitSeq[1])
    else:
      boxes[boxNo] = {splitSeq[0]: int(splitSeq[1])}

total = 0

for box, boxContents in boxes.items():
  boxTotal = 0
  for index, lens in enumerate(boxContents):
    boxTotal += (box+1) * ((index+1)*boxContents[lens])
  total += boxTotal

print(total)
