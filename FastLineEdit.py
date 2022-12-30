import sys

outFile = open("C:\\Users", "w")

lines = sys.stdin.read().splitlines()
linesNum = len(lines)

for lineCounter in range(linesNum):
    if (((lineCounter + 1) % 5 == 0) & (lineCounter != 0)):
        enter = "\n"
    else:

    if ((lineCounter + 1) != linesNum):
        comma = ","
    else:
        comma = ""

    lines[lineCounter] = lines[lineCounter] + comma + enter
    outFile.write(lines[lineCounter])
    
print(lines)
outFile.close()

