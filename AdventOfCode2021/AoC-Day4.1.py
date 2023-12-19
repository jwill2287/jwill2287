fileNumbers = open("AdventOfCodeDay4 - NumbersDrawn.txt", "rt")
fileBoards = open("AdventOfCodeDay4 - BingoBoards.txt", "rt")

#declaring of needed global variables
finalScore = 0
sumRow = 0
sumColumn = 0
lastNumberDrawn = 0
i = 0
boardCount = 1
winningBoard = 0
numberOfLines = 0
numberOfBoards = 0
maxDrawn = 0
maxLines = 0
number = 0
numberCount = 0
previousNumberCount = 0

#declaring lists to store values
numbersDrawn = []
bingoBoards = []
finalRow = []
finalColumn = []

#loops through file, separates values, and stroes the values in the numbersDrawn list
for line in fileNumbers:
    a = line
    numbersDrawn = a.split(",")

#loops through file and stores the values in the bingoBoards list as a string which is a group of 5 numbers
for line in fileBoards:
    bingoBoards.append(line)

#filters out the empty values from the bingoBoards list and creates the newBingoBoards list
newBingoBoards = [x for x in bingoBoards if x != "\n"]

#loops through newBingoBoards list and calculates the total number of lines
for value in newBingoBoards:
    numberOfLines += 1

#calculates the total number of bingo boards and stores it as an integer
numberOfBoards = int(numberOfLines / 5)

#loops through the numbersDrawn list and calculates the total number of drawn numbers
for value in numbersDrawn:
    maxDrawn += 1

#subtract 1 from maxDrawn and calculate maxLines by subtracting 5 from numberOfLines for index purpopses
maxDrawn -= 1
maxLines = int(numberOfLines - 5)

