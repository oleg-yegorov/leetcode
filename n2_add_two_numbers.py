from typing import Optional

import pytest

from auxiliary_types import ListNode


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class SolutionMy:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2
        head = None
        prev = None

        add_one = False
        while l1_ptr or l2_ptr:
            r = (l1_ptr.val if l1_ptr else 0) + (l2_ptr.val if l2_ptr else 0) + add_one
            if r > 9:
                add_one = True
                r -= 10
            else:
                add_one = False

            new_node = ListNode(r)
            new_node.next = None
            if not head:
                head = new_node
                prev = head
            else:
                prev.next = new_node
                prev = new_node

            l1_ptr = l1_ptr.next if l1_ptr else l1_ptr
            l2_ptr = l2_ptr.next if l2_ptr else l2_ptr

        if add_one:
            new_node = ListNode(1)
            new_node.next = None
            prev.next = new_node

        return head


class SolutionOthers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


@pytest.mark.parametrize('solution_class', [SolutionMy, SolutionOthers])
def test_add_two_number(solution_class):
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = solution_class().addTwoNumbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8

    l1 = ListNode(0)
    l2 = ListNode(0)
    res = solution_class().addTwoNumbers(l1, l2)
    assert res.val == 0

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    res = solution_class().addTwoNumbers(l1, l2)
    assert res.val == 8
    assert res.next.val == 9
    assert res.next.next.val == 9
    assert res.next.next.next.val == 9
    assert res.next.next.next.next.val == 0
    assert res.next.next.next.next.next.val == 0
    assert res.next.next.next.next.next.next.val == 0
    assert res.next.next.next.next.next.next.next.val == 1
