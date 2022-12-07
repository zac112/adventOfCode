def readinput():
    with open("data.txt") as f:
        commands = f.read().split("\n")[::-1]
        while commands:
            command = commands.pop()
            files = []
            while not command.startswith("$"):
                files.append(command)
                if commands:
                    command = commands.pop()
                else:
                    break
            if files: yield files
            yield command.split(" ")[1:]             
                
filesystem = {}
def explore(fs, userinput):    
    for cmd in userinput:
        if cmd[0]=='cd':
            if cmd[1]=='..':
                return
            else:
                newdir = fs.setdefault(cmd[1], {})
                explore(newdir,userinput)
        if cmd[0]=='ls':
            for file in next(userinput):
                f_type, f_name = file.split(" ")
                try:
                    size=int(f_type)
                    fs[f_name] = size
                except:
                    fs.setdefault(f_name,{})

def getSizes(fs,sizes, path=[]):
    size = 0
    for k,v in fs.items():
        if isinstance(v,dict):
            path.append(k)
            sizes["/".join(path)] = getSizes(v,sizes, path)
            size += sizes["/".join(path)]
            path.pop()
        else:
            size += v
    return size

explore(filesystem, readinput())
#print(filesystem)

dirsizes = {}
getSizes(filesystem,dirsizes)
#print(dirsizes)

smalls = [v for k,v in dirsizes.items() if v <= 100000]
result = sum(smalls)
print(result)
