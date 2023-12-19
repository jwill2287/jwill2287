fileLineSegments = open("AdventOfCodeDay5.txt")

i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
q = 0

count = 0
finalCount = 0

lineSegmentList = []
lineSegmentListValues = []
coordinatesString1 = []
coordinatesString2 = []
filteredCoordinatesString1 = []
filteredcoordinatesString2 = []
pointsHit = []
pointsHitTwice = []
finalPointsHitTwice = []


for line in fileLineSegments:
    a = line
    b = a.split()
    lineSegmentList.append(b)

for value in lineSegmentList:
    a = lineSegmentList[i]
    x = 0
    while x < 3:
        lineSegmentListValues.append(a[x])
        x += 1
    i += 1

lineSegmentListValues = [x for x in lineSegmentListValues if x != "->"]

for value in lineSegmentListValues:
    
    if k == 0:
        coordinatesString1.append(str(lineSegmentListValues[j]))
        j += 1
        k = 1
    elif k == 1:
        coordinatesString2.append(str(lineSegmentListValues[j]))
        j += 1
        k = 0

for value in coordinatesString1 and coordinatesString2:
    a = str(coordinatesString1[l])
    b = a.split(",")
    x1 = int(b[0])
    y1 = int(b[1])
    
    c = str(coordinatesString2[l])
    d = c.split(",")
    x2 = int(d[0])
    y2 = int(d[1])

    if b[0] == d[0] or b[1] == d[1]:
        
        filteredCoordinatesString1.append(coordinatesString1[l])
        filteredcoordinatesString2.append(coordinatesString2[l])

    else:
        slope = int((y2 - y1) / (x2 - x1))

        if slope == 1 or slope == -1:
            filteredCoordinatesString1.append(coordinatesString1[l])
            filteredcoordinatesString2.append(coordinatesString2[l])
    
    l += 1

for value in filteredCoordinatesString1 and filteredcoordinatesString2:
    a = str(filteredCoordinatesString1[m])
    b = a.split(",")
    x1 = int(b[0])
    y1 = int(b[1])

    c = str(filteredcoordinatesString2[m])
    d = c.split(",")
    x2 = int(d[0])
    y2 = int(d[1])
    
    if x1 == x2:

        if y1 < y2:

            while y1 <= y2:
                x1str = str(x1)
                y1str = str(y1)
                pointsHit.append(str(x1str + "," + y1str))
                y1 += 1

        elif y2 < y1:

            while y2 <= y1:
                x1str = str(x1)
                y2str = str(y2)
                pointsHit.append(str(x1str + "," + y2str))
                y2 += 1

    elif y1 == y2:

        if x1 < x2:

            while x1 <= x2:
                x1str = str(x1)
                y1str = str(y1)
                pointsHit.append(str(x1str + "," + y1str))
                x1 += 1

        elif x2 < x1:

            while x2 <= x1:
                x2str = str(x2)
                y1str = str(y1)
                pointsHit.append(str(x2str + "," + y1str))
                x2 += 1

    else:

        slope = int((y2 - y1) / (x2 - x1))

        if slope == 1:

            if x1 < x2 and y1 < y2:

                while x1 <= x2 and y1 <= y2:
                    x1str = str(x1)
                    y1str = str(y1)
                    pointsHit.append(str(x1str + "," + y1str))
                    x1 += 1
                    y1 += 1

            elif x1 > x2 and y1 > y2:

                while x1 >= x2 and y1 >= y2:
                    x1str = str(x1)
                    y1str = str(y1)
                    pointsHit.append(str(x1str + "," + y1str))
                    x1 -= 1
                    y1 -= 1            
            
        elif slope == -1:

            if x1 < x2 and y1 > y2:

                while x1 <= x2 and y1 >= y2:
                    x1str = str(x1)
                    y1str = str(y1)
                    pointsHit.append(str(x1str + "," + y1str))
                    x1 += 1
                    y1 -= 1

            elif x1 > x2 and y1 < y2:

                while x1 >= x2 and y1 <= y2:
                    x1str = str(x1)
                    y1str = str(y1)
                    pointsHit.append(str(x1str + "," + y1str))
                    x1 -= 1
                    y1 += 1

    m += 1

for value in pointsHit:
    count += 1

print(count)
pointsHit.sort()

while n < len(pointsHit):
    x = str(pointsHit[n])
    p = n + 1

    if p < len(pointsHit):
        y = str(pointsHit[p])
        
        if x == y:
            pointsHitTwice.append(str(x))

    n += 1

count1 = 0
for value in pointsHitTwice:
    count1 += 1

print(count1)

for value in pointsHitTwice:
    finalPointsHitTwice.append(value)

while q < len(pointsHitTwice):
    x = str(pointsHitTwice[q])
    p = q + 1

    if p < len(pointsHitTwice):
        y = str(pointsHitTwice[p])

        if x == y:
            finalPointsHitTwice.remove(y)

    q += 1

for value in finalPointsHitTwice:
    finalCount += 1

print(finalCount)
