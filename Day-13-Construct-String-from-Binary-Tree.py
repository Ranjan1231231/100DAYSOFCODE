"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        def traversal(root,ans):
            ans = ("("+str(root.val))
            if root.left:
              ans+=traversal(root.left,ans)
              if root.right:
                ans+=traversal(root.right,ans)
            else:
              if root.right:
                ans+="()"
                ans+=traversal(root.right,ans)
            ans+=")"
            return ans
        ans = traversal(root,ans)
        return ans[1:len(ans)-1]
