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

#loops through the instructionsList list checks the direction value
for value in instructionsList:
    
    #delcaring local variables and lists
    a = []
    b = []
    i = 1
    j = 0

    #splits the direction instruction from the number instruction into list a
    a = instructionsList[index].split()

    #appends the number portion of the instruction into list b as an integer
    b.append(int(a[i]))

    #checks direction instruction from list a and runs corresponding calcuation on the instruction number in list b
    if a[0] == "forward":
        horizontalPosition += b[j]
        depth += (aim * b[j])

    elif a[0] == "down":
        aim += b[j]

    elif a[0] == "up":
        aim -= b[j]

    index += 1

#calculating the desire answer
horizontalPostionByDepth = horizontalPosition * depth

#printing values for fun
print(aim)
print(depth)
print(horizontalPosition)


print(horizontalPostionByDepth)
