from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        delete_last = False
        while ptr.next and ptr.next.next:
            if ptr.next.val == ptr.next.next.val:
                ptr.next = ptr.next.next
                delete_last = True
            elif delete_last:
                ptr.next = ptr.next.next
                delete_last = False
            else:
                ptr = ptr.next

        if delete_last:
            ptr.next = ptr.next.next

        return dummy.next


def test_delete_duplicated_from_sorted_list_ii():
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)
    l.next.next.next.next.next = ListNode(4)
    l.next.next.next.next.next.next = ListNode(5)
    res = Solution().deleteDuplicates(l)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 5

    l = ListNode(1)
    l.next = ListNode(1)
    res = Solution().deleteDuplicates(l)
    assert res == None

    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(3)
    res = Solution().deleteDuplicates(l)
    assert res.val == 2
    assert res.next.val == 3
