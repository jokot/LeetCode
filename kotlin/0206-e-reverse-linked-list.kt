// https://leetcode.com/problems/reverse-linked-list

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        if (head == null) return null
        val reverse = ListNode(head!!.`val`)

        val copy = mutableListOf<Int>()

        var node = head
        while (node != null) {
            copy.add(node!!.`val`)
            node = node?.next
        }

        val right = copy.size - 1
        for (i in 0 until copy.size / 2) {
            val temp = copy[right - i]
            copy[right - i] = copy[i]
            copy[i] = temp
        }

        node = head
        var tNode = node
        for (i in 0 until copy.size) {
            tNode?.`val` = copy[i]
            tNode = tNode?.next
            
        }

        return node
    }
}