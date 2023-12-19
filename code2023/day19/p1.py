import re

with open('data.txt') as f:
    data = f.read().splitlines()
    
workflow = {}
for i,line in enumerate(data):
    data[i] = '"'+line.replace("{",'":["').replace(",",'","').replace("}",'"]')
    if not line:break

lines = '{'+",".join(data[:i])+'}'
workflow = eval(lines)

items = []
for i, line in enumerate(data[i+1:]):
    line = line.replace("=","':").replace(",",",'").replace("{","{'").replace("}","}")
    items.append(eval(line))


def workItem(workflow, item, target):
    print("Starting",item, "with target",target)
    for flow in workflow[target]:
        print(item, flow)
        if flow=='A': 
            accepted.append(item)
            break
        if flow=='R': 
            rejected.append(item)
            break
        if flow in workflow:
            workItem(workflow,item,flow)
            return
        else:
            if ":" not in flow: raise Exception("Not a valid flow?")
            rule, target = flow.split(":")
            rule = re.sub("([xmas])([<>])", "item['\\1']\\2",rule)
            if eval(rule):
                if target=="A":
                    accepted.append(item)
                    return
                if target=='R': 
                    rejected.append(item)
                    return
                workItem(workflow,item,target)
                return
            
accepted = []
rejected = []
for item in items:
    workItem(workflow, item, 'in')

print(len(accepted))
value = 0
for A in accepted:
    value += sum(A.values())
print(value)