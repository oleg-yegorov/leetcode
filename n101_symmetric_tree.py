from typing import Optional

from auxiliary_types import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def nlr_nrl(ptr_l: TreeNode, ptr_r: TreeNode) -> bool:
            if not ptr_l and not ptr_r:
                return True
            elif ptr_l and ptr_r:
                return ptr_l.val == ptr_r.val and nlr_nrl(ptr_l.left, ptr_r.right) and nlr_nrl(ptr_l.right, ptr_r.left)
            else:
                return False

        if not root:
            return True

        return nlr_nrl(root.left, root.right)


def test_is_symmetric_tree():
    tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert Solution().isSymmetric(tree)

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert not Solution().isSymmetric(tree)

    assert not Solution().isSymmetric(TreeNode(1, None, TreeNode(2)))