#loops through all of the bingo boards
while boardCount <= numberOfBoards:
    
    #loops through lines of each bingo board
    while i <= maxLines:
        
        #stores each line of the bingo board as a string in separate variables
        a = str(newBingoBoards[i])
        b = str(newBingoBoards[i+1])
        c = str(newBingoBoards[i+2])
        d = str(newBingoBoards[i+3])
        e = str(newBingoBoards[i+4])

        #splits the string variables and stores the values within their respective row of the bingo board
        row1 = a.split()
        row2 = b.split()
        row3 = c.split()
        row4 = d.split()
        row5 = e.split()
        
        #creates row and column lists
        row = []
        column = []

        #ensure lists are cleared before adding values for the next loop
        row.clear()
        column.clear()
        
        #for indexing row1
        j = 0
        
        #loops through row1 and appends the values as integers into the row list
        for value in row1:
            
            row.append(int(row1[j]))
            
            j += 1

        #for indexing row2    
        k = 0
        
        #loops through row2 and appends the values as integers into the row list
        for value in row2:
            
            row.append(int(row2[k]))
            
            k += 1

        #for indexing row3    
        l = 0
        
        #loops through row3 and appends the values as integers into the row list
        for value in row3:
            
            row.append(int(row3[l]))
            
            l += 1

        #for indexing row4    
        m = 0
        
        #loops through row4 and appends the values as integers into the row list
        for value in row4:
            
            row.append(int(row4[m]))
            
            m += 1

        #for indexing row5    
        n = 0
        
        #loops through row5 and appends the values as integers into the row list
        for value in row5:
            row.append(int(row5[n]))
            
            n += 1

        #appends the values from the row lists into the appropriate column location in the column list    
        column.append(int(row1[0]))
        column.append(int(row2[0]))
        column.append(int(row3[0]))
        column.append(int(row4[0]))
        column.append(int(row5[0]))
        
        column.append(int(row1[1]))
        column.append(int(row2[1]))
        column.append(int(row3[1]))
        column.append(int(row4[1]))
        column.append(int(row5[1]))
        
        column.append(int(row1[2]))
        column.append(int(row2[2]))
        column.append(int(row3[2]))
        column.append(int(row4[2]))
        column.append(int(row5[2]))
        
        column.append(int(row1[3]))
        column.append(int(row2[3]))
        column.append(int(row3[3]))
        column.append(int(row4[3]))
        column.append(int(row5[3]))
        
        column.append(int(row1[4]))
        column.append(int(row2[4]))
        column.append(int(row3[4]))
        column.append(int(row4[4]))
        column.append(int(row5[4]))
        
        #creates bingo, numIndex, and numberCount variables
        bingo = 0
        numIndex = 0
        numberCount = 0
        
        #loops through the row and column lists to look for bingo
        while numIndex <= maxDrawn:
            
            #sets the variable number to be the last number drawn when a card has achieved bingo
            number = int(numbersDrawn[numIndex])

            #for indexing purposes
            numIndex += 1
            p = 0
            q = 0
            
            #checks to see if bingo has been reached before drawing a new number
            if bingo != 1:
                
                #tracking the number of numbers drawn before bingo is achieved
                numberCount += 1
                
                #loop to make sure the index does not go out of range
                while p < 25 and q < 25:
                    
                    #check to see if bingo is achieved prior to continuing to check if a row or column contains the number drawn
                    if bingo != 1:
                        
                        #stores the nex row and column values into variables
                        y = row[p]
                        z = column[p]
                        
                        #check to see if the number in the row and column matches the number drawn and changes the value to an X
                        if y == number:
                            
                            row[p] = "X"

                        if z == number:

                            column[p] = "X"

                        #check to see if any row or column contains a bingo
                        if (row[0] == "X" and row[1] == "X" and row[2] == "X" and row[3] == "X" and row[4] == "X") or (column[0] == "X" and column[1] == "X" and column[2] == "X" and column[3] == "X" and column[4] == "X"):
                                
                            bingo = 1
                                
                        elif (row[5] == "X" and row[6] == "X" and row[7] == "X" and row[8] == "X" and row[9] == "X") or (column[5] == "X" and column[6] == "X" and column[7] == "X" and column[8] == "X" and column[9] == "X"):
                                
                            bingo = 1
                                
                        elif (row[10] == "X" and row[11] == "X" and row[12] == "X" and row[13] == "X" and row[14] == "X") or (column[10] == "X" and column[11] == "X" and column[12] == "X" and column[13] == "X" and column[14] == "X"):
                                
                            bingo = 1
                                
                        elif (row[15] == "X" and row[16] == "X" and row[17] == "X" and row[18] == "X" and row[19] == "X") or (column[15] == "X" and column[16] == "X" and column[17] == "X" and column[18] == "X" and column[19] == "X"):
                                
                            bingo = 1
                                
                        elif (row[20] == "X" and row[21] == "X" and row[22] == "X" and row[23] == "X" and row[24] == "X") or (column[20] == "X" and column[21] == "X" and column[22] == "X" and column[23] == "X" and column[24] == "X"):
                                
                            bingo = 1
                                
                    p += 1
                    
                    q += 1

                #checks if bingo was achieved
                if bingo == 1:
                    
                    #checks if the current board took few numbers drawn to achieve bingo than the prior board and stores the board values with the X's and the number of numbers drawn to achieve bingo
                    if numberCount < previousNumberCount or previousNumberCount == 0:
                        
                        finalRow = row
                        finalColumn = column
                        previousNumberCount = numberCount
                        winningBoard = boardCount
                        
        i += 5
        
        boardCount += 1

#prints the board that "won" and the values contained in the board for validation
print(winningBoard)   
print(finalRow)
print(finalColumn)

#creates a list of values without the X's from the winning board and prints the values for validation
sumRowList = [w for w in finalRow if w != "X"]
print(sumRowList)

#creates a list of values without the X's from the winning board and prints the values for validation (duplicate work for math verification later)
sumColumnList = [v for v in finalColumn if v != "X"]
print(sumColumnList)

#for indexing
t = 0

#loops through the sumRowList and calculates the sum of the remaining values from the board
for value in sumRowList:
    sumRow += int(sumRowList[t])
    t += 1

#for indexing
u = 0

#loops through the sumColumnList and calculates the sum of the remaing values from the board (duplicate work for math verification)
for value in sumColumnList:
    sumColumn += int(sumColumnList[u])
    u += 1

#prints the number of numbers drawn to achieve bingo for the "winning" board for validation
print(previousNumberCount)

#subtracts 2 from the previousNumberCount to achieve the correct index number from the numbersDrawn list and prints for validation
previousNumberCount -= 1
print(previousNumberCount)

#stores the last number drawn in the lastNumberDrawn variable as an integer
lastNumberDrawn = int(numbersDrawn[previousNumberCount])

#prints the last number drawn and the sum of the values remaining (dupilcate work done for verification)
print(lastNumberDrawn)
print(sumRow)
print(sumColumn)

#calculates the final score of the board
finalScore = sumRow * lastNumberDrawn

#prints the answer
print(finalScore)
