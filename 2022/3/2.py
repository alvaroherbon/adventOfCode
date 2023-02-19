file = open("input.txt", "r")
input = file.read()


def main():
    number = 0
    for i in range(0, len(input.splitlines()), 3):
        values = ""
        line1 = input.splitlines()[i]
        line2 = input.splitlines()[i + 1]
        line3 = input.splitlines()[i + 2]
        for j in line1: 
            if j in line2 and j in line3 and j not in values:
                values += j
        for char in values:
            if char.islower():
                number += (ord(char)) - 96 
            else:
                number += (ord(char) - 64) + 26
    print(number)

main()

