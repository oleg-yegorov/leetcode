from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        # this approach add a special node and points to it from all already passed nodes
        if head is None:
            return False

        special_node = ListNode(0)

        while True:
            next = head.next
            head.next = special_node
            head = next
            if head == special_node:
                return True
            if head is None:
                return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow_pointer = fast_pointer = head

        while True:
            slow_pointer = slow_pointer.next

            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return False

            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return False
            if fast_pointer == slow_pointer:
                return True

    def hasCycleTobe(self, head: Optional[ListNode]) -> bool:
        slow_pointer = fast_pointer = head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if fast_pointer == slow_pointer:
                return True
        return False


def test_linked_list_cycle():
    n0 = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1
    assert Solution().hasCycle(n0) == True

    n0 = ListNode(3)
    n0.next = None
    assert Solution().hasCycle(n0) == False


