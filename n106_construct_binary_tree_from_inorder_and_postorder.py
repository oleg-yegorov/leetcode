from typing import List, Optional

from auxiliary_types import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree_4_pointers(pl: int, pr: int, il: int, ir: int) -> Optional[TreeNode]:
            head = TreeNode(postorder[pr-1])
            in_head = inorder.index(head.val, il, ir)
            left_part = in_head - il
            right_part = ir - in_head - 1

            head.left = build_tree_4_pointers(pl, pl + left_part, il, in_head) if left_part else None
            head.right = build_tree_4_pointers(pl + left_part, pr-1, in_head+1, ir) if right_part else None

            return head

        if not postorder:
            return None

        return build_tree_4_pointers(0, len(postorder), 0, len(inorder))




def test_build_tree_from_inorder_and_postorder():
    tree = Solution().buildTree(postorder=[9,15,7,20,3], inorder=[9,3,15,20,7])
    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20
    assert tree.right.left.val == 15
    assert tree.right.right.val == 7
