// https://leetcode.com/problems/balanced-binary-tree
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
    fun isBalanced(root: TreeNode?): Boolean {
        var balance = true

        fun balanced(node: TreeNode?): Int {
            if (node == null || !balance) return 0

            val l = balanced(node.left)
            val r = balanced(node.right)

            if (abs(l - r) > 1) {
                balance = false
            }

            return 1 + max(l, r)
        }

        balanced(root)
        
        return balance
    }
}