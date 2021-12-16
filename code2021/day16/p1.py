with open('data.txt') as f:
    data = f.readline().strip()

#data = "A0016C880162017C3686B18A3D4780"
#data = "C0015000016115A2E0802F182340"
binary = bin(int(data,base=16))[2:]
print(binary)
binary = list(binary)

class Literal():
    def __init__(self,val, version):
        self.val = int("".join(val),2)
        self.version = int(version,2)

    def __repr__(self):
        version = self.version
        value = self.val
        return f"Literal {value=}, {version=}"

    def getSubitems(self):
        return []
    
class Operator():
    def __init__(self,typeId, packets, version):
        self.id = int(typeId,2)
        self.version = int(version,2)
        self.packets = packets
        
    def __repr__(self):
        version = self.version
        typeId = self.id
        item = self.packets
        res = f"Operator {typeId=}"
        res += "\n {"+"\n".join([repr(x) for x in item])+"}\n"
        res += f"{version=}"
        return res

    def getSubitems(self):
        return self.packets
        
def parsePacket(binary):
    def readbits(binary, num):
        res = []
        for _ in range(num):
            res.append(binary.pop(0))
        return "".join(res)

    #print("Parsing","".join(binary))
    version = readbits(binary,3)
    packetType = readbits(binary,3)
    if int(packetType, base=2)==4:
        subpacket = []
        while (t := readbits(binary,5))[0] == '1':
            subpacket += t[1:]
        subpacket += t[1:]
        return Literal(subpacket, version)
    else:
        lengthID = readbits(binary,1)
        packets = []
        #print("Operator lengthID",lengthID)
        if lengthID == '0':
            subpacketLength = int(readbits(binary,15),2)
            #print("length:",subpacketLength)
            subpacketbits = list(readbits(binary, subpacketLength))
            while subpacketbits:
                packets.append(parsePacket(subpacketbits))
        else:
            subpackets = int(readbits(binary,11),2)
            #print("packets:",subpackets)
            for packet in range(subpackets):
                packets.append(parsePacket(binary))

        return Operator(packetType, packets, version)
            
            
def sumVersions(packet):
    versionsum = packet.version
    for p in packet.getSubitems():
        versionsum += sumVersions(p)
    return versionsum

packet = parsePacket(binary)
print(sumVersions(packet))
        
        
    

    
