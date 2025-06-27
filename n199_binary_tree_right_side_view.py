from collections import deque
from typing import Optional, List

import pytest

from auxiliary_types import TreeNode


class SolutionRec:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # recursive
        def right_side_view(node: TreeNode, level: int, res: list[int]):
            if len(res) < level + 1:
                res.append(node.val)

            if node.right:
                right_side_view(node.right, level+1, res)
            if node.left:
                right_side_view(node.left, level+1, res)

        if not root:
            return []

        res = []
        right_side_view(root, 0, res)
        return res


class SolutionBFS_DEQUE:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS with deque
        if not root:
            return []

        res = []
        d = deque([root])
        while d:
            res.append(d[-1].val)
            for i in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res


class SolutionBFS_LISTS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Breadth-first-search (BFS)
        if not root:
            return []

        one_level_nodes = [root]
        right_side_view = []
        while len(one_level_nodes):
            right_side_view.append(one_level_nodes[0].val)
            new_one_level_nodes = []
            for node in one_level_nodes:
                if node.right:
                    new_one_level_nodes.append(node.right)
                if node.left:
                    new_one_level_nodes.append(node.left)
            one_level_nodes = new_one_level_nodes

        return right_side_view


@pytest.mark.parametrize('solution_class', [SolutionRec, SolutionBFS_LISTS, SolutionBFS_DEQUE])
def test_right_side_view(solution_class):
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(5)
    assert solution_class().rightSideView(root) == [1, 3, 4]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    assert solution_class().rightSideView(root) == [1, 3, 4, 5]

    root = TreeNode(1)
    root.right = TreeNode(3)
    assert solution_class().rightSideView(root) == [1, 3]
