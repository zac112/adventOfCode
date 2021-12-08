with open('data.txt') as file:
    def decode(line):
        signal, output = line.split(' | ')
        return (signal,output[:-1])
    
    signal = {decode(line) for line in file.readlines()}

print(signal)

output = [x for x in map(lambda a:a[1].split(' '),signal)]
easyNums = [x for signal in output for x in signal if len(x) in [2,3,4,7]]

#print(easyNums)
print(len(easyNums))
