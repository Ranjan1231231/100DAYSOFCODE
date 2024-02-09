"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        nums.sort()
        for num in nums:
            divisors = []
            for key in subsets:
                if num % key == 0:
                    divisors.append(key)

            possibilities = []
            for possibility in divisors:
                # Collect subsets corresponding to each divisor
                possibilities.append(subsets[possibility])

            # Find the subset with the maximum length
            max_subset = max(possibilities, key=len)

            # Union of max_subset and num for the subset of num
            subsets[num] = max_subset | {num}

        return max(subsets.values(), key=len)    
