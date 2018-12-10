import json

def recursiveSearchForNumbers(jsonObj):
    sumInJson = 0
    if type(jsonObj) == type(3):
        return int(jsonObj)

    #print("obj is",type(jsonObj))
    for thing in jsonObj:
        #print("thing is", type(thing))
        if type(thing) == type(3):
            sumInJson += int(thing)
            continue       
        elif type(thing) == type([]):
            sumInJson += recursiveSearchForNumbers(thing)
        elif type(thing) == type({}):
            sumInJson += recursiveSearchForNumbers(thing)
        elif type(thing) == type("") and type(jsonObj) == type({}):
            sumInJson += recursiveSearchForNumbers(jsonObj[thing])
    return sumInJson

accounts = ""
with open("../../data/12.txt", "r") as f:
    for line in f:
        accounts = json.loads(line);

print(recursiveSearchForNumbers(accounts))
