// https://leetcode.com/problems/binary-tree-preorder-traversal
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
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val res = mutableListOf<Int>()

        fun preorder(root: TreeNode?) {
            if (root == null) return

            res.add(root.`val`)
            preorder(root.left)
            preorder(root.right)
        }
        
        preorder(root)

        return res
    }
}