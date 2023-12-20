class Signal:
    def __init__(self, high : bool) -> None:
        self.high = high

    def flip(self):
        self.high = not self.high

class Gate:
    def __init__(self, name, targets) -> None:        
        self.targets = targets
        self.signal = Signal(False)
        self.currSignals = {}
        self.inputs = 0
        self.activated = False
        self.name = name
        self.sending = False

    def connect(self,source):
        self.currSignals[source] = Signal(False)

    def reset(self):
        for k,v in self.currSignals.items():
            self.currSignals[k]
        self.sending = False

    def broadcast(self):
        res = []
        #if not self.activated:            
        for t in self.targets:
            t.receive(Signal(False), self)
            pulses[False] += 1   
            #print(f"{self.name}-False->{t.name}")
        #self.activated = True
        res = self.targets
        
        self.reset()
        return res
    
    def receive(self, signal, source):        
        self.currSignals[source] = signal
        self.sending = True
    
    def __repr__(self) -> str:
        return f"{self.name}->{list(map(lambda a:a.name,self.targets))}"

class FF(Gate):
    def broadcast(self):
        res = []
        if self.sending:
            res = self.targets
            for t in self.targets:
                pulse = self.signal.high
                t.receive(Signal(pulse), self)
                pulses[pulse] += 1
                #print(f"{self.name}-{pulse}->{t.name}")            
            self.activated = True
            
        self.reset()
        return res
    
    def receive(self, signal, source):
        if signal.high:return
        self.sending = True
        self.currSignals[source] = signal
        self.signal.flip()


class Inv(Gate):
    def broadcast(self):
        if True:
            for t in self.targets:
                if len(self.currSignals) == 1:
                    k = list(self.currSignals)[0]
                    pulse = not self.currSignals[k].high
                    t.receive(Signal(pulse), self)
                    pulses[pulse] += 1
                    #print(f"{self.name}-{pulse}->{t.name}")
                else:
                    sigs = self.currSignals.values()
                    newsig = not all(map(lambda a:a.high, sigs))
                    t.receive(Signal(newsig), self)
                    pulses[newsig] += 1
                    #print(f"{self.name}-{newsig}->{t.name}")
            self.activated = True
            #self.reset()
            return self.targets
        return []

with open('data.txt') as f:
    data = f.read().splitlines()
    pass

targets = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in data}

gates = {}
for gate, targets in targets.items():
    if gate[0]=="%":
        gates[gate[1:]] = FF(gate, targets.split(", "))
    elif gate[0]=="&":
        gates[gate[1:]] = Inv(gate, targets.split(", "))
    else:
        gates[gate] = Gate(gate, targets.split(", "))
    

for x in range(2):
    for name, gate in gates.items():
        for i, g in enumerate(gate.targets):
            try:
                if x==0:gate.targets[i] = gates[g]
                if x==1:g.connect(gate)
            except Exception as e:
                gate.targets[i] = Gate(str(e),"")
                print(e)

pulses = [0,0]
targets = [gates['broadcaster']]
for tick in range(1000):
    pulses[False] += 1
    while targets:
        t = targets.pop(0)
        targets.extend(t.broadcast())        
    targets = [gates['broadcaster']]
        
print(pulses, pulses[0]*pulses[1])

