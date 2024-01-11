"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]      
        def diff(root,maxi,mini):
            if root == None:
                return
            maxi = max(maxi,root.val)
            mini = min(mini,root.val)
            if maxi!=-10e9 and mini!=10e9:
                ans[0] = max(ans[0],maxi-mini)  
            if root.left:
                diff(root.left,maxi,mini)
            if root.right:
                diff(root.right,maxi,mini)
        diff(root,-10e9,10e9)
        return ans[0]      
