from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        if self.prev == None:
            p = "None"
        else:
            p = str(self.prev.data)

        if self.next == None:
            n = "None"
        else:
            n = str(self.next.data)
            
        #return(str(self.data)+" ["+p+","+n+"]")
        return(str(self.data))
            
class Cups:   

    def __init__(self, iterable):
        self.head = Node(iterable[0])
        self.tail = self.head
        self.length = 1
        self.memory = {self.head.data:self.head}
        for x in iterable[1:]:
            self.append(x)
        #print(self.length, len(iterable))

    def index(self, data):
        n = self.head
        i = 0
        #print("indexing",data)
        #print(self)
        while n.data != data:
            #print("index",data,n.data)
            n = n.next
            i += 1
        return i

    def append(self, data):
        self.insertTail(data)

    def insertHead(self,data):
        x = Node(data)
        x.next = self.head
        self.head.prev = x
        self.head = x
        self.length +=1
        self.memory[data] = x

    def popHead(self):        
        t = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -=1
        del self.memory[t.data]
        return t.data

    def popTail(self):
        t = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -=1
        del self.memory[t.data]
        return t.data
        
    def insertTail(self,data):
        x = Node(data)
        self.tail.next = x
        x.prev = self.tail
        self.tail = x
        self.length +=1
        self.memory[data] = x
        #print("tail",self.tail,self.tail.next,self.tail.prev)

    def insertAfter(self, val, data):
        x = Node(data)
        #print("ins after",self.memory[val],data)
        #print(self.tail)
        if self.memory[val] == self.tail:
            self.insertTail(data)
            return

        n = self.memory[val].next
        self.length +=1        
        
        x.next = n
        x.prev = n.prev
        
        n.prev.next = x
        n.prev = x
        #print(self)
        self.memory[data] = x
        
    
    def insert(self, index, data):
        x = Node(data)
        #print("insert to",index,data,self.length)
        #print(self)
        if index > self.length:
            self.insertTail(data)
            return
        
        if index <= 0:
            self.insertHead(data)
            return

        n = self.head
        for i in range(index):
            n = n.next
            if n == None:                
                self.insertTail(data)
                return
                #break
                

        #n = n.prev
        #if n.next == None:                
        #    self.insertTail(data)
        #    return

        self.length +=1
        x.next = n
        x.prev = n.prev
        
        n.prev.next = x
        n.prev = x
        #print(self)
        self.memory[data] = x

    def pop(self, index):
        #print("popping",index,len(self))

        #index = index%self.length
        #print("popping",index,len(self))
        
        if index <= 0:
            return self.popHead()
            
        n = self.head
        for i in range(index):
            n = n.next
            if n == None:
                return self.popTail()

        #print(n)
        if n.next == None:
            return self.popTail()

        if n.prev == None:
            return self.popHead()
        
        n.prev.next = n.next
        n.next.prev = n.prev
        
        self.length -=1
        #print("pop",index,":",n)
        #print(self)
        del self.memory[n.data]
        return n.data

    def popNext(self, node):
        #print("Popnext",node)
        #print(self.tail)
        if node == self.tail:
            return self.popHead()
        if node.next == self.tail:
            return self.popTail()
        
        n = node.next        
        node.next = n.next
        if n.next != None:
            n.next.prev = node
        
        self.length -=1
        #print("pop",index,":",n)
        #print(self)
        del self.memory[n.data]
        return n.data

    def __len__(self):
        return self.length

    def __getitem__(self, i):
        n = self.head
        for x in range(i):
            n = n.next
        return n.data
            
    def __str__(self):
        n = self.head
        res = str(n)
        n = n.next
        while n != None:
            res += ","+str(n)
            n = n.next
        return res

    def getAsList(self):
        res = []
        n = self.head
        while n != self.tail:
            res.append(n.data)
            n = n.next
        res.append(n.data)
        return res

data = "318946572"
test = "389125467"
d = data

maxval = 10**6
#maxval = 9
mil = list(range(1,maxval+1))
#mil = list(range(0))
print("mil")
mil[:len(d)] = list(map(int,d))

print("dd len:",len(mil))
cups = Cups(mil)
#cups =Cups(list(map(int,data)))

turns = 10**7
current = list(map(int,d))[0]

numCups = 3

allCups = [cups]
print("Cups created")
#print(cups)

print("----")
    
for i in range(turns):
    #print(i+1)
    if i%1000000==0:
        print(i)
    #print(cups)
    #cuplist, index = getIndex(i)        
    #turnCups = allCups[cuplist]

    removed = []
    for n in range(3):
        #l,ii = getIndex(cups.index(current)+1)        
        #print("before pop",ii,cups)
        removed.append(cups.popNext(cups.memory[current]))
        #print("after pop",cups)

    #print(cups,";",current,removed)
    
    destination = current -1
    while destination <= 0 or destination in removed:
        
        if destination <= 0:
            destination = maxval
            continue
        destination -= 1
                    
    #destination = cups.index(destination)

    #print(" cur:",current,"\n rem:",removed,"\n dest:", destination)
    
    for x in removed[::-1]:
        cups.insertAfter(destination,x)
        #cups.insert(destination+1,x)

    #current = cups[(cups.index(current)+1)%len(cups)]
    current = cups.memory[current].next
    if current == None:
        current = cups.head
    current = current.data

print("Done")
#print(cups)
c = cups.getAsList()
c = c+c
#print(c)
i = c.index(1)
print(c[i+1],c[i+2],c[i+1]*c[i+2])
#print(cups.memory[1].next.data,cups.memory[1].next.next.data)
    
#high 501501*230019 = 115354758519
