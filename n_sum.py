"""
Given an array of n integers, are there elements a, b, .. , n in nums
such that a + b + .. + n = target?
Find all unique n-tuplets in the array which gives the sum of target.
Example:
    basic:
        Given:
            n = 4
            nums = [1, 0, -1, 0, -2, 2]
            target = 0,
        return [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""


def n_sum(ipt, resultnumber, target):
    """
    Get the total number of combination of the possible results.
    """
    output = []
    eachlevel(ipt,[],resultnumber,output, target)
    """
    To iterate all possible result and store in the dict
    """
   
def eachlevel(ipt_notvisited, ipt_visited, level, output, target):
    if level == 0 :
        sumofvisited = sum(ipt_visited)
        if sumofvisited == target:
            output.append(ipt_visited)
            print(sumofvisited)
    else:
        for i in range(len(ipt_notvisited)):
            tempNotVist = ipt_notvisited[i::]
            tempVist = ipt_visited[::]
            tempVist.append(tempNotVist.pop(0))
            if len(tempNotVist) >= level - 1:
                eachlevel(tempNotVist, tempVist, level-1, output, target)
    return 0

nums = [1, 0, -1, 0, -2, 2]
#nums = [1,2,3]

n_sum(nums, 4, 0)







    

        
