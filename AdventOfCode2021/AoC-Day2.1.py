file = open("AdventOfCodeDay2.txt", "rt")

#declaring of needed global variables
horizontalPostionByDepth = 0
horizontalPosition = 0
depth = 0
forward = 0
down = 0
up = 0
x = 0
y = 0
z = 0
i = 0
j = 0
k = 0
forwardIndex = 0
downIndex = 0
upIndex = 0

#declaring lists to store values
instructionsList = []
forwardSplit = []
downSplit = []
upSplit = []
forwardValues = []
downValues = []
upValues = []

#loops through file and stores values in instructionsList list
for line in file:
    instructionsList.append(line)

#creates separate lists for forward instructions, down instructions, and up instructions
forwardList = [x for x in instructionsList if "forward" in x]
downList = [y for y in instructionsList if "down" in y]
upList = [z for z in instructionsList if "up" in z]

#loops through the forwardList list to split values and store numbers as an integer in the forwardValues list
for value in forwardList:
    a = 0
    index = 1
    a = forwardList[forwardIndex].split()
    forwardValues.append(int(a[index]))
    forwardIndex += 1

#loops through the downList list to split values and store numbers as an integer in the downValues list
for value in downList:
    a = 0
    index = 1
    a = downList[downIndex].split()
    downValues.append(int(a[index]))
    downIndex += 1

#loops through the upList list to split values and store numbers as an integer in the upValues list
for value in upList:
    a = 0
    index = 1
    a = upList[upIndex].split()
    upValues.append(int(a[index]))
    upIndex += 1

#loops through the forwardValues list to calculate the total number
for value in forwardValues:
    forward += forwardValues[i]
    i += 1

#loops through the downValues list to calculate the total number
for value in downValues:
    down += downValues[j]
    j += 1

#loops through the upValues list to calculate the total number
for value in upValues:
    up += upValues[k]
    k += 1

#printing to validate the subsequent math
print(forward)
print(down)
print(up)

#calculating the horizontalPosition and depth
horizontalPosition = forward
depth = down - up

#printing to validate the subsequent math
print(horizontalPosition)
print(depth)

#calculating the desired answer
horizontalPostionByDepth = horizontalPosition * depth

print(horizontalPostionByDepth)
