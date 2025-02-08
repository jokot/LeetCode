from typing import Optional

# https://leetcode.com/problems/linked-list-cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        fast = head.next
        slow = head

        while fast != slow:
            if fast is None: return False
            if fast.next is None: return False
            fast = fast.next.next
            slow = slow.next
        return True

def create_cycle_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head

# Runner
if __name__ == "__main__":
    solution = Solution()

    # Test data
    test_cases = [
        ([3, 2, 0, -4], 1),  # Cycle at position 1
        ([1, 2], 0),         # Cycle at position 0
        ([1], -1),           # No cycle
        ([1, 2, 3, 4, 5], 2),# Cycle at position 2
        ([], -1)             # Empty list, no cycle
    ]

    for i, (values, pos) in enumerate(test_cases):
        head = create_cycle_list(values, pos)
        result = solution.hasCycle(head)
        print(f"Test case {i + 1}: {result}")   