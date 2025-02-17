# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return p.val == q.val and left and right

# Runner and test cases
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

def test_is_same_tree():
    solution = Solution()

    # Test case 1
    p = build_tree([1, 2, 3])
    q = build_tree([1, 2, 3])
    assert solution.isSameTree(p, q) == True

    # Test case 2
    p = build_tree([1, 2])
    q = build_tree([1, None, 2])
    assert solution.isSameTree(p, q) == False

    # Test case 3
    p = build_tree([1, 2, 1])
    q = build_tree([1, 1, 2])
    assert solution.isSameTree(p, q) == False

    # Test case 4
    p = build_tree([])
    q = build_tree([])
    assert solution.isSameTree(p, q) == True

    # Test case 5
    p = build_tree([1])
    q = build_tree([1])
    assert solution.isSameTree(p, q) == True

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_same_tree()