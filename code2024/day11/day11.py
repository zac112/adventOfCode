from functools import cache

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

node = None
with open('data.txt') as f:
    prev_n = None
    for i, val in enumerate([int(x) for x in f.read().split(" ")]):
        n = Node(val)
        if node == None: node = n
        if prev_n: prev_n.next = n
        prev_n = n

n = node
n_p2 = Node(node.val)

def doBlinks(blinks):
    for blink in range(blinks):
        n = node
        while n:
            if n.val == 0: n.val = 1
            elif len(str(n.val))%2==0:
                n_len = len(str(n.val))
                n_1 = str(n.val)[:n_len//2]
                n_2 = str(n.val)[n_len//2:]            
                
                n.val = int(n_1)
                n_new = Node(int(n_2))
                n_new.next = n.next
                n.next = n_new
                n = n.next
            else:
                n.val = n.val*2024
                
            n = n.next

doBlinks(25)

nodes = 0
n = node
while n:
    nodes += 1
    n = n.next
print("nodes_part1:",nodes)

#P2
@cache
def doBlinks(blinks, val):
    if blinks <= 0: return 1
    stones = 0
    if val == 0:
        stones += doBlinks(blinks-1, 1)
    elif len(str(val))%2==0:
        n_len = len(str(val))
        n1 = str(val)[:n_len//2]
        n2 = str(val)[n_len//2:]            
        
        stones += doBlinks(blinks-1,int(n1))
        stones += doBlinks(blinks-1,int(n2))
    else:
        stones += doBlinks(blinks-1, val*2024)        
    return stones

nodes = 0
n = n_p2
while n:
    nodes += doBlinks(75,n.val)
    n = n.next
print("nodes2:",nodes)
