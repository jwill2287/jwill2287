file = open("AdventOfCodeDay8.txt")

outputValues = []
oneFourSevenEight = 0

for line in file:

    a = line
    b = a.split("|")
    c = b[1]
    outputValues = c.split()
    i = 0

    while i < len(outputValues):
        x = str(outputValues[i])
        y = len(x)

        if y == 2 or y == 4 or y == 3 or y == 7:

            oneFourSevenEight += 1

        i += 1

print(oneFourSevenEight)