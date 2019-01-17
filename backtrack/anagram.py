'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Out put: false

lower or higher case is not sensitive
'''
def anagram(a, b):
    c1 = [0] * 26
    c2 = [0] * 26

    for c in a:
        pos = ord(c) - ord('a')
        c1[pos] += 1

    for c in b:
        pos = ord(c) - ord('a')
        c2[pos] += 1

    return c1 == c2

print(anagram("abc","acb"))
