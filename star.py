import sys

try:
    size = int(sys.argv[1])
except ValueError:
    size = 0

halfStarMap = []

for x0 in range(size):
    newLine = [" "]*(size*6 + 1)
    if x0 == 0:
        newLine[size*3] = '*'
    else:
        newLine[size*3 + x0] = '*'
        newLine[size*3 - x0] = '*'
    halfStarMap.append(newLine)

newLine = []
for z in range(size*6 + 1):
    if z < size*2+1 or z > size*4 -1 :
        newLine.append("*")
    else:
        newLine.append(" ")
halfStarMap.append(newLine)

for x in range(size):
    newLine = [" "]*(size*6 + 1)
    newLine[x+1] = '*'
    newLine[len(newLine)-x-2] = '*'
    halfStarMap.append(newLine)

for line in halfStarMap:
    print("".join(line))
del halfStarMap[-1]
for line in reversed(halfStarMap):
    print("".join(line))