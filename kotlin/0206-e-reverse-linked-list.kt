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
        var newNode: ListNode? = null
        var traverseNode = head

        while (traverseNode != null) {
            val temp = traverseNode.next

            traverseNode.next = newNode
            newNode = traverseNode

            traverseNode = temp
        }

        return newNode
    }
}