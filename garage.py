"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.
"""
"""
a[x:y:z] means : x is the former xth data is removed, y is after yth data is removed , so [x to y] is keeped, z is the stride it is going to take
"""

def garage(ini,fin):
    ini = ini[::]
    steps = 0
    seq = []#out put of the sequence of each step
    while ini != fin:
    zero = ini.index(0)
    if zero != fin.index(0):
	car_moves = fin[zero]
	pos = ini.index(car_moves)
	ini[zero],ini[pos] = ini[pos], ini[zero]
    else:
	for i in range(len(ini)):
	    if ini[i] != fin[i]:
		ini[zero]
