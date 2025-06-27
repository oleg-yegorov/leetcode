from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # in-order traversal
        def inorder_with_diff(node: TreeNode):
            if node.left:
                yield from inorder_with_diff(node.left)

            yield node.val

            if node.right:
                yield from inorder_with_diff(node.right)

        it = inorder_with_diff(root)
        low = next(it)
        _min = 20000
        for i in it:
            high = i
            _min = min(_min, high - low)
            if _min == 1:
                return _min
            low = high
        return _min


def test_get_min_diff_in_bst():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    assert Solution().getMinimumDifference(root) == 1