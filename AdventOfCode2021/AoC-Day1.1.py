f = open("AdventOfCodeDay1.txt", "rt")

#declaring of needed global variables
increased = 0
decreased = 0
x = 0
y = 1

#declaring list to store values
measurementList = []

#loops through file and stores values in measurementList list as integers
for line in f:
    measurementList.append(int(line))

#loops through list to run comparisons    
for value in measurementList:

    #avoids from going out of scope
    if y != 2000:

        #compares an index value to the index value immediately after it to see if it is greater than or less than the index value immediately after it
        if measurementList[x] < measurementList[y]:

            #adds 1 to the increased variable
            increased += 1

            #adds 1 to x and y to incrementally increase the starting index value to work through the list
            x += 1
            y += 1

        else:

            #adds 1 to the decreased variable
            decreased += 1

            #adds 1 to x and y to incrementally increase the starting index value to work through the list
            x += 1
            y += 1

#prints both the number of increases and decreases
print(increased)
print(decreased)

