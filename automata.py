import globalvar

def readTxt(filename):
    lines = open(filename, 'rt')
    i = 0
    for line in lines:
        if i == 0:
            globalvar.state.extend((line.rstrip('\n').split(" ")))
            i+=1
        elif i == 1:
            globalvar.insymbol.extend((line.rstrip('\n').split(" ")))
            i+=1
        elif i == 2:
            globalvar.stasymbol.extend((line.rstrip('\n').split(" ")))
            i+=1
        elif i == 3:
            globalvar.currstate = line.rstrip('\n')
            i+=1
        elif i == 4:
            globalvar.stack.extend((line.rstrip('\n').split(" ")))
            i+=1
        elif i == 5: 
            globalvar.final = line.rstrip('\n')
            i+=1
        elif i == 6:
            globalvar.sta_str = line.rstrip('\n')
            i+=1
        else:
            globalvar.rules.append(line.rstrip('\n').split(" "))

readTxt("a.txt")
print(globalvar.state)
print(globalvar.insymbol)
print(globalvar.stasymbol)
print(globalvar.currstate)
print(globalvar.stack)
print(globalvar.final)
print(globalvar.sta_str)
print(globalvar.rules)

dic = {}
dic[globalvar.rules[0][0]] = {globalvar.rules[0][1] : {globalvar.rules[0][2] : {globalvar.rules[0][3]: globalvar.rules[0][4]}}}
for i in range(len(globalvar.rules)):
    if globalvar.rules[i][0] in dic:
        if globalvar.rules[i][1] in dic[globalvar.rules[i][0]]:
            dic[globalvar.rules[i][0]][globalvar.rules[i][1]][globalvar.rules[i][2]] =  {globalvar.rules[i][3]:globalvar.rules[i][4]}
        else: 
            dic[globalvar.rules[i][0]][globalvar.rules[i][1]] =  {globalvar.rules[i][2] : {globalvar.rules[i][3]:globalvar.rules[i][4]}}
    else:
        dic[globalvar.rules[i][0]] = {globalvar.rules[i][1] : {globalvar.rules[i][2] : {globalvar.rules[i][3]:globalvar.rules[i][4]}}}

print(dic)
