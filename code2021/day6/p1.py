
with open("data.txt") as file:
    school = [int(x) for x in file.readline().split(',')]

#test data
#school = [int(x) for x in "3,4,3,1,2".split(',')]

for day in range(80):
    for index, fish in enumerate(school):
        school[index] -= 1
        if school[index] < 0:
            school.append(9)
            school[index] = 6
    
    #print(day+1,":",school)

print(len(school))
