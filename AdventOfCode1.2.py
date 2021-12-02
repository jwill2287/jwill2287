file = open("AdventOfCodeDay1.txt", "rt")

#declaring of needed global variables
increased = 0
decreased = 0
x = 0
y = 1

#declaring list to store values
measurementList = []

#loops through file and stores values in measurementList list as integers
for line in file:
    measurementList.append(int(line))

#loops through list to run calculations
for value in measurementList:
    
    #declaring local variables to call specific index values for calculations
    a = x
    b = a + 1
    c = b + 1
    d = y
    e = d + 1
    f = e + 1

    #avoids from going out of scope
    if y != 1998:

        #sum of indexes 0, 1, 2 then 1, 2, 3 etc.
        sum1 = measurementList[a] + measurementList[b] + measurementList[c]

        #sum of indexes 1, 2, 3 then 2, 3, 4 etc.
        sum2 = measurementList[d] + measurementList[e] + measurementList[f]

        #compares sum1 to sum2 to determine if sum1 is greater or less than sum2
        if sum1 < sum2:

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

