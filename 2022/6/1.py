file = open("input.txt", "r")
input = file.read()


def main():
    for line in input.splitlines():
        index = 3
        for i in range(0, len(line)):
            substring = line[i : i + 4]
            contador = 0
            for j in substring:
                if substring.count(j) == 1:
                    contador += 1
                index += 1
            print(substring, index)
            if contador == 4:
                return index


print(main())
