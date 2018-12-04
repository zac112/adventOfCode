area = []

#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
events = []
with open("../../data/4.txt", "r") as f:
    for line in f:
        events.append(line[:-1])

events.sort()

#times: [guardid : [minutesAsleep]]
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
        times[guardId][fallsAsleepTime:wakesupTime] = [x+1 for x in times[guardId][fallsAsleepTime:wakesupTime]]
        continue
    
#guard, minute, value
mostSleepyOnTheSameMinute = (0,0,0)
for guard in times:
    if mostSleepyOnTheSameMinute[2] < max(times[guard]):
        mostSleepyOnTheSameMinute = (guard, times[guard].index(max(times[guard])) ,max(times[guard]))

print "Sleepiest guard:", mostSleepyOnTheSameMinute[0]
print "Sleepiest minute:", mostSleepyOnTheSameMinute[1]
print "Key:",mostSleepyOnTheSameMinute[0]*mostSleepyOnTheSameMinute[1]


