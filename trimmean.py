"""
When make reliable means, we need to neglect best and worst values.
For example, when making average score on athletes we need this option.
So, this algorithm affixes some percentage to neglect when making mean.
For example, if you suggest 20%, it will neglect the best 10% of values
and the worst 10% of values.
This algorithm takes an array and percentage to neglect. After sorted,
if index of array is larger or smaller than desired ratio, we don't
compute it.
Compleity: O(n)
"""
def trimmean(ipt, perc):
    ipt.sort()
    summ = 0
    ratio = perc/200
    for idx in range(len(ipt)):
        if idx/len(ipt) < ratio or idx/len(ipt) > 1-ratio:
            pass
        else:
            summ += ipt[idx]
    
    return summ/len(ipt)

            
a = [1,2,3,4,5,6,7,8,9,10]
print(trimmean(a, 20))
