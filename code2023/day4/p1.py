import re
with open("data.txt") as f:
    data = f.read().split("\n")

score = 0
for card in data:
    winNums,nums = card.split(":")[1].split("|")
    
    empty = lambda a:len(a.strip())>0
    winNums = set(map(int, filter(empty, winNums.split(" "))))
    nums = set(map(int, filter(empty, nums.split(" "))))
    score += int(2**(len(winNums.intersection(nums))-1))

print(score)




