from functools import reduce

with open('data.txt') as f:
    data = f.readline().strip()

binary = bin(int(data,base=16))[2:]
print(binary)
binary = list(binary)

class Literal():
    def __init__(self,val, version):
        self.val = int("".join(val),2)
        self.version = version

    def __repr__(self):
        version = self.version
        value = self.val
        return f"Literal {value=}, {version=}"

    def getSubitems(self):
        return []

    def operate(self):
        return self.val
    
class Operator():
    def __init__(self,typeId, packets, version):
        self.id = typeId
        self.version = version
        self.packets = packets
        
    def __repr__(self):
        version = self.version
        typeId = self.id
        item = self.packets
        res = f"Operator {typeId=}"
        res += "\n {"+"\n".join([repr(x) for x in item])+"}\n"
        res += f"{version=}"
        return res

    def getSubItems(self):
        return self.packets
    
class SumPacket(Operator):
    def operate(self):
        return reduce(lambda a,b:a+b.operate(),self.getSubItems(),0)

class ProductPacket(Operator):
    def operate(self):
        return reduce(lambda a,b:a*b.operate(),self.getSubItems(), 1)

class MinimumPacket(Operator):
    def operate(self):        
        return min([x.operate() for x in self.getSubItems()])

class MaximumPacket(Operator):
    def operate(self):
        return max([x.operate() for x in self.getSubItems()])

class GTPacket(Operator):
    def operate(self):
        items = self.getSubItems()
        return 1 if items[0].operate() > items[1].operate() else 0
        
class LTPacket(Operator):
    def operate(self):
        items = self.getSubItems()
        return 1 if items[0].operate() < items[1].operate() else 0

class EQPacket(Operator):
    def operate(self):
        items = self.getSubItems()
        return 1 if items[0].operate() == items[1].operate() else 0
    
def getOperator(typeId, packets, version):
    if typeId == 0:
        return SumPacket(typeId, packets, version)
    if typeId == 1:
        return ProductPacket(typeId, packets, version)
    if typeId == 2:
        return MinimumPacket(typeId, packets, version)
    if typeId == 3:
        return MaximumPacket(typeId, packets, version)
    if typeId == 5:
        return GTPacket(typeId, packets, version)
    if typeId == 6:
        return LTPacket(typeId, packets, version)
    if typeId == 7:
        return EQPacket(typeId, packets, version)
    
def parsePacket(binary):
    def readbits(num):
        return "".join([binary.pop(0) for _ in range(num)])

    def parseLiteral():
        subpacket = []
        while (t := readbits(5))[0] == '1':
            subpacket += t[1:]
        subpacket += t[1:]
        return Literal(subpacket, version)
    
    version = int(readbits(3), 2)
    packetType = int(readbits(3), 2)
    if packetType==4:
        return parseLiteral()
    else:
        lengthID = readbits(1)
        packets = []
        if lengthID == '0':
            subpacketLength = int(readbits(15), 2)
            subpacketbits = list(readbits(subpacketLength))
            while subpacketbits:
                packets.append(parsePacket(subpacketbits))
        else:
            subpackets = int(readbits(11), 2)
            for packet in range(subpackets):
                packets.append(parsePacket(binary))

        return getOperator(packetType, packets, version)
                 
packet = parsePacket(binary)
print(packet.operate())
        
        
    

    
