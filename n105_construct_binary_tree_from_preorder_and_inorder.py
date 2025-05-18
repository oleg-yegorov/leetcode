from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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


def test_build_tree():
    tree = Solution().buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20
    assert tree.right.left.val == 15
    assert tree.right.right.val == 7

    tree = Solution().buildTree(preorder=[1,2], inorder=[1,2])
    assert tree.val == 1
    assert tree.right.val == 2

    tree = Solution().buildTree(preorder=[1,2,3], inorder=[3,2,1])
    assert tree.val == 1
    assert tree.left.val == 2
    assert tree.left.left.val == 3

    tree = Solution().buildTree(preorder=[2, 1, 3, 4], inorder=[1,2,3,4])
    assert tree.val == 2
    assert tree.left.val == 1
    assert tree.right.val == 3
    assert tree.right.right.val == 4
