import re

immuneData = """698 units each with 10286 hit points with an attack that does 133 fire damage at initiative 9\n
6846 units each with 2773 hit points (weak to slashing, cold) with an attack that does 4 slashing damage at initiative 14\n
105 units each with 6988 hit points (weak to bludgeoning; immune to radiation) with an attack that does 616 radiation damage at initiative 17\n
5615 units each with 7914 hit points (weak to bludgeoning) with an attack that does 13 radiation damage at initiative 20\n
1021 units each with 10433 hit points (weak to cold; immune to slashing, bludgeoning) with an attack that does 86 bludgeoning damage at initiative 12\n
6099 units each with 11578 hit points with an attack that does 15 bludgeoning damage at initiative 13\n
82 units each with 1930 hit points (weak to bludgeoning; immune to cold) with an attack that does 179 bludgeoning damage at initiative 5\n
2223 units each with 9442 hit points (immune to bludgeoning) with an attack that does 38 cold damage at initiative 19\n
140 units each with 7594 hit points (weak to radiation) with an attack that does 452 fire damage at initiative 8\n
3057 units each with 3871 hit points (weak to bludgeoning) with an attack that does 11 radiation damage at initiative 16"""

infectionData = """263 units each with 48098 hit points (immune to radiation; weak to slashing) with an attack that does 293 bludgeoning damage at initiative 2\n
111 units each with 9893 hit points (immune to slashing) with an attack that does 171 fire damage at initiative 18\n
2790 units each with 36205 hit points with an attack that does 25 cold damage at initiative 4\n
3325 units each with 46479 hit points (weak to slashing) with an attack that does 27 radiation damage at initiative 1\n
3593 units each with 6461 hit points (weak to fire, slashing) with an attack that does 3 radiation damage at initiative 15\n
2925 units each with 13553 hit points (weak to cold, bludgeoning; immune to fire) with an attack that does 8 cold damage at initiative 10\n
262 units each with 43260 hit points (weak to cold) with an attack that does 327 radiation damage at initiative 6\n
4228 units each with 24924 hit points (weak to radiation, fire; immune to cold, bludgeoning) with an attack that does 11 cold damage at initiative 11\n
689 units each with 42315 hit points (weak to cold, slashing) with an attack that does 116 fire damage at initiative 7\n
2649 units each with 37977 hit points (weak to radiation) with an attack that does 24 cold damage at initiative 3"""

pattern = "(\d+) units each with (\d+) hit points \((.*)\) with an attack that does (\d+) (.*) damage at initiative (\d+)"
weakness = "weak to (.*);?"
immune = "immune to (.*)"

def parse(s):
    army = []
    for l in s.split("\n"):
        if len(l)==0:
            continue
        
        print l
        m = re.search(pattern, l)
        if m != None:
            print m.group(3)
            weaknesses = []
            try:
                weaknesses = re.search(weakness, m.group(3)).group(1).split(",")
            except:
                pass
            
            immunities = []
            try:
                immunities = re.match(immune, m.group(3)).group(1).split(",")
            except:
                pass

            army.append({
                "units": int(m.group(1)),
                "hp": int(m.group(2)),
                "dmg": int(m.group(4)),
                "dmgtype": m.group(5),
                "initiative": int(m.group(6)),
                "weakness": weaknesses,
                "immune": immunities
                }
            )
    return army

def effectivePower(group):
    return group['units']*group['dmg']

#both are groups
def getDmgDone(attacking, receiving):
    multiplier = 1
    if attacking['dmgtype'] in receiving['immune']:
        multiplier = 0
        
    if attacking['dmgtype'] in receiving['weakness']:
        multiplier = 2

    return effectivePower(attacking)*multiplier

def countUnitsLost(group, dmgDone):
    return dmgDone/army['hp']

def fight(army1,army2):
    groupInitiativeList = army1+army2
    groupInitiativeList.sort(key=lambda a: a['initiative'], reverse=True)
    groupInitiativeList.sort(key=lambda a: effectivePower(a), reverse=True)
    print map(lambda a: str(a['initiative'])+" "+str(effectivePower(a)),groupInitiativeList, )

def hasUnits(army):
    units = 0
    for a in army:
        units += a['units']
    return units > 0

immuneArmy, infectionArmy = parse(immuneData), parse(infectionData)
#while hasUnits(immuneArmy) and hasUnits(infectionArmy):
fight(immuneArmy, infectionArmy)
