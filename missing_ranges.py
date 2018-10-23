"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)].
"""
def missing_ranges(ipt,lowvalue, highvalue):
    out = []
    for i in range(len(ipt)):
        if i != len(ipt)-1:
            if ipt[i] > lowvalue:
                out.append((lowvalue, ipt[i]-1))

                

