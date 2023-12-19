def checkForSymbolAdjcent(rowIndex, colIndex):
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
        if gridDictionary[rightKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[downAndRightKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex + 1 == len(grid) and colIndex + 1 == len(row): # bottom right corner
        if gridDictionary[leftKey] not in notSymbols or gridDictionary[upKey] not in notSymbols or gridDictionary[upAndLeftKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex + 1 == len(grid) and colIndex == 0: # bottom left corner
        if gridDictionary[rightKey] not in notSymbols or gridDictionary[upKey] not in notSymbols or gridDictionary[upAndRightKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex == 0 and colIndex + 1 == len(row): # top right corner
        if gridDictionary[leftKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[downAndLeftKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex == 0 and colIndex != 0 and colIndex + 1 != len(row): # top row not including corners
        if gridDictionary[leftKey] not in notSymbols or gridDictionary[rightKey] not in notSymbols or gridDictionary[downAndLeftKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[downAndRightKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex + 1 == len(grid) and colIndex != 0 and colIndex + 1 != len(row): # bottom row not including corners
        if gridDictionary[leftKey] not in notSymbols or gridDictionary[rightKey] not in notSymbols or gridDictionary[upAndLeftKey] not in notSymbols or gridDictionary[upKey] not in notSymbols or gridDictionary[upAndRightKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex != 0 and rowIndex + 1 != len(grid) and colIndex == 0: # left column not including corners
        if gridDictionary[upKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[upAndRightKey] not in notSymbols or gridDictionary[rightKey] not in notSymbols or gridDictionary[downAndRightKey] not in notSymbols:
            return True
        else:
            return False
    elif rowIndex != 0 and rowIndex + 1 != len(grid) and colIndex + 1 == len(row): # right column not including corners
        if gridDictionary[upKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[upAndLeftKey] not in notSymbols or gridDictionary[leftKey] not in notSymbols or gridDictionary[downAndLeftKey] not in notSymbols:
            return True
        else:
            return False
    else: # all other locations
        if gridDictionary[upAndLeftKey] not in notSymbols or gridDictionary[upKey] not in notSymbols or gridDictionary[upAndRightKey] not in notSymbols or gridDictionary[leftKey] not in notSymbols or gridDictionary[rightKey] not in notSymbols or gridDictionary[downAndLeftKey] not in notSymbols or gridDictionary[downKey] not in notSymbols or gridDictionary[downAndRightKey] not in notSymbols:
            return True
        else:
            return False

file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day3-EngineSchematic.txt")
grid = []
numbers = []
gridDictionary = {}
notSymbols = ["0","1","2","3","4","5","6","7","8","9","."]
rowIndex = int(0)
colIndex = int(0)
total = 0
symbolAdjacent = False

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
    colIndex = 0
    number = ""
    for col in row:
        if col.isdigit():
            number += col
            if symbolAdjacent == False:
                symbolAdjacent = checkForSymbolAdjcent(rowIndex, colIndex)
        else:
            if number != "" and symbolAdjacent == True:
                total += int(number)
                numbers.append(number)
                number = ""
                symbolAdjacent = False
            else:
                number = ""
                symbolAdjacent = False
        if colIndex == len(row) - 1 and number != "" and symbolAdjacent == True:
            total += int(number)
            numbers.append(number)
            number = ""
            symbolAdjacent = False 
        colIndex += 1
    rowIndex += 1
print(total)