# https://leetcode.com/problems/merge-two-sorted-lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        elif not list1: return list2
        elif not list2: return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Sample data
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

list3 = ListNode(2, ListNode(5, ListNode(6)))
list4 = ListNode(1, ListNode(3, ListNode(7)))

list5 = ListNode(1, ListNode(1, ListNode(1)))
list6 = ListNode(2, ListNode(2, ListNode(2)))

# Runner
if __name__ == "__main__":
    solution = Solution()
    
    merged_list1 = solution.mergeTwoLists(list1, list2)
    print("Merged List 1:")
    print_list(merged_list1)
    
    merged_list2 = solution.mergeTwoLists(list3, list4)
    print("Merged List 2:")
    print_list(merged_list2)
    
    merged_list3 = solution.mergeTwoLists(list5, list6)
    print("Merged List 3:")
    print_list(merged_list3)