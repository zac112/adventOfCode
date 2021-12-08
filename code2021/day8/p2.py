with open('data.txt') as file:
    def decode(line):
        signal, output = line.split(' | ')
        return (signal,output[:-1])
    
    signal = {decode(line) for line in file.readlines()}

print(signal)

def decodeSegments(signal):    
    result = []

    for entry,output in signal:
        display = {a:[] for a in 'abcdefg'}
        segments = {}
        signals = [set(x) for x in " ".join([entry,output]).split(' ')]
        
        segments[1] = [set(x) for x in signals if len(x)==2][0]
        segments[4] = [set(x) for x in signals if len(x)==4][0]
        segments[7] = [set(x) for x in signals if len(x)==3][0]
        segments[8] = [set(x) for x in signals if len(x)==7][0]

        segments[9] = [set(x) for x in signals if len(x) == 6 and len(set(x)-segments[4])==2][0]
        display['a'] = segments[7]-segments[1]        
        display['g'] = segments[9]-segments[4]-display['a']
        display['e'] = segments[8]-segments[9]
        
        segments[0] = [set(x) for x in signals if len(x) == 6 and len(set(x)-segments[7]-display['g']-display['e'])==1][0]
        segments[6] = [set(x) for x in signals if len(x) == 6 and set(x)!=segments[9] and set(x)!=segments[0]][0]
        display['d'] = segments[8]-segments[0]
        display['b'] = segments[4]-segments[1]-display['d']

        segments[3] = display['g'] | display['d'] | segments[7]                
        display['c'] = segments[8]-segments[6]
        display['f'] = segments[1]-display['c']        

        segments[5] = segments[8]-display['c']-display['e']                      
        segments[2] = segments[8]-display['b']-display['f']

        res = []        
        for x in output.split(" "):
            for key,val in segments.items():
                if set(x)==val:
                    res.append(str(key))
        result.append(int("".join(res)))
        
        #print(display)
        #print(segments)
        #print(output)
        #print(res)
                
    return result

print(sum([x for x in decodeSegments(signal)]))


    
    
