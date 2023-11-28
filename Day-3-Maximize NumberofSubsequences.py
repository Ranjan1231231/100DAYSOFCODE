import sys
def maximumSubsequenceCount( text, pattern):
    # Separate the pattern into two characters, p1 and p2
    p1, p2 = pattern
    # If both characters in the pattern are the same, calculate count directly
    if p1 == p2:
        n = text.count(p1) + 1
        return n * (n - 1) // 2
    # defining a helper function to count the occurrences of p2 after p1 in a string
    def count(s):
        res = curr = 0
        for x in s:
            if x == p1:
                curr += 1
            elif x == p2:
                res += curr
        return res
    return max(count(p1 + text), count(text + p2))
print(maximumSubsequenceCount("ababc","ab"))        
print(maximumSubsequenceCount("ababab","ab"))
print(maximumSubsequenceCount("abdcdbc","ac"))
