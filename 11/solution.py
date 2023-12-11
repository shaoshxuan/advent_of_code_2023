import itertools as it

InputList = []
with open("test.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

ColumnPresentSet = set()
RowPresentSet = set()
RowAllSet = set()
ColumnAllSet = set()
GalaxyList = []
for y, u in enumerate(InputList):
    RowAllSet.add(y)
    for x, c in enumerate(u):
        ColumnAllSet.add(x)
        if c == "#":
            RowPresentSet.add(y)
            ColumnPresentSet.add(x)
            GalaxyList.append((x,y))

ColumnClearSet = ColumnAllSet - ColumnPresentSet
RowClearSet = RowAllSet - RowPresentSet

Answers = []
for Expand in [1, 999999]:
    ExpandedGalaxyList = []
    for x, y in GalaxyList:
        XExpand = 0
        YExpand = 0
        for c in ColumnClearSet:
            if c < x:
                XExpand += Expand
        for r in RowClearSet:
            if r < y:
                YExpand += Expand
        NX, NY = x+XExpand, y+YExpand
        ExpandedGalaxyList.append((NX,NY))

    Answer = 0
    for A, B in it.combinations(ExpandedGalaxyList, 2):
        AX, AY = A
        BX, BY = B
        NewValue = abs(AX-BX) + abs(AY-BY)
        Answer += NewValue
    Answers.append(Answer)

Part1Answer, Part2Answer = Answers

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")