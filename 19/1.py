testFile = open('test.txt', 'r')
testData = testFile.read().split('\n\n')

def conditionals(evaluate):
  if ">" in evaluate:
    specialIdx = evaluate.find(">")
    splitEval = evaluate.split(specialIdx)
    return 
  elif "<" in evaluate:
    specialIdx = evaluate.find(">")
def objWorkflow(data):
  objWorkflows = {}

  lines = data[0].split("\n")
  for line in lines:
    splitLine = line[:-1].split("{")
    key = splitLine[0]
    conditions = splitLine[1].split(",")
    objWorkflow[key] = {
      
    }
    print(conditions)

workflows = objWorkflow(testData)
parts = testData[1].split("\n")

