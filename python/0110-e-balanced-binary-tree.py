# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def balanced(node):
            nonlocal balance

            if not node or not balance:
                return 0

            l = balanced(node.left)
            r = balanced(node.right)

            if abs(l - r) > 1:
                balance = False

            return 1 + max(l, r)
        
        balanced(root)
        
        return balance

def buildTree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def test():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([3,9,20,None,None,15,7], True),  # Balanced tree
        ([1,2,2,3,3,None,None,4,4], False),  # Unbalanced tree
        ([], True),  # Empty tree
        ([1], True),  # Single node
        ([1,2,2,3,None,None,3,4,None,None,4], False)  # Another unbalanced tree
    ]
    
    for i, (values, expected) in enumerate(test_cases, 1):
        root = buildTree(values)
        result = solution.isBalanced(root)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    test()
