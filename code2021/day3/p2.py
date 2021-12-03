from collections import Counter 

with open('data.txt') as f:
    data = [x.strip() for x in f.readlines()]

def sieve(data, index, comparison_func, tiebreaker):
    print(data)
    if len(data) ==1:
        return data
    
    bits = []
    bit = 0
    c = Counter([element[index] for element in data])
    print(c)
    if c['1'] == c['0']:
        bit = tiebreaker
    else:
        bit = comparison_func(c, key=lambda a:c[a])
    bits.append(bit)
    
    #bit = int("".join(bits), base=2)
    newData = [x for x in data if x[index] == bit]
    
    return sieve(newData, index+1, comparison_func, tiebreaker)
    
oxygen = sieve(data, 0, max, "1")
co2 = sieve(data, 0, min, "0")

print(int("".join(oxygen), base=2)*int("".join(co2), base=2))
