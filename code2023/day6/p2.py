from functools import reduce
class Race:    
    def __init__(self, time, distance) -> None:
        self.time = time
        self.distance = distance

races = [Race(41667266,244104712281040)]

def win(race):
    waystoWin = 0
    for t in range(race.time):
        distance = (race.time-t)*t
        if distance > race.distance:
            waystoWin += 1
    return waystoWin


total = reduce(lambda a,b:a*b,map(win,races),1)
print(total)