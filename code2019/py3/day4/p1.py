def matches(i):
    digits = 0
    pw = str(i)
    if len(pw) != 6:
        return False

    for c in range(0,len(pw)-1):
        if pw[c]>pw[c+1]:
            return False
        
    for c in pw:
        digits += len([x for x in pw if x==c])
    if digits == len(pw):
        return False

    return True

low=134792
high=675810

found = 0
for i in range(low,high+1):
    if matches(i):
        found += 1

print(found)
