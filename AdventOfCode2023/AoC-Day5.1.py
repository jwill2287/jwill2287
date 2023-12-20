file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day5-SeedLocationData.txt")
data = []
dataDict = {}
seeds = []

for line in file:
    if line.strip() != "":
        data.append(line.strip())

for string in data:
    if string.startswith("seeds"):
        seeds = string.split(":")
        seeds = seeds[-1].split()
        data.remove(string)

value = []
for string in data:
    string = string.rstrip(" map:")
    if string[0].isalpha():
        key = string
        dataDict[key] = []
        value = []
    else:
        value.append(string.split())
        dataDict[key] = value

endLocations = []
for seed in seeds:
    currentLocation = int(seed)
    for key in dataDict.keys():
        for value in dataDict[key]:
            destinationRangeStart = int(value[0])
            sourceRangeStart = int(value[1])
            rangeLength = int(value[2])
            sourceRangeEnd = sourceRangeStart + rangeLength
            if currentLocation in range(sourceRangeStart, sourceRangeEnd):
                difference = currentLocation - sourceRangeStart
                currentLocation = destinationRangeStart + difference
            else:
                continue
    endLocations.append(currentLocation)

answer = min(endLocations)
print(answer)