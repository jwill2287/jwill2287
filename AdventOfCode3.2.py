file = open("AdventOfCodeDay3.txt", "rt")

#declaring of needed global variables
lifeSupportRating = 0
oRating = 0
oString = 0
co2Rating = 0
co2String = 0
a = 0
index = 0
i = 1
j = 0
k = 0
bit = 0
countOne = 0
countZero = 0

#declaring lists to store values
diagnosticReportList = []
b=[]
c=[]

#loops through file and stores values in diagnosticReportList, b, and c lists
for line in file:
    diagnosticReportList.append(line)
    b.append(line)
    c.append(line)

#loops to go through list b until there is only 1 index value left in b
while i < len(b):

    #resets the index variable to 0
    index = 0

    #loops through list b as long as it is in range
    for value in range(len(b)):

        #sets variable a to be the next value from list b as a string
        a = (b[index])

        #sets the bit variable to the appropriate character from variable a
        bit = a[j]

        #check to see if the bit variable is a 1 or 0 and starts adding to countOne and countZero
        if bit == "1":
            countOne += 1

        elif bit == "0":
            countZero += 1

        index += 1

    #compares countOne to countZero to determine what the bit variable should be set as in order to compare the characters from each index value so appropriate values can be progressively eliminated from list b
    if countOne >= countZero:
        bit = "1"

    elif countOne < countZero:
        bit = "0"

    #resets the index, countOne, and countZero variables to 0
    index = 0
    countOne = 0
    countZero = 0

    #loops through list b as long as it is in range
    for value in range(len(b)):

        #sets variable a to be the next value from list b as a string
        a = (b[index])

        #sets the bitCompare variable to the appropriate character from variable a
        bitCompare = a[j]

        #checks to see if the bit variable is not equal to the bitCompare variable and either eliminates the index value from list b or adds 1 to the index variable
        if bit != bitCompare:
            b.pop(index)
    
        else:
            index += 1
    
    #increases variable j by 1 so it moves onto the next character for the bit and bitCompare variables
    j += 1

#sets the oString variable to the only remaining list b index value
oString = b[0]

#converts the oString string variable into the oRating integer variable as a decimal
oRating = int(oString, 2)

#prints the oString variable for validation purposes
print(oString)

#prints the oRating variable for validation purposes
print(oRating)

#loops to go through list b until there is only 1 index value left in c
while i < len(c):

    #resets the index variable to 0
    index = 0

    #loops through list c as long as it is in range
    for value in range(len(c)):

        #sets variable a to be the next value from list c as a string
        a = (c[index])

        #sets the bit variable to the appropriate character from variable a
        bit = a[k]

        #check to see if the bit variable is a 1 or 0 and starts adding to countOne and countZero
        if bit == "1":
            countOne += 1

        elif bit == "0":
            countZero += 1

        index += 1

    #compares countOne to countZero to determine what the bit variable should be set as in order to compare the characters from each index value so appropriate values can be progressively eliminated from list c
    if countOne >= countZero:
        bit = "0"

    elif countOne < countZero:
        bit = "1"

    #resets the index, countOne, and countZero variables to 0
    index = 0
    countOne = 0
    countZero = 0

    #loops through list c as long as it is in range
    for value in range(len(c)):

        #sets variable a to be the next value from list c as a string
        a = (c[index])

        #sets the bitCompare variable to the appropriate character from variable a
        bitCompare = a[k]

        #checks to see if the bit variable is not equal to the bitCompare variable and either eliminates the index value from list c or adds 1 to the index variable
        if bit != bitCompare:
            c.pop(index)
    
        else:
            index += 1
    
    #increases variable j by 1 so it moves onto the next character for the bit and bitCompare variables
    k += 1

#sets the co2String variable to the only remaining list c index value
co2String = c[0]

#converts the co2String string variable into the co2Rating integer variable as a decimal
co2Rating = int(co2String, 2)

#prints the co2String variable for validation purposes
print(co2String)

#prints the co2Rating variable for validation purposes
print(co2Rating)

#calculates the lifeSupportRating variable
lifeSupportRating = oRating * co2Rating

#prints the lifeSupportRating variable for validation purposes
print(lifeSupportRating)