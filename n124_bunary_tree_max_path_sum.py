from typing import Optional

import pytest

import utility


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # I. doesnot pass all tests
        def max_path_and_leaf(node: TreeNode, path_prev: int, max_path: int, max_leaf: int) -> (int, int):
            path = path_prev + node.val

            if node.left and node.right:
                max_leaf_left, max_path_left = max_path_and_leaf(node.left, path, max_path, max_leaf)
                max_leaf_right, max_path_right = max_path_and_leaf(node.right, path, max_path, max_leaf)

                max_leaf = max(max_leaf_left, max_leaf_right)
                max_path = max(max_path_left, max_path_right, max_leaf_left + max_leaf_right + 2 * (0 if node == root else path) - node.val)
            elif node.left or node.right:
                ptr = node.left or node.right

                max_leaf_ptr, max_path_ptr = max_path_and_leaf(ptr, path, max_path, max_leaf)
                max_path = max_leaf_ptr
            else:
                max_leaf = path
                max_path = max_leaf

            return max_leaf, max_path

        return max_path_and_leaf(root, 0, -50000, -50000)[1]


class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Здесь идея примерно такая же, но теперь я иду обратным обходом и сохраняю максимальный найденный путь
        # и максимальный подпуть, проходящий через эту вершину
        def max_path_and_half_path(node: TreeNode) -> (int, int):
            if node.left and node.right:
                max_path_l, max_half_path_l = max_path_and_half_path(node.left)
                max_path_r, max_half_path_r = max_path_and_half_path(node.right)

                max_half_path = max(node.val, max_half_path_r+node.val, max_half_path_l+node.val)
                max_path = max(max_half_path, max_half_path_l + max_half_path_r + node.val, max_path_l, max_path_r)
            elif ptr := (node.left or node.right):
                max_path_p, max_half_path_p = max_path_and_half_path(ptr)

                max_half_path = max(node.val, max_half_path_p+node.val)
                max_path = max(max_half_path, max_half_path_p, max_path_p)
            else:
                max_path = max_half_path = node.val

            return max_path, max_half_path

        return max_path_and_half_path(root)[0]


@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[Solution1, TreeNode]))
def test_max_path_sum(solution_class):
    # [            1,
    #           null, -7,
    #               -9, -8,
    #        null, null, 3, null,
    #                null, -2]
    root = TreeNode(1)
    root.right = TreeNode(-7)
    root.right.left = TreeNode(-9)
    root.right.right = TreeNode(-8)
    root.right.right.left = TreeNode(3)
    root.right.right.left.right = TreeNode(-2)
    assert solution_class().maxPathSum(root) == 3


    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution_class().maxPathSum(root) == 3

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert solution_class().maxPathSum(root) == 42

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert solution_class().maxPathSum(root) == 6

    assert solution_class().maxPathSum(TreeNode(0)) == 0
