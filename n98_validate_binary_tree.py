from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_with_diff(node: TreeNode):
            if node.left:
                yield from inorder_with_diff(node.left)

            yield node.val

            if node.right:
                yield from inorder_with_diff(node.right)

        it = inorder_with_diff(root)
        low = next(it)
        for i in it:
            if low > i:
                return False
            low = i

        return True
