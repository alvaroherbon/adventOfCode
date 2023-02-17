file = open("input.txt", "r")
input = file.read()


def main():
    score = 0
    valuesB = {'X' : 1, 'Y': 2 , 'Z': 3}
    draw = {'A' : 'X', 'B' : 'Y' , 'C' : 'Z'}
    wins = {'A' : 'Y', 'B' : 'Z' , 'C' : 'X'}
    loses = {'C' : 'Y', 'A' : 'Z' , 'B' : 'X'}
    for line in input.splitlines():
        valueA = line[0]
        valueB = line[2]
        if (valueB == 'X'):
            score += 0 + valuesB.get(loses.get(valueA))
        elif (valueB == 'Y'):
            score += 3 + valuesB.get(draw.get(valueA))
        else: 
            score += 6 + valuesB.get(wins.get(valueA))
        print(score)
main()