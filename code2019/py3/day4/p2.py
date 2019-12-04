import re

def matches(i):
    pw = str(i)
    if len(pw) != 6:
        return False

    for c in range(0,len(pw)-1):
        if pw[c]>pw[c+1]:
            return False
        
    pair = False
    for c in pw:
        char = str(c);
        regex = "([^"+char+"]|k)"+char*2+"([^"+char+"]|k)"
        pair = pair or (re.search(regex,"k"+pw+"k") != None)

    if pair == False:
        return False

    return True

low=134792
high=675810

found = len([i for i in range(low,high+1) if matches(i)])

print(found)
