"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = [nums[0]]

        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)
            else:
                left, right = 0, len(res) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if res[mid] < num:
                        left = mid + 1
                    else:
                        right = mid

                res[left] = num

        return len(res)        
