// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

 class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        
        fun valNN(node: TreeNode?): Int {
            return node?.`val` ?: 0
        }

        val pVal = valNN(p)
        val qVal = valNN(q)        
        var current = root

        while (true) {
            val curVal = valNN(current)
            when {
                pVal > curVal && qVal > curVal -> {
                    current = current?.right
                }
                pVal < curVal && qVal < curVal -> {
                    current = current?.left
                }
                else -> return current
            }
        }

        return current
    }
}