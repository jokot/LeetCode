// https://leetcode.com/problems/binary-tree-inorder-traversal
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
    fun inorderTraversal(root: TreeNode?): List<Int> {
        val res = mutableListOf<Int>()

        fun inorder(root: TreeNode?) {
            if (root == null) return

            inorder(root.left)
            res.add(root.`val`)
            inorder(root.right)
        }

        inorder(root)

        return res
    }
}