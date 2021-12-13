from collections import namedtuple
from functools import reduce

enemy= {
    'hp': 103,
    'dmg' : 9,
    'armor' : 2}

#dmg, armor, cost
Item = namedtuple('item',['dmg','armor','cost'])
weapons = [Item(4,0,8),Item(5,0,10),Item(6,0,25),Item(7,0,40),Item(8,0,74)]
armor = [Item(0,0,0),Item(0,1,13),Item(0,2,31),Item(0,3,53),Item(0,4,75),Item(0,5,102)]
rings = [Item(0,0,0),Item(0,0,0),Item(1,0,25),Item(2,0,50),Item(3,0,100),Item(0,1,20),Item(0,2,40),Item(0,3,80)]

def createPlayer(items):
    player = {
    'hp':100,
    'armor':0,
    'dmg':0
    }
    for i in items:
        player['armor'] += i.armor
        player['dmg'] += i.dmg
    return player

def fight(player, enemy):
    while True:
        enemy['hp'] -= (player['dmg']-enemy['armor'])
        if enemy['hp'] <= 0:
            print("player won")
            return True
        player['hp'] -= (enemy['dmg']-player['armor'])
        if player['hp'] <= 0:
            print("enemy won")
            return False
    return False

def getEquips():
    costs = []
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r1 == r2:
                        continue
                    items = [w,a,r1,r2]
                    if not fight(createPlayer(items), dict(enemy)):
                        costs.append(reduce(lambda a,b:a+b.cost, items, 0))
    return costs
costs = getEquips()
print(sorted(costs)[-1])
