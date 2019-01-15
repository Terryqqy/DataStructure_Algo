"""
Leetcode 282 Expression Add operator
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they prevuate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
"""
ipt is the input number
tgt is the target value
expr is the expression to return 
pos is the position of last fucked number
prev is the value of former number group
curr is the result of current operation
"""
def DFS(ipt,tgt, expr, pos, prev, curr, opt):
    if pos == len(ipt):#where we need to end
        if tgt == prev:
            opt.append(expr)
        return
    for i in range(pos,len(ipt)):
        if i != pos and ipt[pos] ==  '0': #if the start is 0 then we stop this one. 08 09 074 like this
            break
        now = int(ipt[pos:i+1])
        if pos == 0:
            DFS(ipt,tgt, str(now) , i+1, now, now, opt)
        else:
            DFS(ipt, tgt, expr + "+" + str(now), i+1, prev + now, now, opt)
            DFS(ipt, tgt, expr + "-" + str(now), i+1, prev - now, now, opt)
            DFS(ipt, tgt, expr + "*" + str(now), i+1, prev - curr + curr*now, curr * now, opt)

opt = []
a = "105"
DFS(a, 5, "", 0, 0, 0,opt)
print(opt)

        
