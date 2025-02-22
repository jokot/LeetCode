# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

# Runner and test cases
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def test_lowest_common_ancestor():
    solution = Solution()

    # Test case 1
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    expected = 6
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == expected

    # Test case 2
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 4)
    expected = 2
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == expected

    # Test case 3
    root = build_tree([2, 1])
    p = find_node(root, 2)
    q = find_node(root, 1)
    expected = 2
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == expected

    # Test case 4
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    p = find_node(root, 1)
    q = find_node(root, 4)
    expected = 3
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == expected

    # Test case 5
    root = build_tree([3, 1, 4, None, 2])
    p = find_node(root, 2)
    q = find_node(root, 4)
    expected = 3
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_lowest_common_ancestor()
