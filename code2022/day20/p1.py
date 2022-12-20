from collections import deque

with open("data.txt") as f:
    numbers = deque([(int(x),i,False) for i,x in enumerate(f.read().splitlines())])
    orig = list(numbers)

index = 0
for index in range(len(numbers)):
    num, i, swapped = numbers.popleft()
    while i != index:
        numbers.append((num,i,swapped))
        num, i, swapped = numbers.popleft()        

    numbers.rotate(-num)
    numbers.appendleft((num,i,True))
    numbers.rotate(num)

print(numbers)
while True:
    numbers.rotate()
    if numbers[0][0] == 0:
        break
res = (numbers[(1000)%len(numbers)],numbers[(2000)%len(numbers)],numbers[(3000)%len(numbers)])

print("result:",res,sum([a for a,*b in res]))
