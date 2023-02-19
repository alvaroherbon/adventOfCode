import string

file = open("input.txt", "r")
input = file.read()

def main(): 
    res = 0
    for line in input.splitlines(): 
        mid = len(line) / 2
        sub1 = line[:int(mid)]
        sub2 = line[int(mid):]
        value = ""
        number = 0
        for char in sub1: 
            if char in sub2 and char not in value:
                value += char
        print("value", value)
        for char in value:
            if char.islower():
                number += (ord(char)) - 96 
            else:
                number += (ord(char) - 64) + 26
        print("number", number)
        res += number
    print(res)
main()


