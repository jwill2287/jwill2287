file = open("AdventOfCodeDay7.txt")

fuelConsumed = 0

crabLocations = []

for line in file:

    a = line
    b = a.split(",")
    x = 0

    while x < len(b):
        crabLocations.append(int(b[x]))
        x += 1

crabLocations.sort()

med = crabLocations[len(crabLocations)//2]

for value in crabLocations:
    fuelConsumed += abs(value-med)

print(fuelConsumed)
