// https://leetcode.com/problems/insert-into-a-binary-search-tree/
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {

        if (root == null) return TreeNode(`val`)

        var left = root.left
        var right = root.right

        if (root.`val` < `val`) {
            right = insertIntoBST(right, `val`)
        } else {
            left = insertIntoBST(left, `val`)
        }
        
        root.right = right
        root.left = left
        
        return root
    }
}