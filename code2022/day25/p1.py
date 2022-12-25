digits = {'=':-2,
          '-':-1,
          '0':0,
          '1':1,
          '2':2}
snafus = {b:a for a,b in digits.items()}

def toDecimal(snafu):    
    return sum([digits[str(x)]*(5**i) for i,x in enumerate(snafu[::-1])])

def toBase(n,target):
    if n == 0: return [0]
    return toBase(n//target,target)+[n%target]

def toSnafu(n):
    res = toBase(n,5)
    tooBig = lambda a:a>=3
    while any(map(tooBig,res)):
        for i,n in enumerate(res):
            if tooBig(n):
                res[i-1] += 1
                res[i] -= 5
    if res[0]==0: del res[0]
    return "".join([snafus[n] for n in res])

with open("data.txt") as f:
    total = sum(toDecimal(line) for line in f.read().splitlines())
    print("Total:",total)
    print(toSnafu(total))
    
