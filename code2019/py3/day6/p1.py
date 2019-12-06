def travelUpTree(obj, hierarchy):
    if obj in hierarchy:
        #print("found parent for",obj,":",hierarchy[obj])
        return 1+ travelUpTree(hierarchy[obj], hierarchy)
    else:
        #print("no found parent for",obj)
        return 0

orbits = {}
parents = {}
objects = set()
with open("../../day6.txt","r") as f:
    #test = """COM)B ,B)C ,C)D ,D)E ,E)F ,B)G ,G)H ,D)I ,E)J ,J)K ,K)L """
    #for line in test.split(","):
    for line in f:
        orbit = line[:-1].split(")")
        orbits.setdefault(orbit[0],[]).append(orbit[1])
        parents[orbit[1]] = orbit[0]
        objects.add(orbit[0])
        objects.add(orbit[1])

#print(orbits)
#print(parents)
numOfOrbits = 0
for obj in objects:
    numOfOrbits += travelUpTree(obj, parents)

print(numOfOrbits)
