file = open("AdventOfCodeDay3.txt", "rt")

lifeSupportRating = 0
oRating = 0
co2Rating = 0
a = 0
index = 0
i = 0
j = 0
bit = 0
countOne = 0
countZero = 0


instructionsList = []
b=[]

for line in file:
    instructionsList.append(line)
    b.append(line)

while i < len(b):
    
    index = 0
    countOne = 0
    countZero = 0
    bit = 0

    for value in b:
        a = (b[index])
        bit = a[j]

        if bit == "1":
            countOne += 1

        elif bit == "0":
            countZero += 1

        index += 1

    print(countOne)
    print(countZero)
    j +=1

    if countOne > countZero:
        bit = "1"

    elif countOne < countZero:
        bit = "0"

    index = 0

    for value in range(len(b)):
        a = (b[index])
        bitCompare = a[j]

        if bit != bitCompare:
            b.pop(index)
    
        else:
            index += 1

    print(b)     