"""
474. Ones and Zeroes
Medium
5.3K
437
Companies
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def helper(s):
            ones = s.count('1')
            zeros = s.count('0')
            return ones, zeros

        if not strs:
            return 0

        if len(strs) == 1: 
            ones, zeros = helper(strs[0])
            if ones <= n and zeros <= m:
                return 1
            else:
                return 0

        combinations = dict()
        combinations['0,0'] = []
        for s in strs: 

            new_combinations = dict()
            ones, zeros = helper(s)
            for k in combinations:
                key_one, key_zeros = list(map(int, k.split(',')))
                key_one += ones
                key_zeros += zeros
                new_combinations[k] = max(new_combinations.get(k, []), combinations[k], key = len)  
                if key_zeros > m or key_one > n:
                    continue
                new_key = str(key_one) + ',' + str(key_zeros)
                new_combinations[new_key] =  max(combinations[k]+[s], combinations.get(new_key, []), key = len) 
            combinations = new_combinations
            
        key = str(n) + ',' + str(m)
        print(combinations)
        return max([len(v) for k, v in combinations.items()])
