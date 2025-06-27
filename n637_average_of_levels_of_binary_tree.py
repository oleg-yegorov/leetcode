from collections import deque
from typing import Optional, List

import pytest

from auxiliary_types import TreeNode


class SolutionDeque:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # with deques
        res = []
        d = deque([root])
        while d:
            res.append(sum(map(lambda n: n.val, d))/len(d))
            for _ in range(len(d)):
                node = d.popleft()

                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res


class SolutionLists:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # with lists
        level_nodes = [root]
        res = []
        while level_nodes:
            res.append(sum(map(lambda n: n.val, level_nodes))/len(level_nodes))
            new_level_nodes = []
            for node in level_nodes:
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)
            level_nodes = new_level_nodes
        return res


@pytest.mark.parametrize('solution_class', [SolutionLists, SolutionDeque])
def test_average_of_levels(solution_class):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution_class().averageOfLevels(root) == [3.0, 14.5, 11.0]
