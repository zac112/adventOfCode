from collections import deque

decryptKey=811589153
with open("data.txt") as f:
    numbers = deque([(int(x)*decryptKey,i) for i,x in enumerate(f.read().splitlines())])

rounds = 10
print("initial:",numbers)
for r in range(rounds):
    index = 0
    for index in range(len(numbers)):
        num, i = numbers.popleft()
        while i != index:
            numbers.append((num,i))
            num, i = numbers.popleft()        

        times = num%len(numbers)
        if num < 0:
            times -= len(numbers)
        numbers.rotate(-times)
        numbers.appendleft((num,i))
        
        
    print("After",r+1,numbers)
    
while True:
    numbers.rotate()
    if numbers[0][0] == 0:
        break
res = (numbers[(1000)%len(numbers)],numbers[(2000)%len(numbers)],numbers[(3000)%len(numbers)])

print("result:",res,sum([a for a,*b in res]))
