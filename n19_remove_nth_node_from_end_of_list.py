from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        ptr = dummy
        for _ in range(n+1):
            ptr = ptr.next

        delete_ptr = dummy
        while ptr:
            ptr = ptr.next
            delete_ptr = delete_ptr.next

        delete_ptr.next = delete_ptr.next.next
        return dummy.next


def test_remove_nth_from_end():
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    res = Solution().removeNthFromEnd(l, 2)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next.val == 5
    assert res.next.next.next.next is None

    Solution().removeNthFromEnd(ListNode(0), 1)  == None
