// https://leetcode.com/problems/linked-list-cycle/

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
    fun hasCycle(head: ListNode?): Boolean {
        if (head == null) return false
        var fast = head.next
        var slow = head

        while (fast != slow) {
            if (fast == null) return false
            if (fast.next == null) return false
            fast = fast.next.next
            slow = slow?.next            
        }

        return true
    }
}