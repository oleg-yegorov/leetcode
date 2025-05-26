from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # напрашивается обход в ширину Breadth-first-search, но такой алгоритм будет использовать O(n) дополнительного
        # пространства. А предлагается использовать O(1) дополнительного пространства.

        # Можно хранить список из элементов, по длине равной глубине дерева
        # Если ты на уровне n и в этом списке есть элемент n, то можно добавить
        # на него связь. Иначе будет связь на null. Ну и после этого обновить элемент в списке.
        def _connect(node, level: int, r_els: list[Optional[Node]]):
            if not node:
                return

            if len(r_els) < level + 1:
                r_els.append(None)

            node.next = r_els[level]
            r_els[level] = node

            _connect(node.right, level+1, r_els)
            _connect(node.left, level+1, r_els)

        right_elements = []
        _connect(root, 0, right_elements)
        return root

def test_popuatel_next_right_pointers():
    root = Node(1, next=None)
    root.left = Node(2, next=None)
    root.left.left = Node(4, next=None)
    root.left.right = Node(5, next=None)
    root.right = Node(3, next=None)
    root.right.right = Node(7, next=None)

    root = Solution().connect(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
    assert root.right.right.next is None

    assert Solution().connect(None) is None
