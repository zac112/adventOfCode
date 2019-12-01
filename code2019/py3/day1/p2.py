def countFuel(x):
    fuel = int(x/3)-2
    if fuel <= 0:
        return 0
    return fuel+countFuel(fuel)

with open("../../day1.txt", "r") as f:
    print(sum([countFuel(int(x)) for x in f]))
