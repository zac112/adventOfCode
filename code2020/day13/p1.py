earliest = 1004098
busses ="23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19"

departures = busses.split(",")

for d in departures:     
    if d == "x":
        continue
    d = int(d)
    dep = 0   
    while dep < earliest:
        dep += d
    print("ID,",d,"earliest:",dep,"wait",dep-earliest)
    #print()
    #dep = earliest% int(d)
    #print(d, earliest% int(d),(int(d)-dep))
