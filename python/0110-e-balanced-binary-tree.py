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

        def dfs(node):

            if not node: return (True, 0)

            l, r = dfs(node.left), dfs(node.right)

            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return (balanced, 1 + max(l[1], r[1]))
        
        return dfs(root)[0]

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
