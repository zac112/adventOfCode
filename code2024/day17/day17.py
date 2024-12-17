global computer
computer = {'A':66171486,'B':0,'C':0, 'IP':0,
            'P':[int(x) for x in '2,4,1,6,7,5,4,6,1,4,5,5,0,3,3,0'.split(",")],
            'output':[]}

operands = {
    0:lambda:0,
    1:lambda:1,
    2:lambda:2,
    3:lambda:3,
    4:lambda:computer['A'],
    5:lambda:computer['B'],
    6:lambda:computer['C'],

}
def adv(op): computer['A'] = int(computer['A']/(2**operands[op]()))
def bxl(op): computer['B'] = computer['B']^op
def bst(op): computer['B'] = operands[op]()%8
def jnz(op): computer['IP'] = (computer['IP'] if computer['A']==0 else op-2)
def bxc(op): computer['B'] = computer['B']^computer['C']
def out(op): computer['output'].append(operands[op]()%8)
def bdv(op): computer['B'] = int(computer['A']/2**operands[op]())
def cdv(op): computer['C'] = int(computer['A']/2**operands[op]())

opcodes = {
    0: lambda op:adv(op),
    1: lambda op:bxl(op),
    2: lambda op:bst(op),
    3: lambda op:jnz(op),
    4: lambda op:bxc(op),
    5: lambda op:out(op),
    6: lambda op:bdv(op),
    7: lambda op:cdv(op),
}

def runComputer():
    while 0<=computer['IP']<len(computer['P']):
        ip = computer['IP']
        opcode= computer['P'][ip]
        operand= computer['P'][ip+1]
        opcodes[opcode](operand)
        computer['IP']+=2
runComputer()
print("Part1:",",".join(map(str,computer['output'])))

#P2
possibleRegisterA = []
def findOctalBitByBit(nums):
    if len(nums) >=17:return
    global computer
    for i in range(8):
        nums[-1]=i
        a = sum(n*8**(len(nums)-e-1) for e,n in enumerate(nums))
        computer = {'A':a,'B':0,'C':0, 'IP':0,
                'P':[2,4,1,6,7,5,4,6,1,4,5,5,0,3,3,0],
                'output':[]}

        runComputer()                
        if computer['output'] == computer['P']:
            possibleRegisterA.append(a)
            return        
        if computer['output'][0] == computer['P'][-len(nums)]:
            findOctalBitByBit(nums+[0])

findOctalBitByBit([0])
print("Smallest register A:",min(possibleRegisterA))
