from math import sqrt
with open('data.txt') as f:
    data = f.read()
    boxes = [tuple(map(int,line.split(","))) for line in data.split("\n")]

distance = lambda a,b,c,aa,bb,cc: (a-aa)**2 + (b-bb)**2 + (c-cc)**2

allCircuits = []
for box in boxes:
    circuit = set()
    circuit.add(box)
    allCircuits.append(circuit)
        
def part1():
    circuits = list(allCircuits)    
    mindist = 0
    
    for i in range(1000):
        print(i)
        closest = None
        for b1 in boxes:
            for b2 in boxes:
                if b1==b2:continue
                dist = distance(*b1,*b2)
                if closest is None or (dist>mindist and dist < closest[0]):
                    closest = (dist, b1, b2)

        d,b1,b2 = closest
        mindist = d
        for circ in circuits:
            if b1 in circ: b1_c = circ
            if b2 in circ: b2_c = circ
        if b1_c == b2_c:continue
        
        b1_c |= b2_c
        circuits.remove(b2_c)

        
    a,b,c = sorted(map(len,circuits),reverse=True)[:3]
    print("Part 1:", a*b*c)

def part2():
    circuits = list(allCircuits)

    nearest = {}
    for box in boxes:
        nearest[box] = (None,10**10)
        for box2 in boxes:
            if box == box2: continue
            dist = distance(*box,*box2)
            if nearest[box][1] > dist:
                nearest[box] = (box2, dist)
    nearest = [(k,*v) for k,v in nearest.items()]
    nearest.sort(key=lambda a:a[2])

    mindist = 0
    while True:
        closest = nearest.pop(0)

        b1,b2,d = closest
        mindist = d
        for circ in circuits:
            if b1 in circ: b1_c = circ
            if b2 in circ: b2_c = circ
        if b1_c == b2_c: continue
        
        b1_c |= b2_c
        circuits.remove(b2_c)
        if len(nearest)==0:
            print("Last boxes:",b1,b2)
            print("Part 2:",b1[0]*b2[0])
            break
part1()
part2()
