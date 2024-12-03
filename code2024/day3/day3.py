import re
import functools

with open("data.txt") as f:
    memory = f.read()

muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)",memory)
print("Sum of multiplications:",sum(map(lambda a:int(a[0])*int(a[1]),muls)))

#part 2
muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)|(do)\(\)",memory)
productsum = 0
multiplier = 1

for a,b,dont,do in muls:
    if do:     multiplier = 1
    elif dont: multiplier = 0
    else:      productsum += int(a)*int(b)*multiplier

print("Sum of multiplications:",productsum)

