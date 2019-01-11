"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""
def twosum(ipt,tgt):
    output =[]
    for i in range(len(ipt)):
        if i!= len(ipt)-1:
            for j in range(i+1,len(ipt)):
                result = ipt[i]+ipt[j] 
                if result == tgt:
                    output.append((i,j))
    return output

a = [2,5,6,7,8]
print(twosum(a, 8))


