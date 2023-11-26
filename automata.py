import globalvar
import json
import jelek

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
def top(stack):
    if stack:
        return stack[-1]   
    else:
        return None
readTxt("pda.txt")
# jsonstring = json.dumps(rules, indent=4)
# print(jsonstring)
def rulesprocess():
    rules = {}
    rules[globalvar.rulestxt[0][0]] = {globalvar.rulestxt[0][1] : {globalvar.rulestxt[0][2] : [globalvar.rulestxt[0][3],globalvar.rulestxt[0][4]]}}
    for i in range(len(globalvar.rulestxt)):
        if globalvar.rulestxt[i][0] in rules:
            if globalvar.rulestxt[i][1] in rules[globalvar.rulestxt[i][0]]:
                rules[globalvar.rulestxt[i][0]][globalvar.rulestxt[i][1]][globalvar.rulestxt[i][2]] =  [globalvar.rulestxt[i][3],globalvar.rulestxt[i][4]]
            else: 
                rules[globalvar.rulestxt[i][0]][globalvar.rulestxt[i][1]] =  {globalvar.rulestxt[i][2] : [globalvar.rulestxt[i][3],globalvar.rulestxt[i][4]]}
        else:
            rules[globalvar.rulestxt[i][0]] = {globalvar.rulestxt[i][1] : {globalvar.rulestxt[i][2] : [globalvar.rulestxt[i][3],globalvar.rulestxt[i][4]]}}
    return rules
def process(currState, input, stack):
    if input in rules[currState]:
        if top(stack) in rules[currState][input]:
            globalvar.currstate = rules[currState][input][top(stack)][0] # currState
            # push into stack
            if rules[currState][input][top(stack)][1] == 'eps': # kalo eps berati di pop
                globalvar.stack.pop()
            elif len(rules[currState][input][top(stack)][1]) == 2: # kalo len = 2, berati ada yang di push
                globalvar.stack.append(list(rules[currState][input][top(stack)][1])[0])
        else: # gak ada di fungsi transisi
            print(input)
            return True
    else: # gak di fungsi transisi
        print(input)
        return True
rules = rulesprocess()
input = jelek.arr
input.reverse()
while True:
    stack = globalvar.stack
    currState = globalvar.currstate
    print(currState, end="")
    print(top(stack))
    if currState == 'qf':
        print("diterima")
        break
    selesai = process(currState, input[-1], stack)
    if selesai == True:
        print("tidak diterima")
        break
    input.pop()