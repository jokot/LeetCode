# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        initial = 0

        if root:
            initial = 1
        else:
            initial = 0

        def innerMax(root: Optional[TreeNode]):
            if not root:
                return 0
                
            left = 0
            right = 0

            if root.left:
                left = innerMax(root.left) + 1
            if root.right:
                right = innerMax(root.right) + 1

            return max(left, right)
        

        return innerMax(root) + initial
