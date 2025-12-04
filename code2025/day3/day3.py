with open('data.txt') as f:
    data = f.read().split("\n")

def maxJoltage(battery):
    biggest = battery[-1]
    combos = []
    for x in reversed(battery[:-1]):
        combos.append(int(x+biggest))
        biggest = max(biggest, x)
    return max(combos)

total = 0
for battery in data:
    total += maxJoltage(battery)
print("Part 1:",total)

def maxJoltage(battery):
    battery = list(battery)[::-1]
    numsLeft = 11
    selected = []
    while numsLeft > 0:
        biggest = max(battery[numsLeft:])        
        while battery[-1] < biggest:
            battery.pop()
        selected.append(battery.pop())        
        numsLeft -= 1
    selected.append(max(battery))
    
    return int("".join(selected))

total = 0
for battery in data:
    total += maxJoltage(battery)
    
print("Part 2:",total)
