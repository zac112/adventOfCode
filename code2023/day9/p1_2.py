from itertools import pairwise

def extrapolate(series, forward):
    newSeries = [b-a for a,b in pairwise(series)]    
    zeroes = (v==0 for v in newSeries)
    match all(zeroes), forward:
        case True, _:       return 0
        case False, True:   return newSeries[-1]+extrapolate(newSeries, forward)
        case False, False:  return newSeries[0]-extrapolate(newSeries, forward)

with open("data.txt") as f:
    data = f.read().splitlines()
    data = [[int(x) for x in line.split(" ")] for line in data]

backwards = 0
forwards = 0
for values in data:
    values.append(values[-1]+extrapolate(values, True))
    values.insert(0,values[0]-extrapolate(values, False))        
    backwards += values[0]
    forwards += values[-1]
    print(values)    
    
print(backwards, forwards)