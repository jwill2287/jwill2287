def checkForAsteriskAdjacent(rowIndex, colIndex):
    rowIndexString = str(rowIndex)
    colIndexString = str(colIndex)
    up = rowIndex - 1
    upString = str(up)
    down = rowIndex + 1
    downString = str(down)
    left = colIndex - 1
    leftString = str(left)
    right = colIndex + 1
    rightString = str(right)

    upAndLeftKey = "(" + upString + ", " + leftString + ")"
    upKey = "(" + upString + ", " + colIndexString + ")"
    upAndRightKey = "(" + upString + ", " + rightString + ")"
    leftKey = "(" + rowIndexString + ", " + leftString + ")"
    rightKey = "(" + rowIndexString + ", " + rightString + ")"
    downAndLeftKey = "(" + downString + ", " + leftString + ")"
    downKey = "(" + downString + ", " + colIndexString + ")"
    downAndRightKey = "(" + downString + ", " + rightString + ")"

    if rowIndex == 0 and colIndex == 0: # top left corner
        if gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[downKey] in asterisk:
            return True, downKey
        elif gridDictionary[downAndRightKey] in asterisk:
            return True, downAndRightKey
        else:
            return False, ""
    elif rowIndex + 1 == len(grid) and colIndex + 1 == len(row): # bottom right corner
        if gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[upAndLeftKey] in asterisk:
            return True, upAndLeftKey
        else:
            return False, ""
    elif rowIndex + 1 == len(grid) and colIndex == 0: # bottom left corner
        if gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[upAndRightKey] in asterisk:
            return True, upAndRightKey
        else:
            return False, ""
    elif rowIndex == 0 and colIndex + 1 == len(row): # top right corner
        if gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[downKey] not in asterisk:
            return True, downKey
        elif gridDictionary[downAndLeftKey] not in asterisk:
            return True, downAndLeftKey
        else:
            return False, ""
    elif rowIndex == 0 and colIndex != 0 and colIndex + 1 != len(row): # top row not including corners
        if gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[downAndLeftKey] in asterisk:
            return True, downAndLeftKey
        elif gridDictionary[downKey] in asterisk:
            return True, downAndLeftKey
        elif gridDictionary[downAndRightKey] in asterisk:
            return True, downAndRightKey
        else:
            return False, ""
    elif rowIndex + 1 == len(grid) and colIndex != 0 and colIndex + 1 != len(row): # bottom row not including corners
        if gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[upAndLeftKey] in asterisk:
            return True, upAndLeftKey
        elif gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[upAndRightKey] in asterisk:
            return True, upAndRightKey
        else:
            return False, ""
    elif rowIndex != 0 and rowIndex + 1 != len(grid) and colIndex == 0: # left column not including corners
        if gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[downKey] in asterisk:
            return True, downKey
        elif gridDictionary[upAndRightKey] in asterisk:
            return True, upAndRightKey
        elif gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[downAndRightKey] in asterisk:
            return True, downAndRightKey
        else:
            return False, ""
    elif rowIndex != 0 and rowIndex + 1 != len(grid) and colIndex + 1 == len(row): # right column not including corners
        if gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[downKey] in asterisk:
            return True, downKey
        elif gridDictionary[upAndLeftKey] in asterisk:
            return True, upAndLeftKey
        elif gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[downAndLeftKey] in asterisk:
            return True, downAndLeftKey
        else:
            return False, ""
    else: # all other locations
        if gridDictionary[upAndLeftKey] in asterisk:
            return True, upAndLeftKey
        elif gridDictionary[upKey] in asterisk:
            return True, upKey
        elif gridDictionary[upAndRightKey] in asterisk:
            return True, upAndRightKey
        elif gridDictionary[leftKey] in asterisk:
            return True, leftKey
        elif gridDictionary[rightKey] in asterisk:
            return True, rightKey
        elif gridDictionary[downAndLeftKey] in asterisk:
            return True, downAndLeftKey
        elif gridDictionary[downKey] in asterisk:
            return True, downKey
        elif gridDictionary[downAndRightKey] in asterisk:
            return True, downAndRightKey
        else:
            return False, ""

file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day3-EngineSchematic.txt")
grid = []
gridDictionary = {}
asteriskDict = {}
asterisk = "*"
rowIndex = int(0)
colIndex = int(0)
total = 0
asteriskAdjacent = False
asteriskLocation = ""

for line in file:
    grid.append(line.strip())

for row in grid:
    colIndex = 0
    number = ""
    for col in row:
        rowString = str(rowIndex)
        colString = str(colIndex)
        locationKey = "(" + rowString + ", " + colString + ")"
        gridDictionary[locationKey] = col
        colIndex += 1
    rowIndex += 1   

rowIndex = int(0)
for row in grid:
    colIndex = int(0)
    for col in row:
        rowString = str(rowIndex)
        colString = str(colIndex)
        locationKey = "(" + rowString + ", " + colString + ")"
        if col in asterisk:
            asteriskDict[locationKey] = []
        colIndex += 1
    rowIndex += 1

rowIndex = int(0)
for row in grid:
    colIndex = int(0)
    number = ""
    for col in row:
        if col.isdigit():
            number += col
            if asteriskAdjacent == False:
                asteriskAdjacent, asteriskLocation = checkForAsteriskAdjacent(rowIndex, colIndex)
        else:
            if number != "" and asteriskAdjacent == True and asteriskLocation != "":
                number = int(number)
                asteriskDict[asteriskLocation].append(number)
                number = ""
                asteriskAdjacent = False
            else:
                number = ""
                asteriskAdjacent = False
        if colIndex == len(row) - 1 and number != "" and asteriskAdjacent == True and asteriskLocation != "":
                number = int(number)
                asteriskDict[asteriskLocation].append(number)
                number = ""
                asteriskAdjacent = False
        colIndex += 1
    rowIndex += 1

for i in asteriskDict:
    if len(asteriskDict[i]) == 2:
        values = asteriskDict[i]
        gearRatio = values[0] * values[-1]
        total += gearRatio

print(total)