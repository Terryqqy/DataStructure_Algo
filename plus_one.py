"""
Given a non-negative number represented as an array of digits,
adding one to each numeral.
The digits are stored big-endian, such that the most significant
digit is at the head of the list.
Eg:
[1,2,4] -- [1,2,5]
[1,9] -- [2,0]
[9,9,9] -- [1,0,0,0]
so it is just use array to represent numbers and do plus
"""

def plus_one(ipt):
    for i in range(len(ipt)-1, -1, -1):
        if ipt[i] == 9:
            if i == 0:
                ipt[i] = 0
                ipt.insert(0,1)
            else:
                ipt[i] = 0
        else:
            ipt[i]+=1
            break
    return ipt
"""
def plus_one(digits):
    
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        summ = 0
        if i >= 0:
            summ += digits[i]
        if ten:
            summ += 1
        res.append(summ % 10)
        ten = summ // 10
        i -= 1
    return res[::-1]
"""
a = [9,9,9]
b = [1,2,3,4]
c = [1,9,2,9]
print(plus_one(a), plus_one(b), plus_one(c))



