import sys
import globalvar
import json
import parser2


def top(stack):
    if stack:
        return stack[-1]   
    else:
        return None
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
    symboltostate = {'H': 'q11', 'J':'q12', 'K':'q14', 'L':'q16', 'M': 'q18', 'N':'q20', 'U':'q33', 'V':'q34', 'W':'q35', 'X':'q40', 'F':'q96', 'P':'q96', 'T':'q96'}
    if input in rules[currState]:
        if top(stack) in rules[currState][input]:
            if input == '"' and top(stack) == 'I' and currState!='q98' and currState!='q55' and currState != 'q95' and currState != 'q82' and currState != 'q79' and currState != 'q84' and currState != 'q86' and currState != 'q26' and currState != 'q23' and currState != 'q48' and currState != 'q89' and currState != 'q88' and currState != 'q73' and currState != 'q74' and currState != 'q75' and currState != 'q76' and currState != 'q77' and currState != 'q61' and currState != 'q63' and currState != 'q62' and currState != 'q51' and currState != 'q55' and currState != 'q73' and currState != 'q65' and currState != 'q68' and currState != 'q69' and currState != 'q93':
                topnow = top(stack)
                stack.pop()
                if top(stack) in symboltostate:
                    globalvar.currstate = symboltostate[top(stack)] 
                else:
                    stack.append(topnow)
                    # print(currState, end="")
                    # print(top(stack))
                    globalvar.currstate = rules[currState][input][top(stack)][0] # currState
                    # push into stack
                    if rules[currState][input][top(stack)][1] == 'eps': # kalo eps berati di pop
                        globalvar.stack.pop()
                    elif len(rules[currState][input][top(stack)][1]) == 2: # kalo len = 2, berati ada yang di push
                        globalvar.stack.append(list(rules[currState][input][top(stack)][1])[0])
            else:
                globalvar.currstate = rules[currState][input][top(stack)][0] # currState
                # push into stack
                if rules[currState][input][top(stack)][1] == 'eps': # kalo eps berati di pop
                    globalvar.stack.pop()
                elif len(rules[currState][input][top(stack)][1]) == 2: # kalo len = 2, berati ada yang di push
                    globalvar.stack.append(list(rules[currState][input][top(stack)][1])[0])
        else: # gak ada di fungsi transisi
            return True
    else: # gak di fungsi transisi
        return True
def readTxt(file_path):
    content = open(file_path, 'rt')
    i = 0
    for line in content:
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
def readHTML(file_path):
    parser2.pathindex = file_path
    parser2.pathlowerindex = f"{file_path[0:-5]}lower.html"
def run():
    if len(sys.argv) != 3:
        print("Masukkan pyton3 main.py file.txt file.html")
        sys.exit(1)

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    if arg1.lower().endswith('.txt') and arg2.lower().endswith('.html'):
        readTxt(arg1)
        readHTML(arg2)
    else:
        print("Salah masukkin")
        sys.exit(1)

    # if __name__ == "__main__":
    #     run()

run()
parser2.parse(parser2.pathindex, parser2.pathlowerindex)
rules = rulesprocess()
input = parser2.arr
input.reverse()
while True:
    stack = globalvar.stack
    currState = globalvar.currstate
    # print(currState, end="")
    # print(top(stack), end="")
    # print(top(input))
    if currState == 'qf':
        print("\nAccepted\n")
        break
    selesai = process(currState, input[-1], stack)
    if selesai == True:
        keys = list(rules[currState])
        print()
        print("Syntax Error")
        print("Expected: ", end="")
        for x in keys:
            if x != keys[-1]:
                if x[0] == '*':
                    print(f"{x[1:]} or", end=" ")
                else:
                    print(f"{x} or", end=" ")
            else:
                if x[0] == '*':
                    print(f"{x[1:]}", end=" ")
                else:
                    print(f"{x}", end=" ")
        print(f"but get {input[-1]} instead\n")
        break
    input.pop()

# jsonstring = json.dumps(rules['q7'], indent=4)
# print(jsonstring)
