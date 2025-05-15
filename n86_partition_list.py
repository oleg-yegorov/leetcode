from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_low = ListNode(0)
        ptr_low = dummy_low

        dummy_high = ListNode(0)
        ptr_high = dummy_high

        ptr = head
        while ptr:
            if ptr.val < x:
                ptr_low.next = ListNode(ptr.val)
                ptr_low = ptr_low.next
            else:
                ptr_high.next = ListNode(ptr.val)
                ptr_high = ptr_high.next
            ptr = ptr.next

        ptr_low.next = dummy_high.next
        return dummy_low.next


def test_partition_list():
    l = ListNode(1)
    l.next = ListNode(4)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(2)

    res = Solution().partition(l, 3)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 2
    assert res.next.next.next.val == 4
    assert res.next.next.next.next.val == 3
    assert res.next.next.next.next.next.val == 5

    Solution().partition(None, 3) == None
