def countFuel(x):
    return int(x/3)-2

with open("../../day1.txt", "r") as f:
    print(sum([countFuel(int(x)) for x in f]))
