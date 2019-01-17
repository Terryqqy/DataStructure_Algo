"""
WAP to take one element from each of the array add it to the target sum.
Print all those three-element combinations.


A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [2, 3, 3, 4]
target = 7


Result:
[[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 3, 3], [1, 4, 2],
 [2, 2, 3], [2, 2, 3], [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
 This one is kind of different from leetcode
 But still can use DFS
"""

def ary_sum(
