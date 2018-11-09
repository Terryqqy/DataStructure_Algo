"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.
This algorithm gets an array, makes a dictionary of it,
 finds the most frequent count, and makes the result list.
For example: top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]
(TL:DR) Get mathematical Mode
Complexity: O(n)
"""
def top_1(ipt): 
    topnum = 0
    dictforelem = {}
    output = []
    for i in ipt:
        if i in dictforelem:
            dictforelem[i] += 1
        else:
            dictforelem[i] = 1
    for i in dictforelem:
        if dictforelem[i] == topnum:
            output.append(i)
        elif dictforelem[i] > topnum:
            output[:] = []
            output.append(i)
            topnum = dictforelem[i]
    return output

a = [1,1,2,2,3,4,2,3,3]
print(top_1(a))
