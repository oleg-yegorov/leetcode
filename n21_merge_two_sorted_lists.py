from typing import Optional

import pytest

from auxiliary_types import ListNode


class SolutionOthers:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # after Youtube
        # return list must be made of list1 and list2 nodes !!!

        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next


class SolutionMy:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 or list2:
            val = min(list1.val if list1 else float("inf"),
                    list2.val if list2 else float("inf"))

            cur.next = ListNode(val)
            cur = cur.next

            if list1 and val == list1.val:
                list1 = list1.next
            else:
                list2 = list2.next
                
        return dummy.next


@pytest.mark.parametrize("solution_class", [SolutionMy, SolutionOthers])
def test_merge_two_sorted_lists(solution_class):
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    r = solution_class().mergeTwoLists(l1, l2)
    assert r.val == 1
    assert r.next.val == 1
    assert r.next.next.val == 2
    assert r.next.next.next.val == 3
    assert r.next.next.next.next.val == 4
    assert r.next.next.next.next.next.val == 4

    assert None is solution_class().mergeTwoLists(None, None)
    assert solution_class().mergeTwoLists(None, ListNode(0)).val == 0