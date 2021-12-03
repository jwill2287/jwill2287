file = open("AdventOfCodeDay3.txt", "rt")

#declaring of needed global variables
a = 0
gString = 0
eString = 0
powerConsumption = 0
gDecimal = 0
eDecimal = 0
index = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
g6 = 0
g7 = 0
g8 = 0
g9 = 0
g10 = 0
g11 = 0
g12 = 0
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0
e6 = 0
e7 = 0
e8 = 0
e9 = 0
e10 = 0
e11 = 0
e12 = 0
bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0
bit5 = 0
bit6 = 0
bit7 = 0
bit8 = 0
bit9 = 0
bit10 = 0
bit11 = 0
bit12 = 0
countOne1 = 0
countOne2 = 0
countOne3 = 0
countOne4 = 0
countOne5 = 0
countOne6 = 0
countOne7 = 0
countOne8 = 0
countOne9 = 0
countOne10 = 0
countOne11 = 0
countOne12 = 0
countZero1 = 0
countZero2 = 0
countZero3 = 0
countZero4 = 0
countZero5 = 0
countZero6 = 0
countZero7 = 0
countZero8 = 0
countZero9 = 0
countZero10 = 0
countZero11 = 0
countZero12 = 0

#declaring list to store values
diagnosticReportList = []

#loops through file and stores values in diagnosticReportList list
for line in file:
    diagnosticReportList.append(line)

#loops through diagnosticReportList list
for value in diagnosticReportList:

    #stores the index item in a as a string
    a = (diagnosticReportList[index])

    #stores each character of the string from variable a in the corresponding bit variable
    bit1 = (a[0])
    bit2 = (a[1])
    bit3 = (a[2])
    bit4 = (a[3])
    bit5 = (a[4])
    bit6 = (a[5])
    bit7 = (a[6])
    bit8 = (a[7])
    bit9 = (a[8])
    bit10 = (a[9])
    bit11 = (a[10])
    bit12 = (a[11])

    #reviews each bit variable to determine if a 1 or 0 should be counted in the corresponding countOne and countZero variables associated with the specific bit location in the string
    if bit1 == "1":
        countOne1 += 1

    elif bit1 == "0":
        countZero1 += 1

    if bit2 == "1":
        countOne2 += 1

    elif bit2 == "0":
        countZero2 += 1
        
    if bit3 == "1":
        countOne3 += 1

    elif bit3 == "0":
        countZero3 += 1

    if bit4 == "1":
        countOne4 += 1

    elif bit4 == "0":
        countZero4 += 1

    if bit5 == "1":
        countOne5 += 1

    elif bit5 == "0":
        countZero5 += 1

    if bit6 == "1":
        countOne6 += 1

    elif bit6 == "0":
        countZero6 += 1

    if bit7 == "1":
        countOne7 += 1

    elif bit7 == "0":
        countZero7 += 1

    if bit8 == "1":
        countOne8 += 1

    elif bit8 == "0":
        countZero8 += 1

    if bit9 == "1":
        countOne9 += 1

    elif bit9 == "0":
        countZero9 += 1

    if bit10 == "1":
        countOne10 += 1

    elif bit10 == "0":
        countZero10 += 1

    if bit11 == "1":
        countOne11 += 1

    elif bit11 == "0":
        countZero11 += 1

    if bit12 == "1":
        countOne12 += 1

    elif bit12 == "0":
        countZero12 += 1

    index += 1

#compares the count of 1s and 0s in their corresponding bit location in the string and assigns the appropriate 1 or 0 to the bit location in the gamma and epsilon variables
if countOne1 > countZero1:
    g1 = "1"
    e1 = "0"

elif countOne1 < countZero1:
    g1 = "0"
    e1 = "1"


if countOne2 > countZero2:
    g2 = "1"
    e2 = "0"

elif countOne2 < countZero2:
    g2 = "0"
    e2 = "1"


if countOne3 > countZero3:
    g3 = "1"
    e3 = "0"

elif countOne3 < countZero3:
    g3 = "0"
    e3 = "1"


if countOne4 > countZero4:
    g4 = "1"
    e4 = "0"

elif countOne4 < countZero4:
    g4 = "0"
    e4 = "1"


if countOne5 > countZero5:
    g5 = "1"
    e5 = "0"

elif countOne5 < countZero5:
    g5 = "0"
    e5 = "1"


if countOne6 > countZero6:
    g6 = "1"
    e6 = "0"

elif countOne6 < countZero6:
    g6 = "0"
    e6 = "1"


if countOne7 > countZero7:
    g7 = "1"
    e7 = "0"

elif countOne7 < countZero7:
    g7 = "0"
    e7 = "1"


if countOne8 > countZero8:
    g8 = "1"
    e8 = "0"

elif countOne8 < countZero8:
    g8 = "0"
    e8 = "1"


if countOne9 > countZero9:
    g9 = "1"
    e9 = "0"

elif countOne9 < countZero9:
    g9 = "0"
    e9 = "1"


if countOne10 > countZero10:
    g10 = "1"
    e10 = "0"

elif countOne10 < countZero10:
    g10 = "0"
    e10 = "1"


if countOne11 > countZero11:
    g11 = "1"
    e11 = "0"

elif countOne11 < countZero11:
    g11 = "0"
    e11 = "1"


if countOne12 > countZero12:
    g12 = "1"
    e12 = "0"

elif countOne12 < countZero12:
    g12 = "0"
    e12 = "1"

#concatenates the gamma and epsilon strings
gString = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12
eString = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10 + e11 + e12

#prints gamma and epsilon string variables to verify
print(gString)
print(eString)

#converts the gamma and epsilon string variables into the gamma and epsilon integer variables as decimals
gDecimal = int(gString, 2)
eDecimal = int(eString, 2)

#prints gamma and epsilon integer variables to verify
print(gDecimal)
print(eDecimal)

#calculates powerConsumption
powerConsumption = gDecimal * eDecimal

#prints desired answer
print(powerConsumption)