'''
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.f
'''
def delete_nth(array, n):
	retval = []
	cout = {}
	for i in array:
		if not i in cout:
			cout[i]=1
			retval.append(i)
		elif i in cout and cout[i] < n:
			cout[i]+=1
			#print(cout[i])
			retval.append(i)
	return retval

a = [1,2,3,1,2,3,1,2,3,4,5,4,6]
print(delete_nth(a,2))

							
