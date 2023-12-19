with open('data.txt') as f:
    data = f.read().splitlines()
    pass
    
workflow = {}
for i,line in enumerate(data):
    data[i] = '"'+line.replace("{",'":["').replace(",",'","').replace("}",'"]')
    if not line:break

lines = '{'+",".join(data[:i])+'}'
workflow = eval(lines)

accepted = []
def count(items):
    bounds = {
    'x' : [1,4000],
    'm' : [1,4000],
    'a' : [1,4000],
    's' : [1,4000],
    }
    for item in items:
        if '<' in item:
            bound = (1 if '=' in item else 0)            
            L,B = item.replace("=","").split("<")
            bound += int(B)-1
            bounds[L][1]=bound
        else:
            bound = (0 if '=' in item else 1)        
            L,B = item.replace("=","").split(">")
            bound += int(B)
            bounds[L][0]=bound    
    vals = 1
    for k,v in bounds.items():
        vals *= (v[1]-v[0]+1)

    accepted.append(vals)
    print(vals, bounds)


possibilities = 0
def createItem(workflow, item, target):
    if target=='A':
        #print(item, target)
        count(item)
        return 
    if target=='R': 
        return
    for flow in workflow[target]:
        if flow in 'A':
            #print(item, flow)
            count(item)
            continue
        if flow in 'R': 
            continue
        if flow in workflow:
            createItem(workflow,item,flow)
            continue
        else:
            rule, target = flow.split(":")
            item = list(item)+[rule]
            createItem(workflow,item,target)
            if len(item)>0:
                if "<=" in item[-1]:
                    item[-1] = item[-1].replace("<=",">")
                elif ">=" in item[-1]:
                    item[-1] = item[-1].replace(">=","<")
                elif "<" in item[-1]:
                    item[-1] = item[-1].replace("<",">=")
                elif ">" in item[-1]:
                    item[-1] = item[-1].replace(">","<=")

            
item = []
createItem(workflow, item, 'in')
print(sum(accepted))


