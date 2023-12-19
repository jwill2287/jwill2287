file = open("AdventOfCodeDay6.txt")

day = 0
previousLength = 0
newLength = 0

initialState = []
lanternFish = []

for line in file:
    a = line
    b = a.split(",")
    x = 0

    while x < len(b):
        initialState.append(int(b[x]))
        x += 1

for value in initialState:
    lanternFish.append(int(value))

previousLength = len(initialState)

while day < 80:

    i = 0

    while i < previousLength:

        if lanternFish[i] == 0:

            lanternFish[i] = 6
            lanternFish.append(int(8))

        else:

            lanternFish[i] = (lanternFish[i] - 1)

        i += 1

    newLength = len(lanternFish)
    previousLength = newLength
    day += 1

print(len(lanternFish))
