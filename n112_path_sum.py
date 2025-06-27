from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True

        left = self.hasPathSum(root.left, targetSum) if root.left else False
        if left:
            return True

        right = self.hasPathSum(root.right, targetSum) if root.right else False
        return True if right else False


def test_has_path_sum():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    assert Solution().hasPathSum(root, 22)

    root = TreeNode(1)
    root.left = TreeNode(2)

    assert not Solution().hasPathSum(root, 1)