def getPath(start, hierarchy):
    if start in hierarchy:        
        l = getPath(hierarchy[start], hierarchy)
        l.append(start)
        return l
    else:        
        return []

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
    #test = """COM)B ,B)C ,C)D ,D)E ,E)F ,B)G ,G)H ,D)I ,E)J ,J)K ,K)L ,K)YOU ,I)SAN """
    #for line in test.split(","):
    for line in f:
        orbit = line[:-1].split(")")
        orbits.setdefault(orbit[0],[]).append(orbit[1])
        parents[orbit[1]] = orbit[0]
        objects.add(orbit[0])
        objects.add(orbit[1])

#print(parents)

YOUpath = getPath("YOU", parents)
SANpath = getPath("SAN", parents)

print(YOUpath)
print(SANpath)

print( [x for x in YOUpath+SANpath if (YOUpath+SANpath).count(x) == 1 and x != "YOU" and x != "SAN"])
