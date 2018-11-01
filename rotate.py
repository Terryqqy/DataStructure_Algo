"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""

def rotate(ipt, n):
    out = []
    n = n%len(ipt)
    while(n != 0):
        out.append(ipt.pop(-1))
        n-=1
    out.reverse()
    for i in ipt:
        out.append(i)
    return out

a = [1,2,3,4,5,6,7]
print(rotate(a,3))

