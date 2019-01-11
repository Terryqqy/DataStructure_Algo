"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
def longest_s(ipt):
    tst1,tst2 ="",""
    for i in ipt:
        if i not in tst1:
            tst1+=i
        else:
            if len(tst1) > len(tst2):
                tst2, tst1 = tst1, i
            else:
                tst1 = i
    return tst2
a = "abccccdefghhhhhhhhhabcd"
b = "pwwkew"
print(longest_s(b))

print(longest_s(a))

    
