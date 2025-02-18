//  https://leetcode.com/problems/subtree-of-another-tree
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
    fun isSubtree(root: TreeNode?, subRoot: TreeNode?): Boolean {
        if (subRoot == null) return true
        if (root == null) return false
        if (sameTree(root, subRoot)) return true
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }

    fun sameTree(root: TreeNode?, subRoot: TreeNode?): Boolean {
        return when {
            (root == null && subRoot == null) -> true
            (root != null && subRoot != null && root.`val` == subRoot.`val`) -> {
                sameTree(root?.left, subRoot?.left) && sameTree(root?.right, subRoot?.right)
            }
            else -> false
        }
    }
}
