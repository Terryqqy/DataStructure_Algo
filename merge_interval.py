"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

"""
my method is from youtube 
I will take the head and tail of input arrays and sort them in accending order
then check the tail and head to see if overlap 
if so we pop out the tail head then move on
the compexity is O(n)
"""
def merge_interval(intv):
    head, tail = [],[]
    for eachinterv in intv:
        head.append(eachinterv[0])
        tail.append(eachinterv[1])
    head.sort()
    tail.sort()
    i = 0
    while i < len(head)-1:
        if tail[i] >= head[i+1]:
            tail.pop(i)
            head.pop(i+1)
        else:
            i+=1
    out = []
    for i in range(len(head)):
        temp = [head[i],tail[i]]
        out.append(temp)
    return out
#a = [[1,3],[2,6],[8,10],[15,18]]
a = [[1,5],[2,6],[4,7],[5,6]]
print(merge_interval(a))
