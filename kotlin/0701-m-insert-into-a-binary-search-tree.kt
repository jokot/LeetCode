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

        if (`val` > root.`val`) {
            root.right = insertIntoBST(root.right, `val`)
        } else {
            root.left = insertIntoBST(root.left, `val`)
        }
        
        return root
    }
}