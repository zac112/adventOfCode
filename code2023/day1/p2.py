import re

with open('data.txt') as f:
    data = f.readlines()

sum = 0
digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
for line in data:
    g = "(\\d|one|two|three|four|five|six|seven|eight|nine)"
    n1 = re.match(f"^.*?{g}",line).group(1)
    n2 = re.match(f"^.*{g}",line).group(1)
    nums = filter(lambda a:a is not None, [n1, n2])
    nums = map(lambda a: str(digits.index(a)) if a in digits else a, nums)
    sum += int("".join(nums))

print(sum)
