def getFirstDigit(line):
    for x in line:
        if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
            return x   

def getSecondDigit(line):
    i = len(line) - 1
    while i > -1:
        if line[i] == "0" or line[i] == "1" or line[i] == "2" or line[i] == "3" or line[i] == "4" or line[i] == "5" or line[i] == "6" or line[i] == "7" or line[i] == "8" or line[i] == "9":
            return line[i]
        else:
            i -= 1

def castCalibrationValueToInt(firstDigit, secondDigit):
    return int(getCalibrationValueString(firstDigit, secondDigit))

def getCalibrationValueString(firstDigit, secondDigit):
    return firstDigit + secondDigit

file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day1-CalibrationData.txt")
total = 0
for line in file:
    firstDigit = (getFirstDigit(line))
    secondDigit = (getSecondDigit(line))
    calibrationValue = castCalibrationValueToInt(firstDigit, secondDigit)
    total += calibrationValue

print(total)

    
