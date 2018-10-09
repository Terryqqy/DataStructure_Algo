"""
input a nested array we need to flatten it into one array
"""
from collections import Iterable

def flatt(ipt_arr, opt_arr= None): #the default of the output array is None by default
    if opt_arr is None:
        opt_arr = []
    for i in ipt_arr:
        if isinstance(i, Iterable):#isinstance is to check if the i is one of Iterable(abstract base class in collections. So if i is iterable it means that it is an array
            flatt(i, opt_arr)
        else:
            opt_arr.append(i)
    return opt_arr

a = [1,1,2,[1,2,3],1,[3,[2,3]],2]
print(flatt(a))
           
