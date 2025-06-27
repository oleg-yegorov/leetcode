from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def _flattern(node: TreeNode) -> TreeNode:
            if node.right and node.left:
                tmp = node.left
                node.left = node.right
                node.right = tmp

                last_node = _flattern(node.right)
                last_node.right = node.left
                last_node = _flattern(node.left)
                node.left = None
                return last_node
            elif node.left:
                node.right = node.left
                node.left = None
                return _flattern(node.right)
            elif node.right:
                return _flattern(node.right)
            else:
                return node

        if root:
            _flattern(root)


def test_flattern_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    Solution().flatten(root)
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    assert root.right.right.right.val == 4
    assert root.right.right.right.right.val == 5
    assert root.right.right.right.right.right.val == 6

    root = None
    Solution().flatten(root)
    assert root is None

    root = TreeNode(0)
    Solution().flatten(root)
    assert root.val == 0
