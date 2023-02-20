file = open("input.txt", "r")
input = file.read()


def main():
    grid = [[], [], [], [], [], [], [], [], []]
    actions = []
    for i in reversed(range(8)):
        numRow = 0
        for j in range(0, len(input.splitlines()[i]), 4):
            char = input.splitlines()[i][j+1]
            if char != " " and char != "[" and char != "]":
                grid[numRow].append(char)
            numRow += 1
    print(grid)
    # for line in input.splitlines()[10:]:
    #     crates = line.split(" ")[1]
    #     fr = line.split(" ")[3]
    #     to = line.split(" ")[5]
    #     #print(crates)


main()
