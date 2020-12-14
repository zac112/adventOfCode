data="""8
131
91
35
47
116
105
121
56
62
94
72
13
82
156
102
12
59
31
138
46
120
7
127
126
111
2
123
22
69
18
157
75
149
88
81
23
98
132
1
63
142
37
133
61
112
122
128
155
145
139
66
42
134
24
60
9
28
17
29
101
148
96
68
25
19
6
67
113
55
40
135
97
79
48
159
14
43
86
36
41
85
87
119
30
108
80
152
158
151
32
78
150
95
3
52
49"""

##data = """16
##10
##15
##5
##1
##11
##7
##19
##6
##12
##4"""

##data = """28
##33
##18
##42
##31
##14
##46
##20
##48
##47
##24
##23
##49
##45
##19
##38
##39
##11
##1
##32
##25
##35
##8
##17
##7
##9
##4
##2
##34
##10
##3"""

adapters = [int(x) for x in data.splitlines()]
adapters.append(0)
target = max(adapters)+3
adapters.append(target)
adjacency = {}
for i, source in enumerate(adapters):
    for j, adapter in enumerate(adapters):
        if i==j:
            continue
        diff = adapter-source
        if diff >=0 and diff < 4:
            adjacency.setdefault(source,[]).append(adapter)
            adjacency[source].sort()

[print(x) for x in sorted(adjacency.items(), key=lambda a:a[0])]

def search(source, memory):
    paths = 1
    if target == source:
        return paths

    path = 0
    for a in adjacency[source]:        
        if a not in memory:
            memory[a] = search(a,memory)
            print(len(adjacency)-len(memory))
        path += memory[a]

    paths *= path
    
    return paths

count = search(0,{})
print(count)
