from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(node, val):
            if not node:
                return TreeNode(val = val)
            
            left = node.left
            right = node.right

            if node.val < val:
                right = insert(node.right, val)
            else:
                left = insert(node.left, val)

            node.right = right
            node.left = left
            
            return node
        
        return insert(root, val)

# Runner and test cases
def build_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(nodes, 2 * index + 1)
    root.right = build_tree(nodes, 2 * index + 2)
    return root

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

def test_insert_into_bst():
    solution = Solution()

    # Test case 1
    root = build_tree([4, 2, 7, 1, 3])
    val = 5
    expected = [4, 2, 7, 1, 3, 5]
    result = solution.insertIntoBST(root, val)
    assert tree_to_list(result) == expected

    # Test case 2
    root = build_tree([40, 20, 60, 10, 30, 50, 70])
    val = 25
    expected = [40, 20, 60, 10, 30, 50, 70, None, None, 25]
    result = solution.insertIntoBST(root, val)
    assert tree_to_list(result) == expected

    # Test case 3
    root = build_tree([4, 2, 7, 1, 3, None, None, None, None, None, None])
    val = 5
    expected = [4, 2, 7, 1, 3, 5]
    result = solution.insertIntoBST(root, val)
    assert tree_to_list(result) == expected

    # Test case 4
    root = build_tree([5, 3, 6, 2, 4, None, None, 1])
    val = 7
    expected = [5, 3, 6, 2, 4, None, 7, 1]
    result = solution.insertIntoBST(root, val)
    assert tree_to_list(result) == expected

    # Test case 5
    root = build_tree([])
    val = 1
    expected = [1]
    result = solution.insertIntoBST(root, val)
    assert tree_to_list(result) == expected

    print("All test cases passed!")

if __name__ == "__main__":
    test_insert_into_bst()
