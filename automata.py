import globalvar
import json

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
            globalvar.rulestxt.append(line.rstrip('\n').split(" "))

readTxt("pda.txt")
# print(globalvar.state)
# print(globalvar.insymbol)
# print(globalvar.stasymbol)
# print(globalvar.currstate)
# print(globalvar.stack)
# print(globalvar.final)
# print(globalvar.sta_str)
# print(globalvar.rulestxt)

def rulesprocess():
    rules = {}
    rules[globalvar.rulestxt[0][0]] = {globalvar.rulestxt[0][1] : {globalvar.rulestxt[0][2] : {globalvar.rulestxt[0][3]: globalvar.rulestxt[0][4]}}}
    for i in range(len(globalvar.rulestxt)):
        if globalvar.rulestxt[i][0] in rules:
            if globalvar.rulestxt[i][1] in rules[globalvar.rulestxt[i][0]]:
                rules[globalvar.rulestxt[i][0]][globalvar.rulestxt[i][1]][globalvar.rulestxt[i][2]] =  {globalvar.rulestxt[i][3]:globalvar.rulestxt[i][4]}
            else: 
                rules[globalvar.rulestxt[i][0]][globalvar.rulestxt[i][1]] =  {globalvar.rulestxt[i][2] : {globalvar.rulestxt[i][3]:globalvar.rulestxt[i][4]}}
        else:
            rules[globalvar.rulestxt[i][0]] = {globalvar.rulestxt[i][1] : {globalvar.rulestxt[i][2] : {globalvar.rulestxt[i][3]:globalvar.rulestxt[i][4]}}}
    return rules
rules = rulesprocess()
currState = globalvar.currstate
input = globalvar.insymbol
stacksymbol = globalvar.stasymbol
jsonstring = json.dumps(rules, indent=4)
print(jsonstring)
def process(currState, input, stacksymbol):
    print()