import sys

class ListNode:
    def __init__(self, key:int, val: int, next=None, prev=None):
        self.key: int = key
        self.val: int = val
        self.next: ListNode = next
        self.prev: ListNode = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.d_nodes: dict[int, ListNode] = {}
        self.capacity = capacity
        self.size = 0

        self.d_head = ListNode(key=-1, val=-1)
        self.d_tail = ListNode(key=-1, val=-1)
        self.d_head.next, self.d_tail.prev = self.d_tail, self.d_head

    def del_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.d_nodes[node.key]
        self.size -= 1

    def insert_node(self, node, after):
        node.next, node.prev, after.next.prev, after.next = after.next, after, node, node
        self.d_nodes[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.d_nodes:
            node = self.d_nodes[key]
            self.del_node(node)
            self.insert_node(node, self.d_head)
            return self.d_nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d_nodes:
            self.del_node(self.d_nodes[key])
        self.insert_node(ListNode(key, value), self.d_head)

        if self.size > self.capacity:
            self.del_node(self.d_tail.prev)


def test_lru_cache():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4
