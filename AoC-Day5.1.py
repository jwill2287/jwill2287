file = open("C:\\Users\jwill\Documents\AdeventOfCode\TestData.txt")
data = []
dataDict = {}
seeds = []
keys = []
values = []


for line in file:
    if line.strip() != "":
        data.append(line.strip())

print(data)

for string in data:
    if string.startswith("seeds"):
        seeds = string.split(":")
        data.remove(string)

print(seeds)
print(data)

for string in data:
    if string[0].isdigit():
        values.append(string)
    else:
        keys.append(string)

print(keys)
print(values)

i = 0
for key in keys:
    dataDict[key] = []

print(dataDict)