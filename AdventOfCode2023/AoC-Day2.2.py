def getReveals(game):
    return game[1].split("; ")

file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day2-GameData.txt")
colors = ["red","green","blue"]
data = []
total = 0

for line in file:
    data.append(line.strip())
    
for string in data:
    game = string.split(": ")
    reveals = getReveals(game)
    red = 0
    green = 0
    blue = 0

    for reveal in reveals:
        currentReveal = reveal.split(", ")
        i = 0

        while i < len(currentReveal):
            values = currentReveal[i].split()
            color = values[-1]
            count = int(values[0])
            if color == colors[0] and count > red:
                red = count
            elif color == colors[1] and count > green:
                green = count
            elif color == colors[2] and count > blue:
                blue = count
            i += 1
    power = red * green * blue
    total += power
print(total)









# def getGameNumber(game):
#     return int(game[0].lstrip("Game "))

# def getReveals(game):
#     return game[1].split("; ")

# def determineIfGameIsPossible(currentReveal):
#     possible = True
#     i = 0
#     while possible == True and i < len(currentReveal):
#         values = currentReveal[i].split()
#         count = int(values[0])
#         color = values[1]
#         if color == colors[0] and count > maxRedCubes:
#             return False
#         elif color == colors[1] and count > maxGreenCubes:
#             return False
#         elif color == colors[2] and count > maxBlueCubes:
#             return False
#         else:
#             i += 1
#     return True

# file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day2-GameData.txt")
# maxRedCubes = 12
# maxGreenCubes = 13
# maxBlueCubes = 14
# maxTotalCubes = maxRedCubes + maxGreenCubes + maxBlueCubes
# colors = ["red","green","blue"]
# data = []
# total = 0

# for line in file:
#     data.append(line.strip())

# for string in data:
#     game = string.split(": ")
#     gameNumber = getGameNumber(game)
#     reveals = getReveals(game)

#     for reveal in reveals:
#         currentReveal = reveal.split(", ")
#         possible = determineIfGameIsPossible(currentReveal)
#         if possible == False:
#             break
#     if possible == True:
#         total += gameNumber
# print(total) 