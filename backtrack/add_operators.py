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
def DFS(ipt,tgt, expr, pos, prev, curr):
    for i in range(

        
