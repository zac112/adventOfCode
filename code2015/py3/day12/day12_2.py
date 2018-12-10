import json

def recursiveSearchForNumbers(thing):
    sumInJson = 0

    if type(thing) == type(0):
        return int(thing)
    
    if type(thing) == type({}):
        for val in thing.values():
            if val == "red":
                return 0
        for key in thing:
            sumInJson += recursiveSearchForNumbers(thing[key])
                        
    if type(thing) == type([]):
        for element in thing:
            sumInJson += recursiveSearchForNumbers(element)

    return sumInJson

accounts = ""
with open("../../data/12.txt", "r") as f:
    for line in f:
        accounts = json.loads(line);

print(recursiveSearchForNumbers(accounts))
