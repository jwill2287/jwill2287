file = open("C:\\Users\jwill\Documents\AdeventOfCode\Day1-CalibrationData.txt")
data = []
numbersAsWords = ["one","two","three","four","five","six","seven","eight","nine"]
total = 0
for line in file:
    data.append(line.strip())

for string in data:
    digits = []
    for i, character in enumerate(string):
        if character.isdigit():
            digits.append(character)
        for number, word in enumerate(numbersAsWords):
            if string[i:].startswith(word):
                digits.append(str(number+1))
    total += int(digits[0] + digits[-1])
print(total)