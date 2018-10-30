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

class Node:
    def __init__(self, data):
        self.data = data
    
    def insert(self, data, formerdata, level):
        self.

def n_sum(ipt, resultnumber, target):
    """
    Get the total number of combination of the possible results.
    """
    lenofipt = len(ipt)
    times= helper = lenofipt
    for i in range(resultnumber):
        times*=(helper-1)

    """
    To iterate all possible result and store in the dict
    """
    a = [[]]
    count = resultnumber
    while count!=0:
        for j in 
   
    eachlevel(
    

        
