# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def longest(root: Optional[TreeNode]):
            nonlocal maxLength

            if not root:
                return 0
            
            longestLeft = longest(root.left)
            longestRight = longest(root.right)
            maxInternal = 1 + max(longestLeft, longestRight)

            maxLength = max(longestLeft + longestRight, maxLength)
            
            return maxInternal
        
        longest(root)

        return maxLength

# Helper function to create tree from array
def createTree(values: List[int], index: int = 0) -> Optional[TreeNode]:
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = createTree(values, 2 * index + 1)
    root.right = createTree(values, 2 * index + 2)
    return root

# Runner code with sample input
if __name__ == "__main__":
    # Test cases: (input_array, expected_output)
    test_cases = [
        ([1,2,3,4,5], 3),              # Example from LeetCode
        ([1,2], 1),                     # Simple tree with one edge
        ([1], 0),                       # Single node
        ([], 0),                        # Empty tree
        ([1,2,3,4,5,None,None,8,9], 4), # Unbalanced tree
        ([1,2,3,4,None,None,5], 4),     # Tree with gaps
        ([3,1,None,None,2], 2)
    ]
    
    solution = Solution()
    
    # Test each case
    for i, (input_array, expected) in enumerate(test_cases, 1):
        root = createTree(input_array)
        result = solution.diameterOfBinaryTree(root)
        print(f"Test Case {i}:")
        print(f"Input tree array: {input_array}")
        print(f"Expected diameter: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")
        print("-" * 50)