file = open("input.txt", "r")
input = file.read()


def main(): 
    first = 0
    second = 0
    third = 0
    next = 0
    for line in input.splitlines():
        if line == "":
            if next > first:
                third = second
                second = first
                first = next
            elif next > second:
                third = second
                second = next
            elif next > third:
                third = next
            next = 0
        else:
            next += int(line)
    print(first + second + third)
main()