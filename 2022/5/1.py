file = open("input.txt", "r")
input = file.read()

def main(): 
    grid = []
    actions = []
    for line in input.splitlines()[:8]:
        grid.append(line)
    for line in input.splitlines()[10:]:
        crates = line.split(" ")[1]
        fr = line.split(" ")[3]
        to = line.split(" ")[5]
        for i in range(int(crates)):
            

main() 
