"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i,j in count.items():
            if j==1: # checking if occurence is 1
                return s.index(i)
        return -1      
