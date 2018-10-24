"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]
The time complexity of the below algorithm is O(n).
"""
def move_zeros(ipt):
    countnumber = 0
    for i in range(len(ipt)):
        #remember here we need to use is! == can not diff 0 and false
        if ipt[i] is 0:
            countnumber+=1
            ipt.pop(i)
            i-=1
        i+=1
    while(countnumber!=0):
        ipt.append(0)
        countnumber-=1
    return ipt
print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
