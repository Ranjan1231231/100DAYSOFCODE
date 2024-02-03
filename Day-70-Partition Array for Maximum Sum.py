"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n

        def recur(i):
            if i == n:
                return 0
            
            max_elm = -1 # max element in segment
            max_score = -1 # overall max score
            segment_len = 0 # this is obvious

            if dp[i] != -1:
                return dp[i]

            for j in range(i,min(i+k,n)):
            # We iterate from i to minimum of i+k or n
            # in spirit of checking all cases
                segment_len += 1
                max_elm = max(max_elm, arr[j])
                score = segment_len*max_elm + recur(j+1)
                # the recursive stack here goes till the end of 
                # arr each time it is called, 
                # hence the // sub-problems //
                max_score = max(max_score,score)

            # dp array fills up from the last, hence
            # the first element of dp array is the ans.
            dp[i] = max_score
            return dp[i]

        return recur(0)        
