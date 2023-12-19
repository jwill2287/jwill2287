file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day4-CardData.txt")
cards = []
cardsDict = {}
cardNumbers = []
total = 0


for line in file:
    cards.append(line.strip())

for string in cards:
    card = string.split(":")
    numbers = card[1].split("|")
    cardsDict.update({card[0]: {"winning": numbers[0].split(), "myNumbers": numbers[1].split()}})

for key in cardsDict:
    points = 0
    winningNumbers = cardsDict[key]["winning"]
    Numbers = cardsDict[key]["myNumbers"]
    for number in winningNumbers:
        for num in Numbers:
            if number == num and points == 0:
                points += 1
            elif number == num and points > 0:
                points *= 2
    total += points

print(total)