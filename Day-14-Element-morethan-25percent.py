"""
1287. Element Appearing More Than 25% In Sorted Array
Easy
1.4K
65
Companies
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=0
        num=0
        for i in arr:
            if arr.count(i)>count:
                count=arr.count(i)
                num=i
        return num
