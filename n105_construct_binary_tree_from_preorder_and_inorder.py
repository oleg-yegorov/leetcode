from typing import List, Optional

import pytest

from auxiliary_types import TreeNode


class SolutionWithPointers:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree_4_pointers(pl: int, pr: int, il: int, ir: int) -> Optional[TreeNode]:
            head = TreeNode(preorder[pl])
            in_head = inorder.index(head.val, il, ir)
            left_part = in_head - il
            right_part = ir - in_head - 1

            head.left = build_tree_4_pointers(pl + 1, pl + left_part + 1, il, in_head) if left_part else None
            head.right = build_tree_4_pointers(pl + left_part + 1, pr, in_head + 1, ir) if right_part else None

            return head

        if not preorder:
            return None

        return build_tree_4_pointers(0, len(preorder), 0, len(inorder))


class SolutionSmall:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # самое короткое решение
        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        in_head = inorder.index(head.val)

        head.left = self.buildTree(preorder[1: in_head + 1], inorder[0:in_head])
        head.right = self.buildTree(preorder[in_head + 1:], inorder[in_head+1:])

        return head


class SolutionClassic:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # нахожу двойки и тройки, мой классический метод
        if not preorder:
            return None

        nodes = [TreeNode(n) for n in preorder]

        while len(preorder) > 1:
            for pre_ind in range(len(preorder)-2, -1, -1):
                if pre_ind+2 < len(preorder):
                    first = preorder[pre_ind]
                    second = preorder[pre_ind+1]
                    third = preorder[pre_ind+2]
                    in_ind = inorder.index(first)
                    if in_ind-1 >= 0 and inorder[in_ind-1] == second and in_ind+1 < len(inorder) and inorder[in_ind+1] == third:
                        nodes[pre_ind].left = nodes[pre_ind+1]
                        nodes[pre_ind].right = nodes[pre_ind+2]
                        del preorder[pre_ind+1]
                        del preorder[pre_ind+1]
                        del nodes[pre_ind+1]
                        del nodes[pre_ind+1]
                        del inorder[in_ind-1]
                        del inorder[in_ind]
                        break
                first = preorder[pre_ind]
                second = preorder[pre_ind + 1]
                in_ind = inorder.index(first)
                if in_ind-1 >= 0 and inorder[in_ind-1] == second:
                    nodes[pre_ind].left = nodes[pre_ind+1]
                    del preorder[pre_ind+1]
                    del nodes[pre_ind+1]
                    del inorder[in_ind-1]
                    break
                if in_ind+1 < len(inorder) and inorder[in_ind+1] == second:
                    nodes[pre_ind].right = nodes[pre_ind+1]
                    del preorder[pre_ind+1]
                    del nodes[pre_ind+1]
                    del inorder[in_ind+1]
                    break

        return nodes[0]


@pytest.mark.parametrize('solution_class', [SolutionClassic, SolutionSmall, SolutionWithPointers])
def test_build_tree(solution_class):
    tree = solution_class().buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20
    assert tree.right.left.val == 15
    assert tree.right.right.val == 7

    tree = solution_class().buildTree(preorder=[1,2], inorder=[1,2])
    assert tree.val == 1
    assert tree.right.val == 2

    tree = solution_class().buildTree(preorder=[1,2,3], inorder=[3,2,1])
    assert tree.val == 1
    assert tree.left.val == 2
    assert tree.left.left.val == 3

    tree = solution_class().buildTree(preorder=[2, 1, 3, 4], inorder=[1,2,3,4])
    assert tree.val == 2
    assert tree.left.val == 1
    assert tree.right.val == 3
    assert tree.right.right.val == 4

    assert solution_class().buildTree(preorder=[], inorder=[]) is None
