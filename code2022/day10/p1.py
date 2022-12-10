
def computer(commands):
    cycles = 0
    x = 1
    cycleValues = [20+40*i for i in range(6)]
    xValues = []
    def noop(_):
        nonlocal cycles,x
        for i in range(1):
            cycles += 1
            if cycles in cycleValues:
                xValues.append(x*cycles)
    def addx(amount):
        nonlocal cycles,x
        for i in range(2):
            cycles += 1
            if cycles in cycleValues:
                xValues.append(x*cycles)
        x += amount

    c = {'noop':noop,
         'addx':addx}

    for command, amount in commands:
        c[command](int(amount))
    print(sum(xValues))
    
with open("data.txt") as f:
    
    data = f.read().splitlines()
    data = [line.split(" ") for line in data]
    [c.append(0) for c in data if len(c)==1]
    computer(data)
