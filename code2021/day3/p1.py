from collections import Counter 

with open('data.txt') as f:
    data = [x.strip() for x in f.readlines()]

gamma = []
epsilon = []

index = 0
for index in range(len(data[0])):    
    c = Counter([element[index] for element in data])
    gamma.append(max(c, key=lambda a:c[a]))
    epsilon.append(min(c, key=lambda a:c[a]))
        
print(int("".join(gamma), base=2)*int("".join(epsilon), base=2))
