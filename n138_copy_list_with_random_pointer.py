from typing import Optional

import pytest

import utility


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        dummy = Node(0)

        # first time create new list and make a map from list nodes to new list nodes
        cur_new = dummy
        cur = head
        while cur:
            cur_new.next = Node(cur.val)
            cur_new = cur_new.next
            d[cur] = cur_new
            cur = cur.next

        # second time add random pointer according to hash map previously created
        cur = head
        while cur:
            if cur.random:
                d[cur].random = d[cur.random]
            else:
                d[cur].random = None
            cur = cur.next

        return dummy.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # write nodes in list
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # write random indices of all nodes to list of indices
        random_indices = []
        cur = head
        while cur:
            random_indices.append(nodes.index(cur.random) if cur.random is not None else -1)
            cur = cur.next


        # create new list with values from original list and write a new list of nodes
        dummy = Node(0)

        cur = dummy
        new_nodes = []
        for node in nodes:
            cur.next = Node(node.val)
            cur = cur.next
            new_nodes.append(cur)

        # fill random-index value accorgind to random_indices list and new_nodes list
        cur = dummy.next
        for index in random_indices:
            cur.random = new_nodes[index] if index > -1 else None
            cur = cur.next

        return dummy.next


@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[Node]))
def test_copy_random_list(solution_class):
    n0 = Node(7)
    n1 = Node(13)
    n2 = Node(11)
    n3 = Node(10)
    n4 = Node(1)

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    n0.random = None
    n1.random = n0
    n2.random = n4
    n3.random = n2
    n4.random = n0

    solution_class().copyRandomList(n0)
