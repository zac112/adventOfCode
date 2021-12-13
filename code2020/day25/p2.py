doordata = [17115212,17807724]
carddata = [3667832,5764801]
test = 0
doorkey = doordata[test]
doorloop = 8217635
cardkey = carddata[test]
cardloop = 20035918
subject = 7

def transform(val, subject):
    val *= subject
    val %= 20201227
    return val

##v = 1
##i = 1
##while doorloop == 0 or cardloop == 0:
##    v = transform(v,subject)
##    if v == doorkey:
##        doorloop = i
##    if v == cardkey:
##        cardloop = i
##    i+=1
##print(doorloop, cardloop)

subject = cardkey
v=1
for i in range(doorloop):
    v = transform(v,subject)
print(v)

subject = doorkey
v=1
for i in range(cardloop):
    v = transform(v,subject)
print(v)
