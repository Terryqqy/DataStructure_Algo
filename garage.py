"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.Hey
"""
"""
a[x:y:z] means : x is the former xth data is removed, y is after yth data is removed , so [x to y] is keeped, z is the stride it is going to take
"""

def garage(initial,fin):
    ini = initial[::] #make a copy to prevent the change to original one
    steps = 0
    seq = []#out put of the sequence of each step
    """
    so in this loop we would do two path:
    check first data is same or not then if not move the first one to 
    the place in final. If yes then go to check next one.
    """
    while ini != fin:
        zero = ini.index(0)
        #that is the pin point
        if zero != fin.index(0):
            pos = ini.index(fin[zero])#python could return the place of zero element
            ini[zero],ini[pos] = ini[pos], ini[zero]#swap them!  so aewsome
        else:
	    for i in range(len(ini)):
		if ini[i] != fin[i]:
		    ini[zero], ini[i] = ini[i], ini[zero]
		    break
	seq.append(ini[::])#careful with the indent!
        steps +=1
    return steps, seq

a = [1,2,3,0,4]
b = [0,3,2,1,4]
opta, optb = garage(a,b)
print 'the steps are', opta,' the sequence is ', optb


