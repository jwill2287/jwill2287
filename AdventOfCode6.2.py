file = open("AdventOfCodeDay6.txt")

day = 0

initialState = []
lanternFish = []

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0


for line in file:
    a = line
    b = a.split(",")
    x = 0

    while x < len(b):
        initialState.append(int(b[x]))
        x += 1

for value in initialState:
    lanternFish.append(int(value))

for value in lanternFish:

    if value == 0:

        zero += 1

    elif value == 1:

        one += 1

    elif value == 2:
        
        two += 1

    elif value == 3:
        
        three += 1

    elif value == 4:
        
        four += 1

    elif value == 5:
        
        five += 1

    elif value == 6:
        
        six += 1

while day < 256:

    previousZero = zero
    previousOne = one
    previousTwo = two
    previousThree = three
    previousFour = four
    previousFive = five
    previousSix = six
    previousSeven = seven
    previousEight = eight

    zero = previousOne
    one = previousTwo
    two = previousThree
    three = previousFour
    four = previousFive
    five = previousSix
    six = previousSeven + previousZero
    seven = previousEight
    eight = previousZero

    day += 1

total = zero + one + two + three + four + five + six + seven + eight

print(total)