file = open("input.txt", "r")
input = file.read()

def main(): 
    number = 0
    for line in input.splitlines(): 
        condition = False
        Onesub1 = int(line.split(",")[0].split("-")[0].strip())
        Onesub2 = int(line.split(",")[0].split("-")[1].strip())
        Twosub1 = int(line.split(",")[1].split("-")[0].strip())
        Twosub2 = int(line.split(",")[1].split("-")[1].strip())
        if ((Onesub1 <= Twosub1 and Onesub2 >= Twosub1) or (Twosub1 <= Onesub1 and Twosub2 >= Onesub1)):
            condition = True
            number += 1
        print(condition)
    print(number)
         
main()

