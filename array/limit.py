"""
Sometimes you need to limit array result to use. Such as you only need the
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value
If array, Min, Max value was given, it returns array that contains values of
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.
ex) limit([1,2,3,4,5], None, 3) = [1,2,3]
Complexity = O(n)
"""
def limit(ipt, minv,maxv):#you could set minv=None as default
    opt = ipt[::]
    if minv == None and maxv == None:
        return ipt
    elif minv == None and maxv != None:
        for i in ipt:
            if i > maxv:
                opt.remove(i)
    elif minv != None and maxv == None:
        for i in ipt:
            if i < minv:
                opt.remove(i)
    else:
        """
        You are not permitted to remove elements from the list while iterating over it using a for loop you need to make a copy and even comment you need to indent probably!
        """
        for i in ipt:
            print("forloop")
            if i < minv:
                opt.remove(i)
            if i > maxv:
                print("ifcondition")
                opt.remove(i)
    return opt

a = [1,2,3,4,5,6]
print(limit(a,2,4))

         
 
