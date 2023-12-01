class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        b=""
        for i in reversed(a):
            b+=i
        return a==b
        
