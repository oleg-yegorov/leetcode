from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head

        dummy = ListNode(0)
        dummy.next = head

        right_ptr = dummy
        for l in range(k):
            if right_ptr.next:
                right_ptr = right_ptr.next
            else:
                right_ptr = head
                if k % l == 0:
                    return head
                else:
                    for _ in range(k % l - 1):
                        right_ptr = right_ptr.next
                    break

        left_ptr = dummy
        while right_ptr.next:
            right_ptr = right_ptr.next
            left_ptr = left_ptr.next

        if left_ptr is not dummy:
            dummy.next = left_ptr.next
            right_ptr.next = head
            left_ptr.next = None

        return dummy.next

def test_rotate_list():
    l = ListNode(0)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    res = Solution().rotateRight(l, 4)
    assert res.val == 2
    assert res.next.val == 0
    assert res.next.next.val == 1

    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    res = Solution().rotateRight(l, 2)
    assert res.val == 4
    assert res.next.val == 5
    assert res.next.next.val == 1
    assert res.next.next.next.val == 2
    assert res.next.next.next.next.val == 3

    Solution().rotateRight(None, 1) == None

    l = ListNode(100)
    res = Solution().rotateRight(l, 1)
    assert res.val == 100
    assert res.next is None

