from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes: list[TreeNode] = [root]

        while next_left := self.nodes[-1].left:
            self.nodes.append(next_left)

    def next(self) -> int:
        node = self.nodes.pop()
        if ptr := node.right:
            self.nodes.append(ptr)
            while ptr.left:
                ptr = ptr.left
                self.nodes.append(ptr)
        return node.val

    def hasNext(self) -> bool:
        return len(self.nodes) > 0


def test_bst_iterator():
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    it = BSTIterator(root)
    assert it.next() == 3
    assert it.next() == 7
    assert it.hasNext()
    assert it.next() == 9
    assert it.hasNext()
    assert it.next() == 15
    assert it.hasNext()
    assert it.next() == 20
    assert not it.hasNext()
