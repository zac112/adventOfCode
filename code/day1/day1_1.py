s = 0
with open("../../data/1.txt", "r") as f:
    for line in f:
        s = s + int(line)

print s
