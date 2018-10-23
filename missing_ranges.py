"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)].
"""
def missing_ranges(ipt,lowvalue, highvalue):
    out = []
    for i in range(len(ipt)):
        if i != len(ipt)-1:
            if i == 0:
                out.append((lowvalue, ipt[i]-1))
            else:
                out.append((ipt[i-1]+1, ipt[i]-1))
        else:
            out.append((ipt[i-1]+1, ipt[i]-1))
            out.append((ipt[i]+1,highvalue))
    return out
"""
This one is better from Keon
"""
def missing_ranges2(arr, lo, hi):

    res = []
    start = lo

    for n in arr:

        if n == start:
            start += 1
        elif n > start:
            res.append((start, n-1))
            start = n + 1

    if start <= hi:                 # after done iterating thru array,
        res.append((start, hi))     # append remainder to list

    return res
                
a = [3, 5]
print(missing_ranges(a,1,10))
