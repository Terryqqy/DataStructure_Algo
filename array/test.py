"""
def out(a):
    if a > 0:
        print("fuck")
    else:
        print("fuck me")
    return a 

a = 10
print(out(a))
"""
def limit(arr, min_lim = None, max_lim = None):
    result = []
    if min_lim == None:
        for i in arr:
            if i <= max_lim:
                result.append(i)
    elif max_lim == None:
        for i in arr:
            if i >= min_lim:
                result.append(i)
    else:
        for i in arr:
            if i >= min_lim and i <= max_lim:
                result.append(i)

    return result
a = [1,2,3,4,6]
print(limit(a))
