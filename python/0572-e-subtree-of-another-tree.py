from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False

# Runner and test cases
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

def test_is_subtree():
    solution = Solution()

    # Test case 1
    root = build_tree([3, 4, 5, 1, 2])
    subRoot = build_tree([4, 1, 2])
    assert solution.isSubtree(root, subRoot) == True

    # Test case 2
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = build_tree([4, 1, 2])
    assert solution.isSubtree(root, subRoot) == False

    # Test case 3
    root = build_tree([1, 1])
    subRoot = build_tree([1])
    assert solution.isSubtree(root, subRoot) == True

    # Test case 4
    root = build_tree([1, 2, 3])
    subRoot = build_tree([2])
    assert solution.isSubtree(root, subRoot) == True

    # Test case 5
    root = build_tree([1, 2, 3])
    subRoot = build_tree([4])
    assert solution.isSubtree(root, subRoot) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_subtree()

