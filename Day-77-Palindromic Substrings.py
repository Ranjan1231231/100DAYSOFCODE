"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
class Solution:
    def checkpaild(self, i, j, s):
        if i > j:
            return True
        if s[i] == s[j]:
            return self.checkpaild(i + 1, j - 1, s)

    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.checkpaild(i, j, s):
                    c += 1
        return c
