from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root


def test_invert_tree():
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    root = Solution().invertTree(root)

    assert root.val == 4
    assert root.left.val == 7
    assert root.right.val == 2
    assert root.left.left.val == 9
    assert root.left.right.val == 6
    assert root.right.left.val == 3
    assert root.right.right.val == 1

