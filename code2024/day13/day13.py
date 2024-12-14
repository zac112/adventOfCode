import numpy as np
import re
from itertools import batched

tokens_p1 = 0
tokens_p2 = 0
with open("data.txt") as f:
    for s in batched(f.read().split("\n"),n=4):
        line = "".join(s)
        pattern = ".*A: X([+-]\d+), Y+([+-]\d+).* B: X([+-]\d+), Y([+-]\d+).*ze: X=([+-]?\d+), Y=([+-]?\d+)"
        ax,ay,bx,by,px,py = map(int,re.findall(pattern,line)[0])
        closeEnough = lambda a: abs(a-int(a+0.09))<0.01

        a = np.array([[ax,bx],[ay,by]])
        b = np.array([px,py])
        x = np.linalg.solve(a,b)                
        if closeEnough(x[0]) and closeEnough(x[1]):            
            tokens_p1 += 3*x[0]+x[1]

        a = np.array([[ax,bx],[ay,by]])
        b = np.array([px+10000000000000,py+10000000000000])
        x = np.linalg.solve(a,b)
        if closeEnough(x[0]) and closeEnough(x[1]):            
            tokens_p2 += 3*x[0]+x[1]

print("Part 1:",tokens_p1)
print("Part 2:",tokens_p2)
