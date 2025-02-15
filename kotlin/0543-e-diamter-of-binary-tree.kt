// https://leetcode.com/problems/diameter-of-binary-tree/
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
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        var maxLength = 0

        fun longest(root: TreeNode?): Int {
            if (root == null) return 0

            val longestLeft = longest(root.left)
            val longestRight = longest(root.right)
            val maxInternal = 1 + max(longestLeft, longestRight)

            maxLength = max(longestLeft + longestRight, maxLength)

            return maxInternal
        }

        longest(root)

        return maxLength
    }
}