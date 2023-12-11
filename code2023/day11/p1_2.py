from itertools import combinations

def expandGalaxy(galaxies, multiplier):
    yExpansions = [y for y,line in enumerate(data) if all(a=='.' for a in line)]
    xExpansions = [x for x,line in enumerate(zip(*data)) if all(a=='.' for a in line)]
    galaxies = {(x,y) for y,line in enumerate(galaxies) for x,c in enumerate(line) if c=='#'}

    newGalaxies = set()
    for galaxy_x,galaxy_y in galaxies:
        shift_x = len(list(x for x in xExpansions if x < galaxy_x))*multiplier
        shift_y = len(list(y for y in yExpansions if y < galaxy_y))*multiplier

        newGalaxies.add((galaxy_x+shift_x,galaxy_y+shift_y))         
    return newGalaxies

with open('data.txt') as f:
    data = f.read().splitlines()
    
for i, multiplier in enumerate([1,10**6-1], start=1):
    newGalaxy = expandGalaxy(data, multiplier)
    totalDist = 0
    for (g1_x,g1_y),(g2_x,g2_y) in combinations(newGalaxy, r=2):
        totalDist += (abs(g1_x-g2_x)+abs(g1_y-g2_y))
    print(f"Part {i}: {totalDist}")
    