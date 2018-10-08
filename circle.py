"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
def circle(ipt):
    opt = ipt[::]
    realopt=[]
    p = -1
    while(opt):
	p+=3
	print(p)
	if p >= len(opt):#doesn't need this one since modulo will do everything
	    p = p%len(opt)
	realopt.append(opt.pop(p))
	p = p - 1
    return realopt#actually could use yield to output continuous result


a = [1,2,3,4,5,6,7,8,9]
print(circle(a))    
