from typing import Optional
import pytest

import utility


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        childs = []

        i = 0
        while nodes:
            i += 1
            for node in nodes:
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            nodes = childs
            childs = []

        return i


class SolutionDepthFirstSearch:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return max_depth


@pytest.mark.parametrize('solution_class', utility.get_module_classes(__name__, exclude_classes=[TreeNode]))
def test_max_depth_of_binary_tree(solution_class):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert solution_class().maxDepth(root) == 3
