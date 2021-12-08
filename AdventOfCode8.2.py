file = open("AdventOfCodeDay8.txt")

sum = 0
letters = ["a", "b", "c", "d", "e", "f", "g"]

for line in file:

    a = line
    b = a.split("|")
    c = b[0]
    uniqueSignalPattern = c.split()
    e = b[1]
    outputValues = e.split()
    r1 = 0
    r2 = 0
    numOutput = []
    numOutputStr = 0
    numOutputInt = 0
    ZERO = []
    ONE = []
    TWO = []
    THREE = []
    FOUR = []
    FIVE = []
    SIX = []
    SEVEN = []
    EIGHT = []
    NINE = []

    index1 = 0

    #find pattern for 1 and 4 (7 and 8 have no bearing on determining 0, 2, 3, 5, 6, or 9, but finding their pattern anyway)
    while index1 < len(uniqueSignalPattern):

        x = len(uniqueSignalPattern[index1])

        if x == 2:

            one = str(uniqueSignalPattern[index1])
            letterIndex = 0

            while letterIndex < len(letters):

                y = one.find(letters[letterIndex])

                if y != -1:

                    ONE.append(letters[letterIndex])
                    
                letterIndex += 1
            
            index1 += 1

        elif x == 3:

            seven = str(uniqueSignalPattern[index1])
            letterIndex = 0

            while letterIndex < len(letters):

                y = seven.find(letters[letterIndex])

                if y != -1:

                    SEVEN.append(letters[letterIndex])
                    
                letterIndex += 1

            index1 += 1

        elif x == 4:

            four = str(uniqueSignalPattern[index1])
            letterIndex = 0

            while letterIndex < len(letters):

                y = four.find(letters[letterIndex])

                if y != -1:

                    FOUR.append(letters[letterIndex])
                    
                letterIndex += 1

            index1 += 1

        elif x == 7:
            
            eight = str(uniqueSignalPattern[index1])
            letterIndex = 0

            while letterIndex < len(letters):

                y = eight.find(letters[letterIndex])

                if y != -1:

                    EIGHT.append(letters[letterIndex])
                    
                letterIndex += 1

            index1 += 1

        else:

            index1 += 1

    index2 = 0

    #find pattern for 6, 9, and 0
    while index2 < len(uniqueSignalPattern):

        x = len(uniqueSignalPattern[index2])

        if x == 6:

            tbd = str(uniqueSignalPattern[index2])
            y = tbd.find(ONE[0])
            z = tbd.find(ONE[1])
            e = tbd.find(FOUR[0])
            f = tbd.find(FOUR[1])
            g = tbd.find(FOUR[2])
            h = tbd.find(FOUR[3])
            letterIndex = 0

            if y == -1 or z == -1:

                six = str(tbd)

                while letterIndex < len(letters):

                    q = six.find(letters[letterIndex])

                    if q != -1:

                        SIX.append(letters[letterIndex])

                    letterIndex += 1

                if y == -1:

                    r1 = str(ONE[0])
                    r2 = str(ONE[1])

                elif z == -1:

                    r1 = str(ONE[1])
                    r2 = str(ONE[0])

            elif e == -1 or f == -1 or g == -1 or h == -1:

                zero = str(tbd)

                while letterIndex < len(letters):

                    q = zero.find(letters[letterIndex])

                    if q != -1:

                        ZERO.append(letters[letterIndex])

                    letterIndex += 1

            elif e != -1 and f != -1 and g != -1 and h != -1:

                nine = str(tbd)

                while letterIndex < len(letters):

                    q = nine.find(letters[letterIndex])

                    if q != -1:

                        NINE.append(letters[letterIndex])

                    letterIndex += 1

            index2 += 1

        else:

            index2 += 1

    index3 = 0

    #find pattern for 2, 3, and 5
    while index3 < len(uniqueSignalPattern):

        x = len(uniqueSignalPattern[index3])
        
        if x == 5:

            tbd = str(uniqueSignalPattern[index3])
            y = tbd.find(r1)
            z = tbd.find(r2)
            letterIndex = 0

            if z == -1:

                two = str(tbd)

                while letterIndex < len(letters):

                    q = two.find(letters[letterIndex])

                    if q != -1:

                        TWO.append(letters[letterIndex])

                    letterIndex += 1

            elif y == -1:

                five = str(tbd)

                while letterIndex < len(letters):

                    q = five.find(letters[letterIndex])

                    if q != -1:

                        FIVE.append(letters[letterIndex])

                    letterIndex += 1

            elif y != -1 and z != -1:

                three = str(tbd)

                while letterIndex < len(letters):

                    q = three.find(letters[letterIndex])

                    if q != -1:

                        THREE.append(letters[letterIndex])

                    letterIndex += 1

            index3 += 1

        else:

            index3 += 1

    index4 = 0

    while index4 < len(outputValues):

        x = len(outputValues[index4])

        if x == 2:

            numOutput.append(str("1"))

        elif x == 4:

            numOutput.append(str("4"))

        elif x == 3:
            
            numOutput.append(str("7"))

        elif x == 7:

            numOutput.append(str("8"))

        elif x == 6:

            y = str(outputValues[index4])

            if y.find(SIX[0]) != -1 and y.find(SIX[1]) != -1 and y.find(SIX[2]) != -1 and y.find(SIX[3]) != -1 and y.find(SIX[4]) != -1 and y.find(SIX[5]) != -1:

                numOutput.append(str("6"))

            elif y.find(NINE[0]) != -1 and y.find(NINE[1]) != -1 and y.find(NINE[2]) != -1 and y.find(NINE[3]) != -1 and y.find(NINE[4]) != -1 and y.find(NINE[5]) != -1:

                numOutput.append(str("9"))

            elif y.find(ZERO[0]) != -1 and y.find(ZERO[1]) != -1 and y.find(ZERO[2]) != -1 and y.find(ZERO[3]) != -1 and y.find(ZERO[4]) != -1 and y.find(ZERO[5]) != -1:

                numOutput.append(str("0"))

        elif x == 5:

            y = str(outputValues[index4])

            if y.find(TWO[0]) != -1 and y.find(TWO[1]) != -1 and y.find(TWO[2]) != -1 and y.find(TWO[3]) != -1 and y.find(TWO[4]) != -1:

                numOutput.append(str("2"))

            elif y.find(THREE[0]) != -1 and y.find(THREE[1]) != -1 and y.find(THREE[2]) != -1 and y.find(THREE[3]) != -1 and y.find(THREE[4]) != -1:

                numOutput.append(str("3"))

            elif y.find(FIVE[0]) != -1 and y.find(FIVE[1]) != -1 and y.find(FIVE[2]) != -1 and y.find(FIVE[3]) != -1 and y.find(FIVE[4]) != -1:

                numOutput.append(str("5"))

        index4 += 1

    numOutputStr = str(numOutput[0]) + str(numOutput[1]) + str(numOutput[2]) + str(numOutput[3])
    numOutputInt = int(numOutputStr)

    sum += numOutputInt

print(sum)   