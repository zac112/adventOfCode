class Computer:
        
    def __init__(self, data, program_input=None, onFinished=None, onOutput=None):
        self.pointer = 0
        self.onFinished = onFinished
        self.onOutput = onOutput
        
        self.input_data = {
            "data": program_input,
            "index": 0
        }
        self.commands = {
            1:self.add,
            2:self.mult,
            3:self.read,
            4:self.output,
            5:self.jit,
            6:self.jif,
            7:self.lt,
            8:self.eq        
            }
        self.readModes = {
            0: lambda a: self.access(a),
            1: lambda a: a
        }
        self.paramCount={
            self.add:3,
            self.mult:3,
            self.read:1,
            self.output:1,
            self.jit:2,
            self.jif:2,
            self.lt:3,
            self.eq:3
            }
        self.data = [[int(x)] for x in data]

    def read(self, indexes):
        if self.input_data["data"] == None:
            val = int(input(str(indexes)+"Input value:"))
        else:
            val = self.input_data["data"][self.input_data["index"]]
            self.input_data["index"] += 1
            
        self.write(indexes[0],val)
        self.pointer += 2

    def output(self, indexes):
        self.output = self.access(indexes[0])
        self.pointer += 2
        if self.onOutput != None:
            self.onOutput(self.output)
        
    def add(self, indexes):
        i1,i2,i3 = indexes
        self.write(i3, self.access(i1)+self.access(i2))
        self.pointer += 4

    def mult(self, indexes):
        i1,i2,i3 = indexes
        self.write(i3, self.access(i1)*self.access(i2))
        self.pointer += 4

    def jit(self, indexes):
        i1,i2 = indexes
        
        if self.access(i1) != 0:
            self.pointer = self.access(i2)
        else:
            self.pointer += 3

    def jif(self, indexes):
        i1,i2 = indexes
        
        if self.access(i1) == 0:
            self.pointer = self.access(i2)
        else:
            self.pointer += 3
            
    def lt(self, indexes):
        i1,i2,i3 = indexes
        if self.access(i1) < self.access(i2):
            self.write(i3, 1)
        else:
            self.write(i3, 0)
        self.pointer += 4

    def eq(self, indexes):
        i1,i2,i3 = indexes

        if self.access(i1) == self.access(i2):
            self.write(i3, 1)
        else:
            self.write(i3, 0)
        self.pointer += 4

    def access(self, index):
        return self.data[index][0]

    def write(self, index, val):
        self.data[index][0] = val

    def receiveInput(self,value):
        self.input_data["data"].append(value)
        self.run()
        
    def decodeParams(self, opcode, modes):
        ptr = self.pointer
        return [self.readModes[int(modes[x])](ptr+x+1) for x in range(self.paramCount[opcode])]        
    
    def execute(self,instruction):        
        instruction = str(instruction).rjust(5,"0")
        command = self.commands[int(instruction[-2:])]
        params = self.decodeParams(command, instruction[-3::-1])
        command(params)

    def run(self):
        while self.access(self.pointer) != 99:
            instruction = self.access(self.pointer)
            self.execute(instruction)

        if self.onFinished != None:
            self.onFinished(self.output)
            self.onFinished = None
        return self.output
