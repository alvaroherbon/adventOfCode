file = open("input.txt", "r")
input = file.read()


def main():
    score = 0
    valuesB = {'X' : 1, 'Y': 2 , 'Z': 3}
    draw = {'X' : 'A', 'Y' : 'B' , 'Z' : 'C'}
    wins = {'Y' : 'A', 'Z' : 'B' , 'X' : 'C'}
    for line in input.splitlines():
        valueA = line[0]
        valueB = line[2]
        if (wins.get(valueB) == valueA):
            score += 6 + valuesB.get(valueB)
            print(valueA, valueB, " wins ", score)
        elif (draw.get(valueB) == valueA):
            score += 3 + valuesB.get(valueB)
            print(valueA, valueB, " draw ", score)
        else:
            score += 0 + valuesB.get(valueB)
            print(valueA, valueB, " loss ", score)

main()