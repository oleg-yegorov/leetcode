from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        last = dummy

        while last.next and last.next.next:
            insert_after = last
            last = insert_after.next
            to_insert = last.next

            for i in range(k-1):
                last.next = to_insert.next
                to_insert.next = insert_after.next
                insert_after.next = to_insert
                if (to_insert := last.next) is None and i < (k-2):
                    for j in range(i + 1):
                        tmp = last.next
                        last.next = insert_after.next
                        insert_after.next = insert_after.next.next
                        last.next.next = tmp
                    break

        return dummy.next


def test_reverse_k_group():
    l = ListNode(1)
    l.next = ListNode(2)
    res = Solution().reverseKGroup(l, 2)
    assert res.val == 2
    assert res.next.val == 1

    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(6)

    res = Solution().reverseKGroup(l, 4)
    assert res.val == 4
    assert res.next.val == 3
    assert res.next.next.val == 2
    assert res.next.next.next.val == 1
    assert res.next.next.next.next.val == 5
    assert res.next.next.next.next.next.val == 6
