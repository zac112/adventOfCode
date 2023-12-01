import re

with open('data.txt') as f:
    data = f.readlines()

sum = 0
for line in data:
    nums = re.findall("\\d",line)
    sum += int(nums[0]+nums[-1])

print(sum)
