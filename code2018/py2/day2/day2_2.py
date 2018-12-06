wantedValues = {2:0, 3:0}

def findDifferingChars(s, s1):
    result = []
    for x in range(len(s)):
        if s[x] != s1[x]:
            result.append(s[x])
    return result

strings = []
with open("../../data/2.txt", "r") as f:
    for line in f:
        strings.append(line)

for i in range(len(strings)):
    for j in range(i):
        r = findDifferingChars(strings[i], strings[j])
        if len(r) == 1:
            result = ""
            for x in range(len(strings[i])):
                if strings[i][x] == strings[j][x]:
                    result = result+ strings[i][x]
            print result
