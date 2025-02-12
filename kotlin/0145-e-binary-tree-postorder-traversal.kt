// https://leetcode.com/problems/binary-tree-postorder-traversal/
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
    fun postorderTraversal(root: TreeNode?): List<Int> {
        val res = mutableListOf<Int>()

        fun postorder(root: TreeNode?) {
            if (root == null) return

            postorder(root.left)
            postorder(root.right)
            res.add(root.`val`)
        }   

        postorder(root)

        return res
    }
}