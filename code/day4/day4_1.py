area = []

#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
events = []
with open("../../data/4.txt", "r") as f:
    for line in f:
        events.append(line[:-1])

events.sort()

#guard -> [minute:int][asleep:boolean]
times = {}
guardId = -1
fallsAsleepTime = 0
wakesupTime = 0
for event in events:
    if "Guard" in event:
        guardId = int(event.split("#")[1].split(" ")[0])
        continue
    if "falls" in event:
        fallsAsleepTime = int(event[event.find(":")+1:event.find("]")])
        continue
    if "wakes" in event:
        if guardId not in times:
            times[guardId] = [0 for x in range(60)]
        wakesupTime = int(event[event.find(":")+1:event.find("]")])
        print "sleeptime",guardId,wakesupTime-fallsAsleepTime
        times[guardId][fallsAsleepTime:wakesupTime] = [x+1 for x in times[guardId][fallsAsleepTime:wakesupTime]]
        continue
    
guards = []
for guard in times:
    guards.append((guard,sum(times[guard])))

guards.sort(key=lambda a : a[1], reverse=True)
sleepiestGuard = guards[0][0]
print "Sleepiest guard:", sleepiestGuard
print "Sleepiest minute:", times[sleepiestGuard].index(max(times[sleepiestGuard]))
print "Key:",sleepiestGuard*times[sleepiestGuard].index(max(times[sleepiestGuard]))


