file = open("input.txt", "r")
input = file.read()


def main(): 
    most = 0
    next = 0
    for line in input.splitlines():
        if line == "":
            if next > most:
                most = next
            next = 0
        else:
            next += int(line)
        print(most)
    return most
main()