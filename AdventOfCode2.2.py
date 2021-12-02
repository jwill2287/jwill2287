file = open("AdventOfCodeDay2.txt", "rt")

#declaring of needed global variables
horizontalPostionByDepth = 0
horizontalPosition = 0
depth = 0
aim = 0
index = 0


#declaring list to store values
instructionsList = []

#loops through file and stores values in instructionsList list
for line in file:
    instructionsList.append(line)

#loops through the instructionsList list, splits the direction from the number inside of a, appends the number into b as an integer, checks the direction value, runs appropriate calculation according to the direction given
for value in instructionsList:
    a = []
    b = []
    i = 1
    j = 0
    a = instructionsList[index].split()
    b.append(int(a[i]))

    if a[0] == "forward":
        horizontalPosition += b[j]
        depth += (aim * b[j])

    elif a[0] == "down":
        aim += b[j]

    elif a[0] == "up":
        aim -= b[j]

    index += 1

#
horizontalPostionByDepth = horizontalPosition * depth

print(aim)
print(depth)
print(horizontalPosition)
print(horizontalPostionByDepth)