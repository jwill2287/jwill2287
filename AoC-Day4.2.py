file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day4-CardData.txt")
cards = []
cardsDict = {}
cardCount = []
total = 0


for line in file:
    cards.append(line.strip())

for string in cards:
    card = string.split(":")
    numbers = card[1].split("|")
    cardsDict.update({card[0]: {"winning": numbers[0].split(), "myNumbers": numbers[1].split()}})

for key in cardsDict:
    cardCount.append(1)

loopCount = 0
for key in cardsDict:
    winningCount = 0
    winningNumbers = cardsDict[key]["winning"]
    Numbers = cardsDict[key]["myNumbers"]
    for number in winningNumbers:
        for num in Numbers:
            if number == num:
                winningCount += 1
                cardCount[winningCount + loopCount] += (1 * cardCount[loopCount])
    loopCount += 1

for card in cardCount:
    total += card

print(total)