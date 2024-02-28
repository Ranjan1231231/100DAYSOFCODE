"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.leftmostelm = root.val
        self.depth = 0
        self.path = 'z'
        self.find(root)
        return self.leftmostelm
    
    def find(self,root,s='r',d=0):
        if root == None:
            return
        if self.depth < d or ( self.path > s):
            self.depth = d
            self.path = s
            self.leftmostelm = root.val
        self.find(root.left,s+'l',d+1)
        self.find(root.right,s+'r',d+1)        
