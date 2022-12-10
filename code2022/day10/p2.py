
def computer(commands):
    w,h = 40,6
    screen = [['.' for i in range(w+1)] for i in range(h+1)]
    cycles = 0
    x = 1
    def draw():
        nonlocal cycles,x
        if cycles%w-1 in [x-1,x,x+1]:
            screen[cycles//w][cycles%w-1]='#'
        else:
            screen[cycles//w][cycles%w-1]='.'

    def noop(_):
        nonlocal cycles
        for i in range(1):
            cycles += 1
            draw()

    def addx(amount):
        nonlocal cycles,x
        for i in range(2):
            cycles += 1
            draw()
        x += amount

    c = {'noop':noop,
         'addx':addx}
    for command, amount in commands:
        c[command](int(amount))        
        
    for line in screen:
        print("".join(line))
    
with open("data.txt") as f:
    
    data = f.read().splitlines()    
    data = [line.split(" ") for line in data]
    [c.append(0) for c in data if len(c)==1]
    computer(data)
