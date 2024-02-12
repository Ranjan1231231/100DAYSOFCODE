"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num1,count1 = None,0
        num2,count2 = None,0
        ans,maxLen = None,0

        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            elif count1<=count2:
                num1=num
                count1=1
            else:
                num2=num
                count2=1

            if count1>maxLen:
                ans=num1
                maxLen = count1

            if count2>maxLen:
                ans=num2
                maxLen = count2

        return ans
