file = open("AdventOfCodeDay7.txt")

fuelConsumed = 0
i = 0

crabLocations = []

for line in file:

    a = line
    b = a.split(",")
    x = 0

    while x < len(b):
        crabLocations.append(int(b[x]))
        x += 1

crabLocations.sort()

minimum = min(crabLocations)
maximum = max(crabLocations)

x = minimum

for i in range(minimum, maximum):

    j = 0
    sum = 0

    while j < len(crabLocations):

        y = crabLocations[j]

        if x > y:
            z = x - y
            sum += z

        elif x < y:
            z = y - x
            sum += z

        j += 1

    if sum < fuelConsumed or fuelConsumed == 0:
        fuelConsumed = sum

    i += 1
    x = i

print(fuelConsumed)
