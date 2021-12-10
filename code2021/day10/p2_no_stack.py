from functools import reduce
import re

with open('data.txt') as file:
    lines = file.readlines()

print(lines)

pairs={
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'}
syntaxMapping={
    ')':3,
    ']':57,
    '}':1197,
    '>':25137}
autocompleteMapping={
    ')':1,
    ']':2,
    '}':3,
    '>':4}

errors = []
autocompleteScores = []
for line in lines:
    print(line.strip())
    while (reline := re.sub('(\(\)|\[\]|\{\}|<>|\n)',"",line)) != line:
        line = reline

    starts = "([{<"
    ends = ")]}>"
    error = False
    for i,x in enumerate(starts):
        for y in ends:
            if x+y in line:
                error = True
                print("Syntax error: got",y,"expected",ends[i])
                errors.append((y,ends[i]))
                
    if not error:
        autocomplete = list(map(lambda a:pairs[a],line[::-1]))
        print("Autocompleted line:","".join(autocomplete))
        autocomplete = list(map(lambda a:autocompleteMapping[a],autocomplete))                
        autocompleteScores.append(reduce(lambda a,b:a*5+b,autocomplete))
        
print("Syntax error score",sum(map(lambda a:syntaxMapping[a[0]],errors)))
print("AC error score",sorted(autocompleteScores)[len(autocompleteScores)//2])
