from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum_numbers(root: TreeNode, val) -> int:
            if not root.left and not root.right:
                return val + root.val

            left_subtree = sum_numbers(root.left, (val + root.val) * 10) if root.left else 0
            right_subtree = sum_numbers(root.right, (val + root.val) * 10) if root.right else 0

            return left_subtree + right_subtree

        if not root:
            return 0
        else:
            return sum_numbers(root, 0)


def test_sum_numbers():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert Solution().sumNumbers(root) == 25
