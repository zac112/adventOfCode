from collections import Counter
       
with open("data.txt") as file:
    school = Counter(map(int,file.readline().split(',')))

#test data
#school = Counter(map(int,"3,4,3,1,2".split(',')))

for day in range(256):
    newSchool = {}
    for x, amount in school.items():            
        if x == 0:
            newSchool[8] = amount
            newSchool[6] = amount+newSchool.get(6,0)
        else:
            newSchool[x-1] = amount+newSchool.get(x-1,0)
    school = newSchool
    #print(day+1,":",school)

print(sum(school.values()))
