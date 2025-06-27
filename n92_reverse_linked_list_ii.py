from typing import Optional

import pytest

from auxiliary_types import ListNode


# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
# of the list from position left to position right, and return the reversed list.


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # in-place
        dummy = ListNode(0)
        dummy.next = head

        # get to the element before left
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        last = prev.next

        cur = last.next
        for _ in range(right - left):
            last.next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = last.next

        return dummy.next


class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur_new = dummy

        # add nodes before interval and the first element of the interval, cur_new points to the last-1 element
        cur = head
        for _ in range(left - 1):
            cur_new.next = ListNode(cur.val)
            cur_new = cur_new.next
            cur = cur.next
        cur_new.next = ListNode(cur.val)
        cur = cur.next

        # insert all elements in interval after left-1 element (= in reverse order)
        last = cur_new.next
        for _ in range(right - left):
            new_node = ListNode(cur.val)
            new_node.next = cur_new.next
            cur_new.next = new_node
            cur = cur.next

        # insert other elements
        while cur:
            last.next = ListNode(cur.val)
            last = last.next
            cur = cur.next

        return dummy.next


@pytest.mark.parametrize('solution_class', [Solution, Solution2])
def test_reverse_between(solution_class):
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    r = solution_class().reverseBetween(l, 2, 4)

    assert r.val == 1
    assert r.next.val == 4
    assert r.next.next.val == 3
    assert r.next.next.next.val == 2
    assert r.next.next.next.next.val == 5

    l = ListNode(1)
    l.next = ListNode(2)
    l = solution_class().reverseBetween(l, 1, 2)
    assert l.val == 2
    assert l.next.val == 1
